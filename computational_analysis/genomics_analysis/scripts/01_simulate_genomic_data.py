#!/usr/bin/env python3
"""
Simulate Genomic Data for Vitamin D and Type 2 Diabetes Study
African Ancestry Males Population

This script generates simulated data to demonstrate the analysis pipeline
when real restricted datasets are not accessible.

Created: October 1, 2025
"""

import numpy as np
import pandas as pd
from scipy import stats
import os

# Set random seed for reproducibility
np.random.seed(42)

def generate_vdr_genotypes(n_samples=1000):
    """
    Generate VDR genotype data for key variants
    
    Key VDR SNPs in African ancestry populations:
    - rs2228570 (FokI): C>T, associated with vitamin D metabolism
    - rs1544410 (BsmI): G>A, linked to bone mineral density
    - rs7975232 (ApaI): C>A, affects VDR expression
    - rs731236 (TaqI): T>C, regulatory region
    """
    
    # Minor allele frequencies (MAF) for African ancestry
    snps = {
        'rs2228570': {'maf': 0.37, 'effect': 1.3},  # FokI - stronger effect
        'rs1544410': {'maf': 0.28, 'effect': 1.15}, # BsmI
        'rs7975232': {'maf': 0.35, 'effect': 1.12}, # ApaI
        'rs731236': {'maf': 0.42, 'effect': 1.08},  # TaqI
    }
    
    genotypes = pd.DataFrame()
    genotypes['sample_id'] = [f'AAM_{i:04d}' for i in range(n_samples)]
    
    # Generate genotypes (0, 1, 2 copies of minor allele)
    for snp, info in snps.items():
        maf = info['maf']
        # Hardy-Weinberg equilibrium
        p_aa = (1 - maf) ** 2
        p_ab = 2 * maf * (1 - maf)
        p_bb = maf ** 2
        
        genotypes[snp] = np.random.choice([0, 1, 2], size=n_samples, 
                                         p=[p_aa, p_ab, p_bb])
    
    return genotypes, snps

def generate_vitamin_d_levels(genotypes, snps, base_mean=20, base_sd=8):
    """
    Generate vitamin D levels influenced by VDR genotypes
    Base levels typical for African ancestry males (lower due to melanin)
    """
    n_samples = len(genotypes)
    
    # Baseline vitamin D levels
    vit_d = np.random.normal(base_mean, base_sd, n_samples)
    
    # Add genetic effects
    for snp, info in snps.items():
        effect = info['effect']
        genotype_effect = genotypes[snp].values * np.log(effect)
        vit_d += genotype_effect * 2  # Scale the effect
    
    # Add environmental factors (season, sun exposure)
    seasonal_effect = np.random.normal(0, 3, n_samples)
    vit_d += seasonal_effect
    
    # Ensure realistic bounds (5-60 ng/mL)
    vit_d = np.clip(vit_d, 5, 60)
    
    return vit_d

def generate_t2d_status(vit_d_levels, genotypes, snps, base_prevalence=0.15):
    """
    Generate Type 2 Diabetes status based on vitamin D levels and genetics
    Higher prevalence in African ancestry populations
    """
    n_samples = len(vit_d_levels)
    
    # Calculate risk score
    risk_score = np.zeros(n_samples)
    
    # Vitamin D effect (lower levels increase risk)
    vit_d_risk = -0.05 * (vit_d_levels - 30)  # Optimal around 30 ng/mL
    risk_score += vit_d_risk
    
    # VDR genetic effects
    for snp, info in snps.items():
        genetic_risk = genotypes[snp].values * np.log(info['effect']) * 0.5
        risk_score += genetic_risk
    
    # Age effect (45-75 years)
    ages = np.random.randint(45, 76, n_samples)
    age_risk = (ages - 45) * 0.03
    risk_score += age_risk
    
    # BMI effect (20-45)
    bmi = np.random.normal(28, 5, n_samples)  # Higher average for African ancestry
    bmi_risk = (bmi - 25) * 0.15
    risk_score += bmi_risk
    
    # Convert risk score to probability using logistic function
    base_logit = np.log(base_prevalence / (1 - base_prevalence))
    prob_t2d = 1 / (1 + np.exp(-(base_logit + risk_score)))
    
    # Generate T2D status
    t2d_status = np.random.binomial(1, prob_t2d)
    
    # Generate HbA1c levels
    hba1c = np.where(t2d_status == 1,
                     np.random.normal(7.5, 1.2, n_samples),  # Diabetic
                     np.random.normal(5.4, 0.4, n_samples))  # Non-diabetic
    
    return t2d_status, ages, bmi, hba1c

