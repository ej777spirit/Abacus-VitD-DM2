# Computational Experiments Plan
## Vitamin D and Type 2 Diabetes in African Ancestry Males

**Date:** October 1, 2025  
**Status:** Ready for Execution

---

## Overview

This document outlines the computational experiments to be performed using the identified publicly available omics datasets. The experiments are organized hierarchically following the multi-omics approach: Genomics → Proteomics → Metabolomics → Integration.

---

## Experiment 1: Genomic Analysis - GWAS and Candidate Gene Analysis

### Objective
Identify genetic variants in vitamin D pathway genes associated with T2D risk in African ancestry populations.

### Datasets
- **Primary:** ARIC (dbGaP phs000280) - African American subset
- **Validation:** Jackson Heart Study (dbGaP phs000286)
- **Reference:** 1000 Genomes Project Phase 3 (African populations)

### Analysis Steps

#### Step 1.1: Data Acquisition and Preparation
```bash
# Download ARIC genotype data (requires dbGaP access)
# For demonstration, we'll use 1000 Genomes African populations as proxy

# Download 1000 Genomes Phase 3 data for African populations
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr*.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz

# Extract African populations (YRI, LWK, GWD, MSL, ESN, ASW, ACB)
# Extract vitamin D pathway genes regions
```

#### Step 1.2: Quality Control
- Call rate > 95%
- MAF > 0.01 in African ancestry samples
- HWE p-value > 1×10⁻⁶
- Remove related individuals (PI_HAT > 0.125)

#### Step 1.3: Candidate Gene Extraction
Focus on key vitamin D pathway genes:
- **VDR** (chr12: 48,235,319-48,298,814)
- **GC** (chr4: 72,607,424-72,669,374)
- **CYP2R1** (chr11: 14,897,487-14,920,590)
- **CYP27B1** (chr12: 57,761,854-57,768,777)
- **CYP24A1** (chr20: 54,148,065-54,174,962)

#### Step 1.4: Association Analysis
```r
# Logistic regression for T2D case-control
# Model: T2D ~ SNP + Age + BMI + PC1-10
# Test for:
# - Additive effects
# - Dominant/recessive models
# - Gene-gene interactions
# - Gene-environment interactions (BMI, age)
```

#### Step 1.5: Functional Annotation
- eQTL lookup in GTEx (pancreas, adipose, muscle, liver)
- RegulomeDB scores
- CADD scores for deleteriousness
- Chromatin state annotations (Roadmap Epigenomics)

### Expected Outputs
- Manhattan plot of association results
- QQ plot for genomic inflation assessment
- Regional association plots for candidate genes
- Table of significant variants (p < 5×10⁻⁸ or p < 0.05 for candidate genes)
- Functional annotation summary

---

## Experiment 2: Proteomic Analysis - Differential Expression and Pathway Analysis

### Objective
Identify proteins differentially expressed between T2D cases and controls, and characterize vitamin D-responsive protein signatures.

### Datasets
- **Primary:** PRIDE PXD015234 (African American T2D proteomics)
- **Reference:** Human Protein Atlas
- **Pathway databases:** KEGG, Reactome, STRING

### Analysis Steps

#### Step 2.1: Data Acquisition
```bash
# Download from PRIDE Archive
# PXD015234: Plasma proteomics of African Americans with T2D
wget ftp://ftp.pride.ebi.ac.uk/pride/data/archive/2020/01/PXD015234/*
```

#### Step 2.2: Protein Identification and Quantification
- Process raw MS data (if available) using MaxQuant or Proteome Discoverer
- Alternatively, use provided protein abundance matrix
- Filter: ≥2 unique peptides per protein
- Normalization: Median normalization or TMM

#### Step 2.3: Differential Expression Analysis
```r
# Compare T2D cases vs. controls
# Statistical test: Limma or DEqMS
# Covariates: Age, BMI, batch
# Significance: FDR < 0.05, |log2FC| > 0.5
```

#### Step 2.4: Vitamin D Pathway Focus
Specifically examine:
- **VDBP (GC):** Vitamin D binding protein
- **VDR:** Vitamin D receptor
- **CYP2R1, CYP27B1, CYP24A1:** Vitamin D metabolizing enzymes
- **Downstream targets:** Insulin signaling (IRS1, IRS2, AKT1/2), inflammatory markers (CRP, IL6)

#### Step 2.5: Pathway Enrichment Analysis
- Gene Ontology (GO) enrichment
- KEGG pathway enrichment
- Reactome pathway enrichment
- Protein-protein interaction network (STRING)

#### Step 2.6: Correlation with Clinical Parameters
- Correlate protein levels with:
  - HbA1c
  - Fasting glucose
  - Insulin levels
  - 25(OH)D levels (if available)

### Expected Outputs
- Volcano plot of differential expression
- Heatmap of top differentially expressed proteins
- Pathway enrichment bar plots
- Protein-protein interaction network
- Correlation matrix with clinical parameters

---

## Experiment 3: Metabolomic Analysis - Metabolic Signatures and Biomarker Discovery

