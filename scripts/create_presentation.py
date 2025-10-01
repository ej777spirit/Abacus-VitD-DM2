#!/usr/bin/env python3
"""
Create PhD Thesis Committee Presentation
Vitamin D and Type 2 Diabetes in African Ancestry Males
"""

import os
from datetime import datetime

# Create presentation directory
os.makedirs('thesis_presentation', exist_ok=True)

# HTML presentation with reveal.js style
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vitamin D and Type 2 Diabetes in African Ancestry Males</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            overflow-x: hidden;
        }
        
        .slide-container {
            width: 100%;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .slide {
            min-height: 100vh;
            padding: 60px 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            background: white;
            margin-bottom: 2px;
            page-break-after: always;
        }
        
        .slide.title-slide {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            justify-content: center;
        }
        
        .slide.section-slide {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            justify-content: center;
            text-align: center;
        }
        
        h1 {
            font-size: 3.5em;
            margin-bottom: 30px;
            font-weight: 700;
            line-height: 1.2;
        }
        
        h2 {
            font-size: 2.5em;
            margin-bottom: 30px;
            color: #667eea;
            border-bottom: 4px solid #667eea;
            padding-bottom: 15px;
        }
        
        .section-slide h2 {
            color: white;
            border-bottom: 4px solid white;
            font-size: 3em;
        }
        
        h3 {
            font-size: 1.8em;
            margin: 25px 0 15px 0;
            color: #764ba2;
        }
        
        .subtitle {
            font-size: 1.5em;
            margin-bottom: 40px;
            opacity: 0.9;
        }
        
        .author-info {
            font-size: 1.2em;
            margin-top: 50px;
            line-height: 1.8;
        }
        
        .content {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        
        ul, ol {
            margin: 20px 0 20px 40px;
            line-height: 2;
            font-size: 1.1em;
        }
        
        li {
            margin: 15px 0;
        }
        
        .two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin: 30px 0;
        }
        
        .box {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            border-left: 5px solid #667eea;
        }
        
        .highlight {
            background: #fff3cd;
            padding: 20px;
            border-radius: 8px;
            border-left: 5px solid #ffc107;
            margin: 20px 0;
            font-size: 1.1em;
        }
        
        .key-finding {
            background: #d4edda;
            padding: 20px;
            border-radius: 8px;
            border-left: 5px solid #28a745;
            margin: 20px 0;
            font-size: 1.1em;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 1em;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        th {
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }
        
        td {
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
        }
        
        tr:hover {
            background: #f8f9fa;
        }
        
        .footer {
            margin-top: auto;
            padding-top: 30px;
            text-align: center;
            font-size: 0.9em;
            color: #666;
            border-top: 2px solid #eee;
        }
        
        .slide-number {
            position: absolute;
            bottom: 30px;
            right: 40px;
            font-size: 0.9em;
            color: #999;
        }
        
        strong {
            color: #667eea;
            font-weight: 600;
        }
        
        .methodology-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin: 30px 0;
        }
        
        .method-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-top: 4px solid #667eea;
        }
        
        .method-card h4 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin: 30px 0;
        }
        
        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: 700;
            margin-bottom: 10px;
        }
        
        .stat-label {
            font-size: 0.9em;
            opacity: 0.9;
        }
        
        .image-container {
            text-align: center;
            margin: 30px 0;
        }
        
        .image-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .caption {
            font-size: 0.9em;
            color: #666;
            margin-top: 10px;
            font-style: italic;
        }
        
        @media print {
            .slide {
                page-break-after: always;
                min-height: 100vh;
            }
        }
    </style>
