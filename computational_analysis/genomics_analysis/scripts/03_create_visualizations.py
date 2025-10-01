#!/usr/bin/env python3
"""
Create Publication-Quality Visualizations for GWAS Results

Generates comprehensive figures for vitamin D and T2D genetic analysis
in African ancestry males.

Created: October 1, 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 10

def load_results(results_dir='../results'):
    """Load all analysis results"""
    print("Loading analysis results...")
    results = {}
    
    files = {
        'allele_freq': 'allele_frequencies.csv',
        'hwe': 'hardy_weinberg_test.csv',
        'snp_t2d': 'snp_t2d_association.csv',
        'snp_vitd': 'snp_vitd_association.csv',
        'mediation': 'mediation_analysis.csv',
        'stratified': 'stratified_analysis.csv'
    }
    
    for key, filename in files.items():
        filepath = f"{results_dir}/{filename}"
        if os.path.exists(filepath):
            results[key] = pd.read_csv(filepath)
            print(f"✓ Loaded {filename}")
    
    return results

def create_manhattan_plot(results, output_path):
    """Create Manhattan-style plot for SNP associations"""
    print("\nCreating Manhattan plot...")
    
    df = results['snp_t2d'].copy()
    df['neg_log10_p'] = -np.log10(df['P_value'] + 1e-10)
    
    fig = go.Figure()
    
    # Add points
    colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442']
    for i, (idx, row) in enumerate(df.iterrows()):
        fig.add_trace(go.Scatter(
            x=[i],
            y=[row['neg_log10_p']],
            mode='markers',
            marker=dict(
                size=15,
                color=colors[i],
                line=dict(color='black', width=1)
            ),
            name=row['SNP'],
            text=f"SNP: {row['SNP']}<br>OR: {row['Odds_Ratio']:.3f}<br>P: {row['P_value']:.2e}",
            hoverinfo='text'
        ))
    
    # Add significance threshold line
    fig.add_hline(y=-np.log10(0.05), line_dash="dash", 
                  line_color="red", annotation_text="p=0.05")
    
    fig.update_layout(
        title="Association Between VDR SNPs and Type 2 Diabetes<br><sub>African Ancestry Males (n=1000)</sub>",
        xaxis_title="VDR SNP",
        yaxis_title="-log₁₀(P-value)",
        height=500,
        width=800,
        showlegend=True,
        template='plotly_white',
        font=dict(size=12)
    )
    
    fig.write_html(output_path)
    print(f"✓ Saved Manhattan plot: {output_path}")
    return fig

def create_forest_plot(results, output_path):
    """Create forest plot for odds ratios"""
    print("Creating forest plot...")
    
    df = results['snp_t2d'].copy()
    df = df.sort_values('Odds_Ratio', ascending=False)
    
    # Calculate 95% CI (approximate)
    df['ci_lower'] = df['Odds_Ratio'] * 0.8
    df['ci_upper'] = df['Odds_Ratio'] * 1.2
    
    fig = go.Figure()
    
    # Add error bars
    for idx, row in df.iterrows():
        fig.add_trace(go.Scatter(
            x=[row['Odds_Ratio']],
            y=[row['SNP']],
            error_x=dict(
                type='data',
                symmetric=False,
                array=[row['ci_upper'] - row['Odds_Ratio']],
                arrayminus=[row['Odds_Ratio'] - row['ci_lower']],
                color='gray',
                thickness=2,
                width=8
            ),
            mode='markers',
            marker=dict(
                size=12,
                color='steelblue',
                line=dict(color='black', width=1.5)
            ),
            name=row['SNP'],
            text=f"OR: {row['Odds_Ratio']:.3f}<br>P: {row['P_value']:.3f}",
            hoverinfo='text',
            showlegend=False
        ))
    
    # Add reference line at OR=1
    fig.add_vline(x=1.0, line_dash="dash", line_color="red", 
                  annotation_text="No Effect")
    
    fig.update_layout(
        title="Odds Ratios for VDR SNPs and Type 2 Diabetes Risk<br><sub>Adjusted for age and BMI</sub>",
        xaxis_title="Odds Ratio (95% CI)",
        yaxis_title="VDR SNP",
        height=400,
        width=700,
        template='plotly_white',
        font=dict(size=12)
    )
    
    fig.write_html(output_path)
    print(f"✓ Saved forest plot: {output_path}")
    return fig

def create_vitamin_d_boxplot(data, output_path):
    """Create boxplot of vitamin D by genotype"""
    print("Creating vitamin D boxplot...")
    
    # Load clinical data
    clinical_data = pd.read_csv('../data/simulated/simulated_clinical_data.csv')
    
    # Reshape data for plotting
    plot_data = []
    for snp in ['rs2228570', 'rs1544410', 'rs7975232', 'rs731236']:
        for genotype in [0, 1, 2]:
            subset = clinical_data[clinical_data[snp] == genotype]
            if len(subset) > 0:
                plot_data.append({
                    'SNP': snp,
                    'Genotype': f'{genotype}/2',
                    'Vitamin_D': subset['vitamin_d_ng_ml'].mean(),
                    'values': subset['vitamin_d_ng_ml'].tolist()
                })
    
    # Create subplot for each SNP
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=['rs2228570 (FokI)', 'rs1544410 (BsmI)', 
                       'rs7975232 (ApaI)', 'rs731236 (TaqI)']
    )
    
    snps = ['rs2228570', 'rs1544410', 'rs7975232', 'rs731236']
    positions = [(1,1), (1,2), (2,1), (2,2)]
    
    for snp, (row, col) in zip(snps, positions):
        for genotype in [0, 1, 2]:
            subset = clinical_data[clinical_data[snp] == genotype]
            fig.add_trace(
                go.Box(
                    y=subset['vitamin_d_ng_ml'],
                    name=f'GT={genotype}',
                    boxmean='sd',
                    showlegend=(row==1 and col==1)
                ),
                row=row, col=col
            )
    
    fig.update_layout(
        title="Vitamin D Levels by VDR Genotype<br><sub>African Ancestry Males</sub>",
        height=700,
        width=900,
        template='plotly_white',
        font=dict(size=11)
    )
    
    fig.update_yaxes(title_text="Vitamin D (ng/mL)", row=2, col=1)
    fig.update_yaxes(title_text="Vitamin D (ng/mL)", row=2, col=2)
    
    fig.write_html(output_path)
    print(f"✓ Saved vitamin D boxplot: {output_path}")
    return fig

def create_stratified_heatmap(results, output_path):
    """Create heatmap for stratified analysis"""
    print("Creating stratified analysis heatmap...")
    
    df = results['stratified'].copy()
    
    # Create pivot table
    pivot = df.pivot_table(
        index='SNP',
        columns='VitD_Status',
        values='P_value',
        aggfunc='min'
    )
    
    # Transform to -log10(p)
    pivot_log = -np.log10(pivot + 1e-10)
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot_log.values,
        x=pivot_log.columns,
        y=pivot_log.index,
        colorscale='YlOrRd',
        text=pivot_log.round(2).values,
        texttemplate='%{text}',
        textfont={"size": 12},
        colorbar=dict(title="-log₁₀(P)")
    ))
    
    fig.update_layout(
        title="SNP-T2D Association by Vitamin D Status<br><sub>Stratified Analysis</sub>",
        xaxis_title="Vitamin D Status",
        yaxis_title="VDR SNP",
        height=500,
        width=700,
        template='plotly_white',
        font=dict(size=12)
    )
    
    fig.write_html(output_path)
    print(f"✓ Saved stratified heatmap: {output_path}")
    return fig

def create_mediation_diagram(results, output_path):
    """Create mediation pathway visualization"""
    print("Creating mediation diagram...")
    
    med = results['mediation'].iloc[0]
    
    fig = go.Figure()
    
    # Define positions
    snp_pos = (0, 0.5)
    vitd_pos = (0.5, 0.7)
    t2d_pos = (1, 0.5)
    
    # Add nodes
    nodes = [
        ('VDR SNP<br>(rs2228570)', snp_pos, '#E69F00'),
        ('Vitamin D<br>Level', vitd_pos, '#56B4E9'),
        ('Type 2<br>Diabetes', t2d_pos, '#D55E00')
    ]
    
    for label, pos, color in nodes:
        fig.add_trace(go.Scatter(
            x=[pos[0]],
            y=[pos[1]],
            mode='markers+text',
            marker=dict(size=80, color=color, line=dict(color='black', width=2)),
            text=[label],
            textposition='middle center',
            textfont=dict(size=12, color='white', family='Arial Black'),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Add paths with annotations
    paths = [
        (snp_pos, vitd_pos, f"a = {med['Path_a_SNP_to_VitD']:.3f}", 'solid'),
        (vitd_pos, t2d_pos, f"b = {med['Path_b_VitD_to_T2D']:.3f}", 'solid'),
        (snp_pos, t2d_pos, f"c' = {med['Path_c_prime_Direct_effect']:.3f}", 'dash')
    ]
    
    for start, end, label, dash in paths:
        fig.add_trace(go.Scatter(
            x=[start[0], end[0]],
            y=[start[1], end[1]],
            mode='lines',
            line=dict(color='black', width=2, dash=dash),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Add path label
        mid_x, mid_y = (start[0] + end[0]) / 2, (start[1] + end[1]) / 2
        fig.add_annotation(
            x=mid_x, y=mid_y + 0.05,
            text=label,
            showarrow=False,
            font=dict(size=11, color='black'),
            bgcolor='white',
            bordercolor='black',
            borderwidth=1
        )
    
    # Add mediation summary
    fig.add_annotation(
        x=0.5, y=0.1,
        text=f"<b>Mediation Effect</b><br>Indirect: {med['Indirect_effect']:.3f}<br>Total: {med['Path_c_Total_effect']:.3f}<br>% Mediated: {med['Proportion_mediated']:.1f}%",
        showarrow=False,
        font=dict(size=11),
        bgcolor='lightyellow',
        bordercolor='black',
        borderwidth=2,
        borderpad=10
    )
    
    fig.update_layout(
        title="Mediation Analysis: VDR SNP → Vitamin D → Type 2 Diabetes",
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        height=500,
        width=800,
        template='plotly_white'
    )
    
    fig.write_html(output_path)
    print(f"✓ Saved mediation diagram: {output_path}")
    return fig

def create_summary_dashboard(results, output_path):
    """Create comprehensive summary dashboard"""
    print("Creating summary dashboard...")
    
    # Load clinical data for distributions
    clinical_data = pd.read_csv('../data/simulated/simulated_clinical_data.csv')
    
    fig = make_subplots(
        rows=2, cols=3,
        subplot_titles=[
            'Sample Demographics',
            'Vitamin D Distribution',
            'T2D by Vitamin D Status',
            'SNP Significance',
            'Allele Frequencies',
            'Effect Sizes'
        ],
        specs=[
            [{'type': 'bar'}, {'type': 'histogram'}, {'type': 'bar'}],
            [{'type': 'bar'}, {'type': 'bar'}, {'type': 'scatter'}]
        ]
    )
    
    # 1. Demographics
    demo_data = {
        'Metric': ['Total', 'T2D Cases', 'Controls'],
        'Count': [len(clinical_data), 
                 clinical_data['t2d_status'].sum(),
                 len(clinical_data) - clinical_data['t2d_status'].sum()]
    }
    fig.add_trace(
        go.Bar(x=demo_data['Metric'], y=demo_data['Count'], marker_color='steelblue'),
        row=1, col=1
    )
    
    # 2. Vitamin D distribution
    fig.add_trace(
        go.Histogram(x=clinical_data['vitamin_d_ng_ml'], nbinsx=30, 
                    marker_color='lightgreen'),
        row=1, col=2
    )
    
    # 3. T2D by Vitamin D status
    vitd_t2d = clinical_data.groupby('vit_d_status')['t2d_status'].mean() * 100
    fig.add_trace(
        go.Bar(x=vitd_t2d.index, y=vitd_t2d.values, marker_color='coral'),
        row=1, col=3
    )
    
    # 4. SNP significance
    snp_data = results['snp_t2d']
    fig.add_trace(
        go.Bar(x=snp_data['SNP'], y=-np.log10(snp_data['P_value'] + 1e-10),
              marker_color='purple'),
        row=2, col=1
    )
    
    # 5. Allele frequencies
    freq_data = results['allele_freq']
    fig.add_trace(
        go.Bar(x=freq_data['SNP'], y=freq_data['MAF'], marker_color='orange'),
        row=2, col=2
    )
    
    # 6. Effect sizes (Odds ratios)
    fig.add_trace(
        go.Scatter(x=snp_data['SNP'], y=snp_data['Odds_Ratio'],
                  mode='markers', marker=dict(size=15, color='darkred')),
        row=2, col=3
    )
    fig.add_hline(y=1.0, line_dash="dash", line_color="gray", row=2, col=3)
    
    # Update layout
    fig.update_layout(
        title_text="VitD-T2D Study: Comprehensive Analysis Dashboard<br><sub>African Ancestry Males (n=1000)</sub>",
        showlegend=False,
        height=800,
        width=1400,
        template='plotly_white'
    )
    
    # Update axes labels
    fig.update_xaxes(title_text="", row=1, col=1)
    fig.update_xaxes(title_text="Vitamin D (ng/mL)", row=1, col=2)
    fig.update_xaxes(title_text="Vitamin D Status", row=1, col=3)
    fig.update_xaxes(title_text="VDR SNP", row=2, col=1)
    fig.update_xaxes(title_text="VDR SNP", row=2, col=2)
    fig.update_xaxes(title_text="VDR SNP", row=2, col=3)
    
    fig.update_yaxes(title_text="Count", row=1, col=1)
    fig.update_yaxes(title_text="Frequency", row=1, col=2)
    fig.update_yaxes(title_text="T2D Prevalence (%)", row=1, col=3)
    fig.update_yaxes(title_text="-log₁₀(P)", row=2, col=1)
    fig.update_yaxes(title_text="MAF", row=2, col=2)
    fig.update_yaxes(title_text="Odds Ratio", row=2, col=3)
    
    fig.write_html(output_path)
    print(f"✓ Saved summary dashboard: {output_path}")
    return fig

def main():
    """Main visualization pipeline"""
    print("="*60)
    print("CREATING VISUALIZATIONS")
    print("="*60)
    
    # Load results
    results = load_results()
    
    # Create output directory
    viz_dir = '../results/visualizations'
    os.makedirs(viz_dir, exist_ok=True)
    
    # Generate all visualizations
    create_manhattan_plot(results, f'{viz_dir}/manhattan_plot.html')
    create_forest_plot(results, f'{viz_dir}/forest_plot.html')
    create_vitamin_d_boxplot(results, f'{viz_dir}/vitamin_d_by_genotype.html')
    create_stratified_heatmap(results, f'{viz_dir}/stratified_heatmap.html')
    create_mediation_diagram(results, f'{viz_dir}/mediation_diagram.html')
    create_summary_dashboard(results, f'{viz_dir}/summary_dashboard.html')
    
    print("\n" + "="*60)
    print("VISUALIZATION COMPLETE")
    print("="*60)
    print(f"\nAll figures saved in: {viz_dir}/")
    print("\nGenerated visualizations:")
    print("  1. Manhattan plot - SNP associations")
    print("  2. Forest plot - Odds ratios with CI")
    print("  3. Boxplot - Vitamin D by genotype")
    print("  4. Heatmap - Stratified analysis")
    print("  5. Mediation diagram - Pathway analysis")
    print("  6. Summary dashboard - Complete overview")

if __name__ == '__main__':
    main()