### Objective
Identify metabolites associated with T2D and vitamin D status, and discover predictive biomarkers.

### Datasets
- **Primary:** Metabolomics Workbench ST001386 (Vitamin D supplementation)
- **Secondary:** Metabolomics Workbench ST002073 (T2D metabolomics)
- **Reference:** HMDB, KEGG for metabolite annotation

### Analysis Steps

#### Step 3.1: Data Acquisition
```bash
# Download from Metabolomics Workbench
wget https://www.metabolomicsworkbench.org/data/DRCCMetadata.php?Mode=Study&StudyID=ST001386
wget https://www.metabolomicsworkbench.org/data/DRCCMetadata.php?Mode=Study&StudyID=ST002073
```

#### Step 3.2: Data Preprocessing
- Missing value imputation (KNN or half-minimum)
- Normalization (probabilistic quotient normalization)
- Log transformation
- Batch effect correction (if needed)

#### Step 3.3: Univariate Analysis
```r
# T2D cases vs. controls
# Statistical tests:
# - t-test or Mann-Whitney U (for non-normal distributions)
# - FDR correction (Benjamini-Hochberg)
# Significance: FDR < 0.05, |log2FC| > 0.5
```

#### Step 3.4: Multivariate Analysis
- **PCA:** Overall metabolic profile differences
- **PLS-DA:** Supervised classification
- **Random Forest:** Feature importance ranking
- **Cross-validation:** 10-fold CV for model validation

#### Step 3.5: Pathway Analysis
Focus on key metabolic pathways:
- Glycolysis/gluconeogenesis
- TCA cycle
- Amino acid metabolism (especially BCAAs: leucine, isoleucine, valine)
- Fatty acid metabolism
- Bile acid metabolism
- Inflammatory lipid mediators

#### Step 3.6: Vitamin D Intervention Analysis
If intervention data available:
- Pre/post comparison
- Responder vs. non-responder analysis
- Dose-response relationships

#### Step 3.7: Biomarker Panel Development
```r
# Machine learning for biomarker discovery
# Models: Logistic regression, Random Forest, XGBoost
# Feature selection: LASSO, Boruta
# Performance metrics: AUC-ROC, sensitivity, specificity
# Cross-validation and external validation
```

### Expected Outputs
- PCA score plot showing group separation
- Volcano plot of metabolite changes
- Heatmap of top discriminatory metabolites
- Pathway enrichment results
- ROC curves for biomarker panels
- Feature importance plots

---

## Experiment 4: Multi-Omics Integration

### Objective
Integrate genomics, proteomics, and metabolomics data to construct comprehensive mechanistic models.

### Analysis Steps

#### Step 4.1: Data Harmonization
- Match samples across omics layers (when available)
- Standardize identifiers (genes, proteins, metabolites)
- Create unified data matrix

#### Step 4.2: Correlation Analysis
```r
# Cross-omics correlations
# - Genetic variants ↔ Protein levels (pQTL)
# - Genetic variants ↔ Metabolite levels (mQTL)
# - Protein levels ↔ Metabolite levels
# Visualization: Circos plots, correlation networks
```

#### Step 4.3: Multi-Omics Factor Analysis (MOFA)
```r
# Identify latent factors explaining variation across omics
# Determine which omics layers contribute to each factor
# Associate factors with T2D phenotype
```

#### Step 4.4: Network Construction
- **Multi-layer network:**
  - Layer 1: Genetic variants
  - Layer 2: Proteins
  - Layer 3: Metabolites
  - Layer 4: Phenotypes (T2D, HbA1c, etc.)
- **Network analysis:**
  - Hub identification
  - Module detection (community detection algorithms)
  - Shortest path analysis (genetic variant → phenotype)

#### Step 4.5: Causal Inference - Mendelian Randomization
```r
# Two-sample MR using summary statistics
# Exposure: Genetic variants → 25(OH)D levels
# Outcome: T2D risk
# Methods: IVW, MR-Egger, Weighted median
# Sensitivity: Pleiotropy tests, leave-one-out analysis
```

#### Step 4.6: Pathway Flux Analysis
- Constraint-based modeling of metabolic pathways
- Integrate gene expression (as proxy from eQTL) and metabolite levels
- Predict flux changes in vitamin D-related pathways

#### Step 4.7: Machine Learning Integration
```r
# Multi-omics predictive models
# Input: Genetic variants + Protein levels + Metabolite levels
# Output: T2D risk prediction
# Models: Elastic net, Random Forest, Deep learning (neural networks)
# Feature importance: SHAP values
# Validation: Cross-validation, external cohort
```

### Expected Outputs
- Multi-omics correlation network
- MOFA factor plots showing omics contributions
- Multi-layer network visualization
- Mendelian randomization forest plots
- Pathway flux diagrams
- Predictive model performance metrics (AUC, accuracy, etc.)
- Feature importance rankings across omics layers

---

## Experiment 5: Ancestry-Specific Analysis

### Objective
Compare findings between African and European ancestry populations to identify ancestry-specific mechanisms.

### Analysis Steps

