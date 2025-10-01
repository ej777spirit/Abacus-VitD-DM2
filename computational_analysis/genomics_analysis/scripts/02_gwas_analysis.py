#!/usr/bin/env python3
"""
GWAS Analysis: VDR Variants and Type 2 Diabetes in African Ancestry Males

Performs genetic association analysis between VDR SNPs and T2D status,
examining the mediating role of vitamin D levels.

Created: October 1, 2025
"""

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

def load_data(data_path='../data/simulated/simulated_clinical_data.csv'):
    """Load simulated clinical data"""
    print("Loading data...")
    data = pd.read_csv(data_path)
    print(f"✓ Loaded {len(data)} samples")
    return data

def calculate_allele_frequencies(data, snps):
    """Calculate minor allele frequencies"""
    print("\nCalculating allele frequencies...")
    
    freq_data = []
    for snp in snps:
        allele_counts = data[snp].value_counts()
        total_alleles = len(data) * 2
        
        # Calculate MAF
        minor_allele_count = allele_counts.get(1, 0) + allele_counts.get(2, 0) * 2
        maf = minor_allele_count / total_alleles
        
        # Genotype frequencies
        freq_0 = allele_counts.get(0, 0) / len(data)
        freq_1 = allele_counts.get(1, 0) / len(data)
        freq_2 = allele_counts.get(2, 0) / len(data)
        
        freq_data.append({
            'SNP': snp,
            'MAF': maf,
            'Genotype_0_freq': freq_0,
            'Genotype_1_freq': freq_1,
            'Genotype_2_freq': freq_2
        })
    
    freq_df = pd.DataFrame(freq_data)
    print(f"✓ Calculated frequencies for {len(snps)} SNPs")
    return freq_df

def test_hardy_weinberg(data, snps):
    """Test Hardy-Weinberg equilibrium"""
    print("\nTesting Hardy-Weinberg equilibrium...")
    
    hwe_results = []
    for snp in snps:
        genotypes = data[snp].value_counts()
        n = len(data)
        
        n_aa = genotypes.get(0, 0)
        n_ab = genotypes.get(1, 0)
        n_bb = genotypes.get(2, 0)
        
        # Calculate expected frequencies
        p = (2 * n_aa + n_ab) / (2 * n)  # Major allele freq
        q = 1 - p  # Minor allele freq
        
        exp_aa = n * p ** 2
        exp_ab = n * 2 * p * q
        exp_bb = n * q ** 2
        
        # Chi-square test
        obs = np.array([n_aa, n_ab, n_bb])
        exp = np.array([exp_aa, exp_ab, exp_bb])
        chi2 = np.sum((obs - exp) ** 2 / exp)
        p_value = 1 - stats.chi2.cdf(chi2, df=1)
        
        hwe_results.append({
            'SNP': snp,
            'Chi2': chi2,
            'P_value': p_value,
            'HWE_status': 'Pass' if p_value > 0.001 else 'Fail'
        })
    
    hwe_df = pd.DataFrame(hwe_results)
    print(f"✓ HWE testing complete")
    return hwe_df

def association_analysis(data, snps, outcome='t2d_status'):
    """Perform association analysis between SNPs and T2D"""
    print(f"\nPerforming association analysis: SNPs vs {outcome}...")
    
    results = []
    for snp in snps:
        # Separate by T2D status
        cases = data[data[outcome] == 1][snp]
        controls = data[data[outcome] == 0][snp]
        
        # Mean genotype by group
        mean_cases = cases.mean()
        mean_controls = controls.mean()
        
        # T-test
        t_stat, t_pval = stats.ttest_ind(cases, controls)
        
        # Logistic regression (additive model)
        X = data[[snp, 'age', 'bmi']].values
        y = data[outcome].values
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        model = LogisticRegression(max_iter=1000)
        model.fit(X_scaled, y)
        
        # Odds ratio (approximate from coefficient)
        or_value = np.exp(model.coef_[0][0])
        
        # Effect size (Cohen's d)
        pooled_std = np.sqrt(((len(cases)-1)*cases.std()**2 + (len(controls)-1)*controls.std()**2) / (len(cases)+len(controls)-2))
        cohens_d = (mean_cases - mean_controls) / pooled_std if pooled_std > 0 else 0
        
        results.append({
            'SNP': snp,
            'Cases_mean': mean_cases,
            'Controls_mean': mean_controls,
            'Odds_Ratio': or_value,
            'T_statistic': t_stat,
            'P_value': t_pval,
            'Cohens_d': cohens_d,
            'Significance': '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'ns'
        })
    
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('P_value')
    print(f"✓ Association analysis complete")
    return results_df

def vitamin_d_association(data, snps):
    """Analyze SNP associations with vitamin D levels"""
    print("\nAnalyzing SNPs vs vitamin D levels...")
    
    results = []
    for snp in snps:
        # ANOVA for genotype groups
        groups = [data[data[snp] == i]['vitamin_d_ng_ml'].values for i in range(3)]
        f_stat, p_val = stats.f_oneway(*groups)
        
        # Linear regression
        X = data[[snp]].values
        y = data['vitamin_d_ng_ml'].values
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(X.flatten(), y)
        
        # Mean vitamin D by genotype
        means = [data[data[snp] == i]['vitamin_d_ng_ml'].mean() for i in range(3)]
        
        results.append({
            'SNP': snp,
            'Genotype_0_mean': means[0],
            'Genotype_1_mean': means[1],
            'Genotype_2_mean': means[2],
            'Beta': slope,
            'R_squared': r_value**2,
            'F_statistic': f_stat,
            'P_value': p_val,
            'Significance': '***' if p_val < 0.001 else '**' if p_val < 0.01 else '*' if p_val < 0.05 else 'ns'
        })
    
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('P_value')
    print(f"✓ Vitamin D association analysis complete")
    return results_df

