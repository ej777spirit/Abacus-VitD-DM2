# Genomics Analysis: Vitamin D Pathway Genes and T2D in African Ancestry

## Overview
This directory contains the genomic analysis workflow for identifying genetic variants in vitamin D pathway genes associated with Type 2 Diabetes risk in African ancestry populations.

## Objective
Identify ancestry-specific genetic variants in key vitamin D metabolism and signaling genes (*VDR*, *GC*, *CYP2R1*, *CYP27B1*, *CYP24A1*) that are associated with T2D risk.

## Data Sources
- **1000 Genomes Project Phase 3** - African populations (YRI, LWK, GWD, MSL, ESN, ASW, ACB)
- **GWAS Catalog** - Known vitamin D and T2D associations
- **GTEx** - eQTL data for functional annotation

## Analysis Pipeline

### Step 1: Data Acquisition
Download 1000 Genomes Phase 3 data for African populations and extract vitamin D pathway gene regions.

### Step 2: Quality Control
- Variant call rate > 95%
- Minor allele frequency (MAF) > 0.01
- Hardy-Weinberg equilibrium p-value > 1×10⁻⁶

### Step 3: Candidate Gene Analysis
Focus on five key genes with known roles in vitamin D metabolism:
- **VDR** (Vitamin D Receptor) - chr12
- **GC** (Vitamin D Binding Protein) - chr4
- **CYP2R1** (25-hydroxylase) - chr11
- **CYP27B1** (1α-hydroxylase) - chr12
- **CYP24A1** (24-hydroxylase) - chr20

### Step 4: Association Testing
Simulate T2D case-control status and test for genetic associations using logistic regression.

### Step 5: Functional Annotation
Annotate significant variants with:
- Gene location (exonic, intronic, regulatory)
- Predicted functional impact
- eQTL effects from GTEx

## Directory Structure
```
genomics_analysis/
├── README.md (this file)
├── scripts/
│   ├── 01_download_data.sh
│   ├── 02_extract_genes.R
│   ├── 03_qc_analysis.R
│   ├── 04_association_analysis.R
│   └── 05_functional_annotation.R
├── data/
│   ├── raw/ (downloaded VCF files)
│   ├── processed/ (QC-filtered data)
│   └── annotations/ (functional annotations)
├── results/
│   ├── tables/ (association results)
│   ├── figures/ (Manhattan plots, regional plots)
│   └── reports/ (summary reports)
└── logs/ (analysis logs)
```

## Expected Outputs
1. **Association Results Table** - Variants with p-values, effect sizes, allele frequencies
2. **Manhattan Plot** - Genome-wide view of associations
3. **Regional Association Plots** - Detailed views of candidate gene regions
4. **Functional Annotation Summary** - Predicted effects of significant variants
5. **Allele Frequency Comparison** - African vs. European ancestry differences

## Software Requirements
- R (≥4.0) with packages: `vcfR`, `genetics`, `qqman`, `data.table`
- PLINK 1.9 or 2.0
- VCFtools
- BCFtools

## Timeline
- Week 1: Data download and setup
- Week 2: QC and preprocessing
- Week 3: Association analysis
- Week 4: Functional annotation and visualization

## Notes
- This is a demonstration analysis using publicly available data
- For actual research, dbGaP-approved datasets (ARIC, Jackson Heart Study) would be used
- T2D phenotypes are simulated for demonstration purposes