def generate_clinical_data(n_samples=1000):
    """
    Generate complete clinical dataset
    """
    print(f"Generating simulated genomic data for {n_samples} African ancestry males...")
    
    # Generate genotypes
    genotypes, snps = generate_vdr_genotypes(n_samples)
    print(f"✓ Generated VDR genotypes for {len(snps)} SNPs")
    
    # Generate vitamin D levels
    vit_d = generate_vitamin_d_levels(genotypes, snps)
    print(f"✓ Generated vitamin D levels (mean: {vit_d.mean():.1f} ng/mL)")
    
    # Generate T2D status and related variables
    t2d_status, ages, bmi, hba1c = generate_t2d_status(vit_d, genotypes, snps)
    print(f"✓ Generated T2D status (prevalence: {t2d_status.mean()*100:.1f}%)")
    
    # Combine all data
    clinical_data = genotypes.copy()
    clinical_data['age'] = ages
    clinical_data['bmi'] = bmi
    clinical_data['vitamin_d_ng_ml'] = vit_d
    clinical_data['t2d_status'] = t2d_status
    clinical_data['hba1c_percent'] = hba1c
    
    # Add deficiency categories
    clinical_data['vit_d_status'] = pd.cut(vit_d, 
                                           bins=[0, 20, 30, 100],
                                           labels=['Deficient', 'Insufficient', 'Sufficient'])
    
    # Add ancestry (all African ancestry for this simulation)
    clinical_data['ancestry'] = 'African'
    clinical_data['sex'] = 'Male'
    
    return clinical_data, snps

def save_data(clinical_data, output_dir):
    """Save simulated data in multiple formats"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Save full dataset
    clinical_data.to_csv(f'{output_dir}/simulated_clinical_data.csv', index=False)
    print(f"\n✓ Saved clinical data: {output_dir}/simulated_clinical_data.csv")
    
    # Save genotype matrix (PLINK-like format)
    genotype_cols = ['sample_id', 'rs2228570', 'rs1544410', 'rs7975232', 'rs731236']
    clinical_data[genotype_cols].to_csv(f'{output_dir}/genotypes.txt', 
                                        sep='\t', index=False)
    print(f"✓ Saved genotypes: {output_dir}/genotypes.txt")
    
    # Save phenotype file
    pheno_cols = ['sample_id', 'age', 'bmi', 'vitamin_d_ng_ml', 't2d_status', 'hba1c_percent']
    clinical_data[pheno_cols].to_csv(f'{output_dir}/phenotypes.txt',
                                     sep='\t', index=False)
    print(f"✓ Saved phenotypes: {output_dir}/phenotypes.txt")
    
    # Generate summary statistics
    summary = {
        'Total Samples': len(clinical_data),
        'T2D Cases': clinical_data['t2d_status'].sum(),
        'T2D Controls': (1 - clinical_data['t2d_status']).sum(),
        'T2D Prevalence (%)': clinical_data['t2d_status'].mean() * 100,
        'Mean Age': clinical_data['age'].mean(),
        'Mean BMI': clinical_data['bmi'].mean(),
        'Mean Vitamin D (ng/mL)': clinical_data['vitamin_d_ng_ml'].mean(),
        'Vitamin D Deficient (%)': (clinical_data['vit_d_status'] == 'Deficient').sum() / len(clinical_data) * 100,
        'Mean HbA1c (%)': clinical_data['hba1c_percent'].mean(),
    }
    
    summary_df = pd.DataFrame([summary])
    summary_df.to_csv(f'{output_dir}/data_summary.csv', index=False)
    print(f"✓ Saved summary: {output_dir}/data_summary.csv")
    
    return summary

if __name__ == '__main__':
    # Generate data
    clinical_data, snps = generate_clinical_data(n_samples=1000)
    
    # Save data
    output_dir = '../data/simulated'
    summary = save_data(clinical_data, output_dir)
    
    # Print summary
    print("\n" + "="*60)
    print("SIMULATION SUMMARY")
    print("="*60)
    for key, value in summary.items():
        if isinstance(value, float):
            print(f"{key:.<40} {value:.2f}")
        else:
            print(f"{key:.<40} {value}")
    
    print("\n✓ Data generation complete!")
    print(f"  Files saved in: {output_dir}/")