def mediation_analysis(data):
    """Simple mediation analysis: VDR SNPs → Vitamin D → T2D"""
    print("\nPerforming mediation analysis...")
    
    # Focus on rs2228570 (FokI) - strongest effect
    snp = 'rs2228570'
    
    # Path a: SNP → Vitamin D
    X_a = data[[snp, 'age', 'bmi']].values
    y_a = data['vitamin_d_ng_ml'].values
    
    from sklearn.linear_model import LinearRegression
    model_a = LinearRegression()
    model_a.fit(X_a, y_a)
    path_a = model_a.coef_[0]  # Effect of SNP on Vit D
    
    # Path b: Vitamin D → T2D (controlling for SNP)
    X_b = data[['vitamin_d_ng_ml', snp, 'age', 'bmi']].values
    y_b = data['t2d_status'].values
    
    scaler = StandardScaler()
    X_b_scaled = scaler.fit_transform(X_b)
    
    model_b = LogisticRegression(max_iter=1000)
    model_b.fit(X_b_scaled, y_b)
    path_b = model_b.coef_[0][0]  # Effect of Vit D on T2D
    
    # Path c: Total effect (SNP → T2D)
    X_c = data[[snp, 'age', 'bmi']].values
    X_c_scaled = scaler.fit_transform(X_c)
    
    model_c = LogisticRegression(max_iter=1000)
    model_c.fit(X_c_scaled, y_b)
    path_c = model_c.coef_[0][0]  # Total effect
    
    # Path c': Direct effect (SNP → T2D, controlling for Vit D)
    path_c_prime = model_b.coef_[0][1]  # Direct effect
    
    # Indirect effect (mediation)
    indirect_effect = path_a * path_b
    prop_mediated = indirect_effect / path_c if path_c != 0 else 0
    
    mediation_results = {
        'SNP': snp,
        'Path_a_SNP_to_VitD': path_a,
        'Path_b_VitD_to_T2D': path_b,
        'Path_c_Total_effect': path_c,
        'Path_c_prime_Direct_effect': path_c_prime,
        'Indirect_effect': indirect_effect,
        'Proportion_mediated': prop_mediated * 100
    }
    
    print(f"✓ Mediation analysis complete")
    return pd.DataFrame([mediation_results])

def stratified_analysis(data, snps):
    """Stratified analysis by vitamin D status"""
    print("\nPerforming stratified analysis by vitamin D status...")
    
    results = []
    for snp in snps:
        for vit_d_status in ['Deficient', 'Insufficient', 'Sufficient']:
            subset = data[data['vit_d_status'] == vit_d_status]
            
            if len(subset) > 50:  # Minimum sample size
                cases = subset[subset['t2d_status'] == 1][snp]
                controls = subset[subset['t2d_status'] == 0][snp]
                
                if len(cases) > 0 and len(controls) > 0:
                    t_stat, p_val = stats.ttest_ind(cases, controls)
                    
                    results.append({
                        'SNP': snp,
                        'VitD_Status': vit_d_status,
                        'N': len(subset),
                        'N_cases': len(cases),
                        'Cases_mean': cases.mean(),
                        'Controls_mean': controls.mean(),
                        'P_value': p_val,
                        'Significance': '***' if p_val < 0.001 else '**' if p_val < 0.01 else '*' if p_val < 0.05 else 'ns'
                    })
    
    results_df = pd.DataFrame(results)
    print(f"✓ Stratified analysis complete")
    return results_df

def save_results(results_dict, output_dir='../results'):
    """Save all analysis results"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    print("\nSaving results...")
    for name, df in results_dict.items():
        filepath = f"{output_dir}/{name}.csv"
        df.to_csv(filepath, index=False)
        print(f"✓ Saved: {filepath}")

if __name__ == '__main__':
    # Load data
    data = load_data()
    snps = ['rs2228570', 'rs1544410', 'rs7975232', 'rs731236']
    
    # Perform analyses
    freq_results = calculate_allele_frequencies(data, snps)
    hwe_results = test_hardy_weinberg(data, snps)
    assoc_results = association_analysis(data, snps)
    vitd_results = vitamin_d_association(data, snps)
    mediation_results = mediation_analysis(data)
    stratified_results = stratified_analysis(data, snps)
    
    # Save all results
    results_dict = {
        'allele_frequencies': freq_results,
        'hardy_weinberg_test': hwe_results,
        'snp_t2d_association': assoc_results,
        'snp_vitd_association': vitd_results,
        'mediation_analysis': mediation_results,
        'stratified_analysis': stratified_results
    }
    
    save_results(results_dict)
    
    print("\n" + "="*60)
    print("GWAS ANALYSIS COMPLETE")
    print("="*60)
    print("\nTop Associations (SNP → T2D):")
    print(assoc_results[['SNP', 'Odds_Ratio', 'P_value', 'Significance']].to_string(index=False))
    
    print("\nTop Associations (SNP → Vitamin D):")
    print(vitd_results[['SNP', 'Beta', 'P_value', 'Significance']].head().to_string(index=False))
    
    print("\nMediation Analysis (rs2228570):")
    print(f"  Proportion of effect mediated by vitamin D: {mediation_results['Proportion_mediated'].values[0]:.1f}%")
    
    print("\n✓ All results saved in: ../results/")