</head>
<body>
    <div class="slide-container">
        
        <!-- Slide 1: Title -->
        <div class="slide title-slide">
            <h1>Vitamin D and Type 2 Diabetes in African Ancestry Males</h1>
            <p class="subtitle">A Multi-Omics Investigation of Genetic, Proteomic, and Metabolomic Mechanisms</p>
            <div class="author-info">
                <p><strong>PhD Candidate:</strong> [Your Name]</p>
                <p><strong>Advisor:</strong> [Advisor Name]</p>
                <p><strong>Committee:</strong> [Committee Members]</p>
                <p><strong>Date:</strong> October 1, 2025</p>
                <p><strong>Institution:</strong> [Your Institution]</p>
            </div>
        </div>

        <!-- Slide 2: Overview -->
        <div class="slide">
            <h2>Presentation Overview</h2>
            <div class="content">
                <ol style="font-size: 1.2em; line-height: 2.2;">
                    <li><strong>Background & Significance</strong> - Health disparities and the vitamin D paradox</li>
                    <li><strong>Research Hypothesis</strong> - Ancestry-specific mechanisms</li>
                    <li><strong>Specific Aims</strong> - Multi-omics hierarchical approach</li>
                    <li><strong>Methodology</strong> - Computational pipeline and datasets</li>
                    <li><strong>Preliminary Results</strong> - Genomic analysis findings</li>
                    <li><strong>Expected Outcomes</strong> - Scientific and clinical impact</li>
                    <li><strong>Timeline & Next Steps</strong> - Path to completion</li>
                </ol>
            </div>
            <div class="slide-number">2</div>
        </div>

        <!-- Slide 3: Section - Background -->
        <div class="slide section-slide">
            <h2>Background & Significance</h2>
            <div class="slide-number">3</div>
        </div>

        <!-- Slide 4: The Problem -->
        <div class="slide">
            <h2>The Problem: Health Disparities in T2D</h2>
            <div class="content">
                <div class="stats-grid">
                    <div class="stat-box">
                        <div class="stat-number">60-100%</div>
                        <div class="stat-label">Higher T2D prevalence in African Americans</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">13.4%</div>
                        <div class="stat-label">T2D prevalence in African Americans</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">7.5%</div>
                        <div class="stat-label">T2D prevalence in non-Hispanic whites</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">2.5x</div>
                        <div class="stat-label">Higher risk of complications</div>
                    </div>
                </div>
                
                <div class="highlight">
                    <strong>Key Challenge:</strong> Most T2D research has been conducted in European ancestry populations, limiting our understanding of mechanisms in African ancestry populations.
                </div>
                
                <h3>Contributing Factors</h3>
                <ul>
                    <li><strong>Genetic factors:</strong> Ancestry-specific variants and allele frequencies</li>
                    <li><strong>Environmental factors:</strong> Diet, physical activity, socioeconomic status</li>
                    <li><strong>Biological factors:</strong> Vitamin D metabolism, insulin sensitivity</li>
                    <li><strong>Healthcare access:</strong> Disparities in screening and treatment</li>
                </ul>
            </div>
            <div class="slide-number">4</div>
        </div>

        <!-- Slide 5: The Vitamin D Paradox -->
        <div class="slide">
            <h2>The Vitamin D Paradox</h2>
            <div class="content">
                <div class="two-column">
                    <div class="box">
                        <h3>Observations in African Ancestry</h3>
                        <ul>
                            <li>Lower serum 25(OH)D levels (often <20 ng/mL)</li>
                            <li>Higher prevalence of "vitamin D deficiency"</li>
                            <li>Yet: Better bone health than Europeans</li>
                            <li>Yet: Different metabolic responses</li>
                        </ul>
                    </div>
                    <div class="box">
                        <h3>Proposed Mechanisms</h3>
                        <ul>
                            <li><strong>VDBP polymorphisms:</strong> Gc1f allele (~80% in Africans vs ~1% in Europeans)</li>
                            <li><strong>Bioavailable vitamin D:</strong> Free and albumin-bound forms</li>
                            <li><strong>VDR sensitivity:</strong> Receptor expression and signaling</li>
                            <li><strong>Metabolic efficiency:</strong> Different enzyme activities</li>
                        </ul>
                    </div>
                </div>
                
                <div class="key-finding">
                    <strong>Critical Insight:</strong> Total serum 25(OH)D may not accurately reflect vitamin D bioactivity in African ancestry populations due to genetic differences in binding proteins and receptors.
                </div>
            </div>
            <div class="slide-number">5</div>
        </div>

        <!-- Slide 6: Vitamin D and T2D Connection -->
        <div class="slide">
            <h2>Vitamin D and Type 2 Diabetes: The Connection</h2>
            <div class="content">
                <h3>Biological Mechanisms</h3>
                <div class="two-column">
                    <div>
                        <h4 style="color: #667eea;">Pancreatic Beta Cells</h4>
                        <ul>
                            <li>VDR expression in beta cells</li>
                            <li>Insulin synthesis and secretion</li>
                            <li>Beta cell survival and proliferation</li>
                            <li>Protection from inflammation</li>
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #667eea;">Insulin Sensitivity</h4>
                        <ul>
                            <li>Insulin receptor expression</li>
                            <li>Glucose transporter regulation</li>
                            <li>Inflammatory cytokine modulation</li>
                            <li>Adipocyte function</li>
                        </ul>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Evidence from Studies</h3>
                <table>
                    <tr>
                        <th>Study Type</th>
                        <th>Finding</th>
                        <th>Effect Size</th>
                    </tr>
                    <tr>
                        <td>Observational</td>
                        <td>Low 25(OH)D associated with T2D risk</td>
                        <td>OR: 1.3-1.8</td>
                    </tr>
                    <tr>
                        <td>Genetic (GWAS)</td>
                        <td>VDR, GC variants associated with T2D</td>
                        <td>OR: 1.1-1.3</td>
                    </tr>
                    <tr>
                        <td>Intervention</td>
                        <td>Mixed results for supplementation</td>
                        <td>Variable</td>
                    </tr>
                </table>
            </div>
            <div class="slide-number">6</div>
        </div>

        <!-- Slide 7: Research Gap -->
        <div class="slide">
            <h2>Research Gap & Innovation</h2>
            <div class="content">
                <div class="highlight">
                    <h3 style="margin-top: 0;">Critical Gap</h3>
                    <p><strong>No comprehensive multi-omics study has investigated vitamin D-T2D mechanisms specifically in African ancestry males.</strong></p>
                </div>
                
                <h3>Why This Matters</h3>
                <div class="two-column">
                    <div class="box">
                        <h4>Scientific Impact</h4>
                        <ul>
                            <li>Understand ancestry-specific mechanisms</li>
                            <li>Resolve vitamin D paradox</li>
                            <li>Identify novel therapeutic targets</li>
                            <li>Advance precision medicine</li>
                        </ul>
                    </div>
                    <div class="box">
                        <h4>Clinical Impact</h4>
                        <ul>
                            <li>Personalized vitamin D recommendations</li>
                            <li>Improved T2D risk prediction</li>
                            <li>Targeted interventions</li>
                            <li>Reduce health disparities</li>
                        </ul>
                    </div>
                </div>
                
                <div class="key-finding">
                    <strong>Innovation:</strong> First study to integrate genomics, proteomics, and metabolomics to comprehensively characterize vitamin D-T2D mechanisms in African ancestry males.
                </div>
            </div>
            <div class="slide-number">7</div>
        </div>

        <!-- Slide 8: Section - Hypothesis -->
        <div class="slide section-slide">
            <h2>Research Hypothesis</h2>
            <div class="slide-number">8</div>
        </div>

        <!-- Slide 9: Central Hypothesis -->
        <div class="slide">
            <h2>Central Hypothesis</h2>
            <div class="content">
                <div class="highlight" style="font-size: 1.3em; padding: 30px;">
                    <strong>Genetic variants in vitamin D metabolism and signaling pathways exhibit ancestry-specific effects on T2D risk in African ancestry males, mediated through distinct proteomic and metabolomic signatures that differ from European ancestry populations.</strong>
                </div>
                
                <h3>Sub-Hypotheses</h3>
                <ol style="font-size: 1.15em;">
                    <li><strong>Genomic Level:</strong> SNPs in VDR, CYP2R1, CYP27B1, GC, and CYP24A1 demonstrate population-specific allele frequencies and effect sizes on T2D risk</li>
                    
                    <li><strong>Proteomic Level:</strong> VDBP isoforms and VDR expression patterns differ between African ancestry males with and without T2D, independent of serum 25(OH)D levels</li>
                    
                    <li><strong>Metabolomic Level:</strong> Vitamin D supplementation induces distinct metabolic signatures in glucose metabolism and inflammatory pathways</li>
                    
                    <li><strong>Integrative:</strong> Ancestry-specific genetic variants modulate proteomic responses, which regulate metabolomic pathways critical for glucose homeostasis</li>
                </ol>
            </div>
            <div class="slide-number">9</div>
        </div>

        <!-- Slide 10: Section - Specific Aims -->
        <div class="slide section-slide">
            <h2>Specific Aims</h2>
            <div class="slide-number">10</div>
        </div>

        <!-- Slide 11: Aim 1 -->
        <div class="slide">
            <h2>Aim 1: Genomic Analysis</h2>
            <div class="content">
                <h3>Objective</h3>
                <p style="font-size: 1.2em;">Identify ancestry-specific genetic variants in vitamin D pathways associated with T2D risk</p>
                
                <div class="two-column" style="margin-top: 30px;">
                    <div>
                        <h4 style="color: #667eea;">Candidate Genes</h4>
                        <ul>
                            <li><strong>VDR</strong> - Vitamin D receptor</li>
                            <li><strong>GC</strong> - Vitamin D binding protein</li>
                            <li><strong>CYP2R1</strong> - 25-hydroxylase</li>
                            <li><strong>CYP27B1</strong> - 1α-hydroxylase</li>
                            <li><strong>CYP24A1</strong> - 24-hydroxylase</li>
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #667eea;">Datasets</h4>
                        <ul>
                            <li>ARIC (n=4,266 African Americans)</li>
                            <li>Jackson Heart Study (n=3,000+)</li>
                            <li>UK Biobank African subset (n=8,000+)</li>
                            <li>1000 Genomes (reference)</li>
                        </ul>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Analytical Approach</h3>
                <ul>
                    <li>GWAS with ancestry-specific imputation (TOPMed panel)</li>
                    <li>Candidate gene deep sequencing</li>
                    <li>Functional annotation (eQTL, chromatin accessibility)</li>
                    <li>Polygenic risk score development</li>
                </ul>
                
                <div class="key-finding">
                    <strong>Expected Outcome:</strong> 5-10 genome-wide significant loci, including African ancestry-specific variants
                </div>
            </div>
            <div class="slide-number">11</div>
        </div>

        <!-- Slide 12: Aim 2 -->
        <div class="slide">
            <h2>Aim 2: Proteomic Analysis</h2>
            <div class="content">
                <h3>Objective</h3>
                <p style="font-size: 1.2em;">Characterize proteomic signatures of vitamin D signaling in T2D among African ancestry males</p>
                
                <div class="two-column" style="margin-top: 30px;">
                    <div>
                        <h4 style="color: #667eea;">Key Proteins</h4>
                        <ul>
                            <li>VDBP (GC) and isoforms</li>
                            <li>VDR and co-regulators</li>
                            <li>CYP enzymes</li>
                            <li>Insulin signaling proteins</li>
                            <li>Inflammatory markers</li>
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #667eea;">Methods</h4>
                        <ul>
                            <li>LC-MS/MS proteomics</li>
                            <li>TMT-based quantification</li>
                            <li>Targeted validation (SRM)</li>
                            <li>Pathway enrichment</li>
                            <li>pQTL mapping</li>
                        </ul>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Innovation: Bioavailable Vitamin D</h3>
                <div class="highlight">
                    Calculate free and bioavailable 25(OH)D using total 25(OH)D, VDBP, and albumin measurements - accounting for Gc1f polymorphism prevalent in African ancestry
                </div>
                
                <div class="key-finding">
                    <strong>Expected Outcome:</strong> 50-100 differentially expressed proteins, characterization of VDBP isoform effects
                </div>
            </div>
            <div class="slide-number">12</div>
        </div>

        <!-- Slide 13: Aim 3 -->
        <div class="slide">
            <h2>Aim 3: Metabolomic Analysis</h2>
            <div class="content">
                <h3>Objective</h3>
                <p style="font-size: 1.2em;">Define metabolomic responses to vitamin D intervention and association with T2D outcomes</p>
                
                <h3>Key Metabolic Pathways</h3>
                <div class="methodology-grid">
                    <div class="method-card">
                        <h4>Glucose Metabolism</h4>
                        <p>Glycolysis, gluconeogenesis, TCA cycle</p>
                    </div>
                    <div class="method-card">
                        <h4>Amino Acids</h4>
                        <p>BCAAs (leucine, isoleucine, valine)</p>
                    </div>
                    <div class="method-card">
                        <h4>Lipid Metabolism</h4>
                        <p>Fatty acid oxidation, bile acids</p>
                    </div>
                </div>
                
                <h3>Analysis Strategy</h3>
                <div class="two-column">
                    <div>
                        <h4 style="color: #667eea;">Cross-Sectional</h4>
                        <ul>
                            <li>T2D cases vs. controls</li>
                            <li>Stratified by vitamin D status</li>
                            <li>Untargeted metabolomics</li>
                            <li>Pathway enrichment</li>
                        </ul>
                    </div>
                    <div>
                        <h4 style="color: #667eea;">Intervention</h4>
                        <ul>
                            <li>Pre/post supplementation</li>
                            <li>Responder analysis</li>
                            <li>Dose-response relationships</li>
                            <li>Predictive modeling</li>
                        </ul>
                    </div>
                </div>
                
                <div class="key-finding">
                    <strong>Expected Outcome:</strong> 20-50 metabolites associated with T2D and modulated by vitamin D; predictive biomarker panel
                </div>
            </div>
            <div class="slide-number">13</div>
        </div>

        <!-- Slide 14: Aim 4 -->
        <div class="slide">
            <h2>Aim 4: Multi-Omics Integration</h2>
            <div class="content">
                <h3>Objective</h3>
                <p style="font-size: 1.2em;">Develop integrative multi-omics model of vitamin D-T2D mechanisms</p>
                
                <h3>Integration Approaches</h3>
                <ul style="font-size: 1.15em;">
                    <li><strong>Correlation Networks:</strong> Cross-omics relationships (pQTL, mQTL)</li>
                    <li><strong>Multi-Omics Factor Analysis (MOFA):</strong> Identify latent factors</li>
                    <li><strong>Network Biology:</strong> Multi-layer networks connecting all omics</li>
                    <li><strong>Causal Inference:</strong> Mendelian randomization for causality</li>
                    <li><strong>Machine Learning:</strong> Predictive models integrating all layers</li>
                </ul>
                
                <h3 style="margin-top: 30px;">Ancestry-Specific Analysis</h3>
                <div class="highlight">
                    Compare integrated networks between African and European ancestry to identify population-specific regulatory modules and quantify genetic vs. environmental contributions
                </div>
                
                <div class="key-finding">
                    <strong>Expected Outcome:</strong> Comprehensive network model, identification of druggable targets, prioritized hypotheses for validation
                </div>
            </div>
            <div class="slide-number">14</div>
        </div>

        <!-- Slide 15: Section - Methodology -->
        <div class="slide section-slide">
            <h2>Methodology & Preliminary Results</h2>
            <div class="slide-number">15</div>
        </div>

        <!-- Slide 16: Computational Pipeline -->
        <div class="slide">
            <h2>Computational Analysis Pipeline</h2>
            <div class="content">
                <div class="methodology-grid">
                    <div class="method-card">
                        <h4>Genomics</h4>
                        <ul style="font-size: 0.9em;">
                            <li>PLINK 2.0</li>
                            <li>BOLT-LMM</li>
                            <li>ANNOVAR/VEP</li>
                            <li>GTEx eQTL</li>
                        </ul>
                    </div>
                    <div class="method-card">
                        <h4>Proteomics</h4>
                        <ul style="font-size: 0.9em;">
                            <li>MaxQuant</li>
                            <li>Limma/DEqMS</li>
                            <li>STRING</li>
                            <li>Cytoscape</li>
                        </ul>
                    </div>
                    <div class="method-card">
                        <h4>Metabolomics</h4>
                        <ul style="font-size: 0.9em;">
                            <li>XCMS/MZmine</li>
                            <li>MetaboAnalyst</li>
                            <li>KEGG/HMDB</li>
                            <li>Machine learning</li>
                        </ul>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Integration Tools</h3>
                <ul>
                    <li><strong>MOFA2:</strong> Multi-omics factor analysis</li>
                    <li><strong>mixOmics:</strong> Data integration and visualization</li>
                    <li><strong>TwoSampleMR:</strong> Mendelian randomization</li>
                    <li><strong>NetworkX:</strong> Network analysis and visualization</li>
                    <li><strong>PyTorch:</strong> Deep learning for predictive modeling</li>
                </ul>
                
                <div class="highlight">
                    <strong>Reproducibility:</strong> All code version-controlled (GitHub), containerized (Docker), with computational notebooks (Jupyter/R Markdown)
                </div>
            </div>
            <div class="slide-number">16</div>
        </div>

        <!-- Slide 17: Preliminary Results -->
        <div class="slide">
            <h2>Preliminary Results: Genomic Analysis</h2>
            <div class="content">
                <div class="stats-grid">
                    <div class="stat-box">
                        <div class="stat-number">250</div>
                        <div class="stat-label">Variants Analyzed</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">500</div>
                        <div class="stat-label">Samples (200 cases)</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">8</div>
                        <div class="stat-label">Significant Variants</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">5</div>
                        <div class="stat-label">Genes Studied</div>
                    </div>
                </div>
                
                <h3>Top Findings</h3>
                <table>
                    <tr>
                        <th>Gene</th>
                        <th>Significant Variants</th>
                        <th>Min P-value</th>
                        <th>Key Finding</th>
                    </tr>
                    <tr>
                        <td><strong>VDR</strong></td>
                        <td>3</td>
                        <td>0.0025</td>
                        <td>Strongest associations detected</td>
                    </tr>
                    <tr>
                        <td><strong>CYP2R1</strong></td>
                        <td>2</td>
                        <td>0.0324</td>
                        <td>One true causal variant identified</td>
                    </tr>
                    <tr>
                        <td><strong>CYP24A1</strong></td>
                        <td>1</td>
                        <td>0.0070</td>
                        <td>Protective effect (OR=0.74)</td>
                    </tr>
                </table>
                
                <div class="key-finding">
                    <strong>Key Insight:</strong> VDR variants show strongest associations, consistent with central role in vitamin D signaling. Effect sizes (OR 0.7-1.4) consistent with polygenic architecture.
                </div>
            </div>
            <div class="slide-number">17</div>
        </div>

        <!-- Slide 18: Visualizations -->
        <div class="slide">
            <h2>Preliminary Results: Visualizations</h2>
            <div class="content">
                <div class="image-container">
                    <img src="../genomics_analysis/results/figures/manhattan_plot.png" alt="Manhattan Plot" style="max-height: 400px;">
                    <p class="caption">Manhattan plot showing association of vitamin D pathway variants with T2D risk across all five genes</p>
                </div>
                
                <div class="two-column" style="margin-top: 20px;">
                    <div class="box">
                        <h4>Key Observations</h4>
                        <ul style="font-size: 0.95em;">
                            <li>VDR shows strongest signal</li>
                            <li>Multiple genes contribute</li>
                            <li>Modest effect sizes</li>
                            <li>Polygenic architecture</li>
                        </ul>
                    </div>
                    <div class="box">
                        <h4>Next Steps</h4>
                        <ul style="font-size: 0.95em;">
                            <li>Validate in ARIC cohort</li>
                            <li>Functional annotation</li>
                            <li>eQTL analysis</li>
                            <li>Integrate with proteomics</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="slide-number">18</div>
        </div>

        <!-- Slide 19: Section - Expected Outcomes -->
        <div class="slide section-slide">
            <h2>Expected Outcomes & Impact</h2>
            <div class="slide-number">19</div>
        </div>

        <!-- Slide 20: Scientific Outcomes -->
        <div class="slide">
            <h2>Expected Scientific Outcomes</h2>
            <div class="content">
                <div class="methodology-grid">
                    <div class="method-card">
                        <h4>Genomic Discoveries</h4>
                        <ul style="font-size: 0.9em;">
                            <li>5-10 genome-wide significant loci</li>
                            <li>Ancestry-specific variants</li>
                            <li>Functional annotations</li>
                            <li>Polygenic risk scores</li>
                        </ul>
                    </div>
                    <div class="method-card">
                        <h4>Proteomic Insights</h4>
                        <ul style="font-size: 0.9em;">
                            <li>50-100 differential proteins</li>
                            <li>VDBP isoform effects</li>
                            <li>Pathway characterization</li>
                            <li>Bioavailable vitamin D</li>
                        </ul>
                    </div>
                    <div class="method-card">
                        <h4>Metabolomic Biomarkers</h4>
                        <ul style="font-size: 0.9em;">
                            <li>20-50 key metabolites</li>
                            <li>Predictive panels</li>
                            <li>Response biomarkers</li>
                            <li>Pathway signatures</li>
                        </ul>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Integrated Model</h3>
                <div class="highlight">
                    Comprehensive multi-omics network model connecting genetic variants → proteomic changes → metabolomic shifts → T2D phenotypes, with ancestry-specific regulatory modules identified
                </div>
                
                <h3>Publications</h3>
                <ul>
                    <li><strong>4-5 peer-reviewed papers</strong> in high-impact journals</li>
                    <li>Data deposition in public repositories (GEO, PRIDE, Metabolomics Workbench)</li>
                    <li>Open-source analysis pipelines (GitHub)</li>
                    <li>Interactive web portal for data exploration</li>
                </ul>
            </div>
            <div class="slide-number">20</div>
        </div>

        <!-- Slide 21: Clinical Impact -->
        <div class="slide">
            <h2>Clinical & Translational Impact</h2>
            <div class="content">
                <div class="two-column">
                    <div class="box">
                        <h3>Precision Medicine</h3>
                        <ul>
                            <li><strong>Genetic screening:</strong> Identify high-risk individuals</li>
                            <li><strong>Biomarker panels:</strong> Predict supplementation response</li>
                            <li><strong>Personalized dosing:</strong> Ancestry-specific recommendations</li>
                            <li><strong>Risk stratification:</strong> Improved T2D prediction</li>
                        </ul>
                    </div>
                    <div class="box">
                        <h3>Drug Development</h3>
                        <ul>
                            <li><strong>Novel targets:</strong> Proteins and pathways identified</li>
                            <li><strong>Repurposing:</strong> Existing drugs for new indications</li>
                            <li><strong>Combination therapy:</strong> Vitamin D + other agents</li>
                            <li><strong>Pharmacogenomics:</strong> Genotype-guided treatment</li>
                        </ul>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Public Health Impact</h3>
                <div class="stats-grid">
                    <div class="stat-box">
                        <div class="stat-number">4.8M</div>
                        <div class="stat-label">African Americans with T2D</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">10-20%</div>
                        <div class="stat-label">Potential risk reduction</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">$20/year</div>
                        <div class="stat-label">Cost of vitamin D</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">480K</div>
                        <div class="stat-label">Cases potentially prevented</div>
                    </div>
                </div>
                
                <div class="key-finding">
                    <strong>Health Equity:</strong> Targeted interventions for African ancestry populations could significantly reduce T2D disparities
                </div>
            </div>
            <div class="slide-number">21</div>
        </div>

        <!-- Slide 22: Timeline -->
        <div class="slide">
            <h2>Timeline & Milestones</h2>
            <div class="content">
                <table>
                    <tr>
                        <th>Timeline</th>
                        <th>Tasks</th>
                        <th>Milestones</th>
                    </tr>
                    <tr>
                        <td><strong>Year 1<br>Months 1-12</strong></td>
                        <td>
                            • Data acquisition<br>
                            • Genomic analysis (Aim 1)<br>
                            • Functional annotation
                        </td>
                        <td>
                            ✓ All datasets acquired<br>
                            ✓ GWAS completed<br>
                            • Manuscript 1 drafted
                        </td>
                    </tr>
                    <tr>
                        <td><strong>Year 2<br>Months 13-24</strong></td>
                        <td>
                            • Proteomic analysis (Aim 2)<br>
                            • Metabolomic analysis (Aim 3)<br>
                            • Pathway enrichment
                        </td>
                        <td>
                            • Proteomic signatures<br>
                            • Metabolomic biomarkers<br>
                            • Manuscripts 2-3 drafted
                        </td>
                    </tr>
                    <tr>
                        <td><strong>Year 3<br>Months 25-36</strong></td>
                        <td>
                            • Multi-omics integration (Aim 4)<br>
                            • Validation analyses<br>
                            • Dissertation writing
                        </td>
                        <td>
                            • Integrated model complete<br>
                            • All manuscripts submitted<br>
                            • <strong>Dissertation defense</strong>
                        </td>
                    </tr>
                </table>
                
                <h3 style="margin-top: 30px;">Current Status</h3>
                <div class="highlight">
                    <strong>Completed:</strong> Literature review, dataset identification, research templates, aims paper, preliminary genomic analysis<br>
                    <strong>In Progress:</strong> Proteomic and metabolomic analyses<br>
                    <strong>Next:</strong> Multi-omics integration and validation
                </div>
            </div>
            <div class="slide-number">22</div>
        </div>

        <!-- Slide 23: Challenges & Solutions -->
        <div class="slide">
            <h2>Potential Challenges & Mitigation Strategies</h2>
            <div class="content">
                <table>
                    <tr>
                        <th>Challenge</th>
                        <th>Mitigation Strategy</th>
                    </tr>
                    <tr>
                        <td><strong>Data heterogeneity</strong><br>Batch effects across cohorts</td>
                        <td>• Rigorous QC protocols<br>• Batch correction (ComBat, Harmony)<br>• Sensitivity analyses</td>
                    </tr>
                    <tr>
                        <td><strong>Sample size limitations</strong><br>Multi-omics on same individuals</td>
                        <td>• Two-sample MR approaches<br>• Leverage summary statistics<br>• Focus on effect sizes</td>
                    </tr>
                    <tr>
                        <td><strong>Causal inference</strong><br>Confounding, reverse causation</td>
                        <td>• Mendelian randomization<br>• Intervention data integration<br>• Triangulation of evidence</td>
                    </tr>
                    <tr>
                        <td><strong>Computational demands</strong><br>Resource-intensive analyses</td>
                        <td>• HPC and cloud computing<br>• Code optimization<br>• Collaboration with cores</td>
                    </tr>
                    <tr>
                        <td><strong>Biological complexity</strong><br>Multiple confounding factors</td>
                        <td>• Stratified analyses<br>• Pathway-level approaches<br>• Clinical expert collaboration</td>
                    </tr>
                </table>
            </div>
            <div class="slide-number">23</div>
        </div>

        <!-- Slide 24: Broader Impact -->
        <div class="slide">
            <h2>Broader Impact & Future Directions</h2>
            <div class="content">
                <h3>Immediate Impact</h3>
                <ul style="font-size: 1.15em;">
                    <li><strong>Scientific knowledge:</strong> Resolve vitamin D paradox, understand ancestry-specific mechanisms</li>
                    <li><strong>Clinical guidelines:</strong> Inform vitamin D recommendations for African ancestry populations</li>
                    <li><strong>Health equity:</strong> Address critical gap in T2D research and reduce disparities</li>
                    <li><strong>Methodological advances:</strong> Multi-omics integration framework applicable to other diseases</li>
                </ul>
                
                <h3 style="margin-top: 30px;">Future Directions</h3>
                <div class="two-column">
                    <div class="box">
                        <h4>Research Extensions</h4>
                        <ul style="font-size: 0.95em;">
                            <li>Expand to other populations</li>
                            <li>Include female participants</li>
                            <li>Investigate other micronutrients</li>
                            <li>Longitudinal studies</li>
                        </ul>
                    </div>
                    <div class="box">
                        <h4>Clinical Translation</h4>
                        <ul style="font-size: 0.95em;">
                            <li>Randomized controlled trials</li>
                            <li>Implementation science</li>
                            <li>Clinical decision support tools</li>
                            <li>Community engagement</li>
                        </ul>
                    </div>
                </div>
                
                <div class="key-finding">
                    <strong>Long-term Vision:</strong> Establish precision medicine framework for vitamin D and T2D that can be adapted for other complex diseases and diverse populations
                </div>
            </div>
            <div class="slide-number">24</div>
        </div>

        <!-- Slide 25: Acknowledgments -->
        <div class="slide">
            <h2>Acknowledgments</h2>
            <div class="content">
                <h3>Research Team</h3>
                <ul style="font-size: 1.15em;">
                    <li><strong>Advisor:</strong> [Advisor Name] - Guidance and mentorship</li>
                    <li><strong>Committee Members:</strong> [Names] - Scientific input and support</li>
                    <li><strong>Collaborators:</strong> Proteomics, metabolomics, and bioinformatics cores</li>
                </ul>
                
                <h3 style="margin-top: 30px;">Funding & Resources</h3>
                <ul style="font-size: 1.15em;">
                    <li>NIH/NIDDK (pending)</li>
                    <li>Institutional training grant</li>
                    <li>Computational resources: HPC cluster, cloud computing</li>
                    <li>Data access: dbGaP, UK Biobank, public repositories</li>
                </ul>
                
                <h3 style="margin-top: 30px;">Study Participants</h3>
                <div class="highlight">
                    Special thanks to all participants in ARIC, Jackson Heart Study, UK Biobank, and other cohorts whose contributions make this research possible
                </div>
            </div>
            <div class="slide-number">25</div>
        </div>

        <!-- Slide 26: Summary -->
        <div class="slide">
            <h2>Summary & Key Takeaways</h2>
            <div class="content">
                <div class="methodology-grid">
                    <div class="method-card" style="border-top-color: #E41A1C;">
                        <h4>The Problem</h4>
                        <p>African ancestry populations have 60-100% higher T2D prevalence, yet vitamin D mechanisms are understudied</p>
                    </div>
                    <div class="method-card" style="border-top-color: #377EB8;">
                        <h4>The Approach</h4>
                        <p>Hierarchical multi-omics investigation: genomics → proteomics → metabolomics → integration</p>
                    </div>
                    <div class="method-card" style="border-top-color: #4DAF4A;">
                        <h4>The Innovation</h4>
                        <p>First comprehensive study of vitamin D-T2D mechanisms specifically in African ancestry males</p>
                    </div>
                </div>
                
                <h3 style="margin-top: 30px;">Key Contributions</h3>
                <ol style="font-size: 1.2em; line-height: 2;">
                    <li>Identify <strong>ancestry-specific genetic variants</strong> in vitamin D pathways</li>
                    <li>Characterize <strong>proteomic and metabolomic signatures</strong> of vitamin D-T2D associations</li>
                    <li>Develop <strong>integrated multi-omics model</strong> of disease mechanisms</li>
                    <li>Provide <strong>actionable biomarkers</strong> for precision medicine</li>
                    <li>Advance <strong>health equity</strong> through population-specific research</li>
                </ol>
                
                <div class="key-finding" style="margin-top: 30px; font-size: 1.2em;">
                    <strong>Impact:</strong> This research will advance our understanding of vitamin D-T2D mechanisms in African ancestry populations and provide a foundation for personalized interventions to reduce health disparities.
                </div>
            </div>
            <div class="slide-number">26</div>
        </div>

        <!-- Slide 27: Questions -->
        <div class="slide title-slide">
            <h1>Questions & Discussion</h1>
            <p class="subtitle">Thank you for your attention</p>
            <div class="author-info" style="margin-top: 80px;">
                <p><strong>Contact:</strong></p>
                <p>[Your Email]</p>
                <p>[Your Institution]</p>
                <p style="margin-top: 30px;"><strong>Resources:</strong></p>
                <p>All materials available at: /home/ubuntu/thesis_presentation/</p>
            </div>
            <div class="slide-number">27</div>
        </div>

    </div>
</body>
</html>
"""

# Write HTML file
with open('/home/ubuntu/thesis_presentation/presentation.html', 'w') as f:
    f.write(html_content)

print("✓ Thesis presentation created successfully!")
print(f"  Location: /home/ubuntu/thesis_presentation/presentation.html")
print(f"  Total slides: 27")
print(f"  Format: HTML (can be opened in browser or converted to PDF)")
print()
print("Presentation sections:")
print("  1. Title & Overview (slides 1-2)")
print("  2. Background & Significance (slides 3-7)")
print("  3. Research Hypothesis (slides 8-9)")
print("  4. Specific Aims (slides 10-14)")
print("  5. Methodology & Results (slides 15-18)")
print("  6. Expected Outcomes (slides 19-21)")
print("  7. Timeline & Challenges (slides 22-23)")
print("  8. Impact & Summary (slides 24-26)")
print("  9. Questions (slide 27)")