#### Step 5.1: Parallel Analysis in European Ancestry
- Repeat Experiments 1-3 using European ancestry datasets
- UK Biobank European subset
- European proteomics/metabolomics studies

#### Step 5.2: Effect Size Comparison
```r
# Compare:
# - Genetic variant effect sizes (OR for T2D)
# - Protein fold-changes
# - Metabolite fold-changes
# Statistical test: Heterogeneity test (Cochran's Q)
```

#### Step 5.3: Allele Frequency Differences
- Compare MAF of vitamin D pathway variants
- Identify ancestry-specific variants (present in one population, absent in other)

#### Step 5.4: Local Ancestry Inference
- For admixed individuals (e.g., African Americans)
- Determine local ancestry at vitamin D pathway loci
- Test for association between local ancestry and T2D risk

#### Step 5.5: Gene-Environment Interaction
```r
# Test if genetic effects differ by:
# - Ancestry
# - Vitamin D levels
# - BMI
# Statistical model: Logistic regression with interaction terms
```

### Expected Outputs
- Forest plots comparing effect sizes across ancestries
- Allele frequency comparison tables
- Local ancestry plots
- Interaction effect plots

---

## Implementation Timeline

### Week 1-2: Setup and Data Acquisition
- Set up computational environment
- Download all datasets
- Organize directory structure
- Install required software

### Week 3-4: Experiment 1 (Genomics)
- QC and preprocessing
- Association analysis
- Functional annotation
- Generate outputs

### Week 5-6: Experiment 2 (Proteomics)
- Data processing
- Differential expression
- Pathway analysis
- Generate outputs

### Week 7-8: Experiment 3 (Metabolomics)
- Data preprocessing
- Statistical analysis
- Biomarker discovery
- Generate outputs

### Week 9-10: Experiment 4 (Integration)
- Data harmonization
- Multi-omics analysis
- Network construction
- Causal inference

### Week 11-12: Experiment 5 (Ancestry-Specific)
- Comparative analysis
- Synthesis of findings
- Final visualizations

---

## Software and Tools Required

### Genomics
- PLINK 2.0
- R packages: `snpStats`, `GWASTools`, `qqman`, `LDlinkR`
- VCFtools, BCFtools
- ANNOVAR or VEP

### Proteomics
- MaxQuant (if processing raw data)
- R packages: `limma`, `DEqMS`, `MSstats`
- Cytoscape (network visualization)
- STRING database

### Metabolomics
- R packages: `MetaboAnalystR`, `mixOmics`, `caret`
- Python: `scikit-learn`, `xgboost`, `shap`
- XCMS (if processing raw data)

### Integration
- R packages: `MOFA2`, `mixOmics`, `igraph`, `TwoSampleMR`
- Python: `networkx`, `pytorch` (for deep learning)
- Cytoscape (multi-layer networks)

### Visualization
- R: `ggplot2`, `pheatmap`, `ComplexHeatmap`, `circlize`
- Python: `matplotlib`, `seaborn`, `plotly`

---

## Expected Challenges and Solutions

### Challenge 1: Data Access Restrictions
**Solution:** Use publicly available proxy datasets (1000 Genomes, GTEx) for demonstration; apply for dbGaP access for actual analysis.

### Challenge 2: Missing Multi-Omics Data on Same Individuals
**Solution:** Use two-sample approaches (e.g., two-sample MR); leverage summary statistics; focus on pathway-level integration.

### Challenge 3: Computational Resources
**Solution:** Use cloud computing (AWS, Google Cloud); optimize code for efficiency; parallelize where possible.

### Challenge 4: Batch Effects
**Solution:** Rigorous QC; batch effect correction methods (ComBat, Harmony); sensitivity analyses.

---

## Quality Control Checklist

- [ ] All datasets downloaded and verified
- [ ] QC metrics documented for each omics layer
- [ ] Reproducible code with version control (Git)
- [ ] Random seeds set for all stochastic processes
- [ ] Intermediate results saved at each step
- [ ] Visualizations generated for all major findings
- [ ] Statistical assumptions checked (normality, homoscedasticity, etc.)
- [ ] Multiple testing correction applied appropriately
- [ ] Sensitivity analyses performed
- [ ] Results validated in independent datasets when possible

---

## Deliverables

1. **Analysis Scripts:** Well-documented R and Python scripts for all experiments
2. **Results Tables:** CSV/Excel files with all statistical results
3. **Figures:** High-resolution publication-quality figures
4. **Reports:** Markdown/HTML reports for each experiment
5. **Integrated Database:** SQLite or similar for storing all results
6. **Interactive Visualizations:** Shiny apps or Plotly dashboards
7. **Manuscript Drafts:** Results sections for each aim

---

## Next Steps

1. Begin with Experiment 1 (Genomics) using 1000 Genomes data as demonstration
2. Proceed sequentially through experiments
3. Document all findings in real-time
4. Prepare interim reports after each experiment
5. Integrate findings progressively

---

**Status:** Ready to begin execution  
**Estimated Completion:** 12 weeks for all experiments
