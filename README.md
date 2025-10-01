# Vitamin D and Type 2 Diabetes in African Ancestry Males
## A Multi-Omics Research Project

### Project Overview

This repository contains a comprehensive research project investigating the correlation between vitamin D levels and Type 2 Diabetes (T2D) among African Ancestry Males, utilizing a hierarchical multi-omics approach (genomics → proteomics → metabolomics).

**Research Focus**: Understanding genetic and molecular mechanisms linking vitamin D deficiency to T2D risk in populations of African ancestry, addressing the critical health disparity gap in diabetes research.

---

## 📂 Repository Structure

```
Abacus-VitD-DM2/
├── literature/                         # Comprehensive literature review
├── datasets/                           # Curated omics datasets inventory
├── templates/                          # Research frameworks and templates
├── aims_paper/                         # Complete aims paper (NIH format)
├── computational_analysis/             # Analysis plans and code
│   ├── computational_experiments_plan.md
│   └── genomics_analysis/             # R-based genomic analysis pipeline
│       ├── scripts/                   # Analysis scripts
│       ├── results/                   # Output figures, tables, reports
│       └── data/                      # Data directories (raw/processed)
├── presentations/                      # Thesis committee presentation
└── project_summary.md                 # Executive summary
```

---

## 📚 Key Deliverables

### 1. Literature Review
**Location**: `literature/`

Comprehensive review covering:
- Vitamin D metabolism and T2D pathophysiology
- Genetic factors in African ancestry populations
- Current research landscape and gaps
- Mechanistic insights into vitamin D-diabetes relationship

**Files**:
- `literature_review_vitD_T2D_african_ancestry.md` (Markdown)
- `literature_review_vitD_T2D_african_ancestry.pdf` (PDF)

---

### 2. Omics Datasets Inventory
**Location**: `datasets/`

Curated list of publicly available datasets from major repositories:
- **Genomics**: GWAS data, whole genome/exome sequencing (dbGaP, UK Biobank)
- **Proteomics**: Plasma/serum protein profiling (PRIDE, ProteomeXchange)
- **Metabolomics**: Metabolite measurements (MetaboLights, Metabolomics Workbench)

Each dataset includes:
- Accession numbers and URLs
- Sample sizes and ethnic composition
- Relevant phenotypes
- Access procedures

**Files**:
- `omics_datasets_inventory.md` (Markdown)
- `omics_datasets_inventory.pdf` (PDF)

---

### 3. Research Templates & Frameworks
**Location**: `templates/`

Comprehensive templates for:
- Hypothesis development (PICO framework)
- NIH-style aims paper structure
- Experimental design
- Computational analysis workflows
- Multi-omics integration strategies

**Files**:
- `research_templates_and_frameworks.md` (Markdown)
- `research_templates_and_frameworks.pdf` (PDF)

---

### 4. Aims Paper
**Location**: `aims_paper/`

Complete NIH R01-style aims paper including:

**Central Hypothesis**: 
Genetic variants in vitamin D-related genes (VDR, CYP27B1, GC) interact with vitamin D deficiency to increase T2D risk in African ancestry males through disrupted insulin signaling and beta-cell dysfunction.

**Specific Aims**:
1. **Genomic Analysis**: Identify genetic variants and SNP×vitamin D interactions
2. **Proteomic Profiling**: Map differential protein expression patterns
3. **Metabolomic Investigation**: Characterize metabolic dysregulation
4. **Multi-Omics Integration**: Build integrative models

**Files**:
- `aims_paper_vitD_T2D_african_ancestry.md` (Markdown)
- `aims_paper_vitD_T2D_african_ancestry.pdf` (PDF)

---

### 5. Computational Analysis
**Location**: `computational_analysis/`

#### Analysis Plan
`computational_experiments_plan.md` - Detailed protocol for:
- Genomic analysis (GWAS, variant calling, pathway analysis)
- Proteomic analysis (differential expression, network analysis)
- Metabolomic analysis (pathway enrichment, biomarker discovery)
- Multi-omics integration (machine learning, systems biology)

#### Genomics Analysis Pipeline
**Location**: `computational_analysis/genomics_analysis/`

Complete R-based analysis pipeline with:
- **Scripts**: `genomic_analysis_demo.R` - Comprehensive analysis workflow
- **Results**: 
  - Association results and gene summaries (CSV)
  - Visualizations: Manhattan plots, QQ plots, effect size plots, MAF comparisons
  - Detailed analysis report (MD/PDF)
- **Logs**: Analysis execution logs

**Key Features**:
- Simulated GWAS analysis for demonstration
- Publication-ready visualizations
- Statistical summaries and gene-level analysis
- Reproducible workflow

---

### 6. Thesis Presentation
**Location**: `presentations/thesis_presentation/`

27-slide HTML presentation for PhD committee including:
- Research background and significance
- Health disparities context
- Hypothesis and specific aims
- Methodology and approach
- Preliminary results (simulated data)
- Expected outcomes and impact
- Timeline and milestones
- Budget considerations
- Challenges and mitigation strategies

**File**: `presentation.html` (Interactive HTML5 slides)

---

## 🎯 Research Significance

### Health Disparities Context
- African Americans: 12.1% T2D prevalence vs. 7.4% in White Americans
- Higher vitamin D deficiency rates in African ancestry populations
- Critical gap in diabetes research representation

### Scientific Innovation
- **First comprehensive multi-omics study** of vitamin D-T2D in African ancestry males
- Integration of genomics, proteomics, and metabolomics
- Population-specific mechanistic insights
- Potential for personalized intervention strategies

### Clinical Impact
- Risk stratification tools for high-risk populations
- Targeted vitamin D supplementation guidelines
- Novel therapeutic targets
- Reduced health disparities

---

## 🔬 Methodology Highlights

### Hierarchical Multi-Omics Approach
1. **Genomics (Foundation)**: Identify genetic predispositions
2. **Proteomics (Functional Layer)**: Map molecular mechanisms
3. **Metabolomics (Phenotypic Outcomes)**: Characterize metabolic signatures

### Key Analytical Methods
- Genome-wide association studies (GWAS)
- Gene-environment (G×E) interaction analysis
- Differential expression analysis (proteomics/metabolomics)
- Machine learning integration (Random Forest, Neural Networks)
- Pathway and network analysis
- Multi-omic data integration (MOFA+, mixOmics)

---

## 📊 Preliminary Results

The genomics analysis pipeline has been demonstrated with simulated data, producing:
- Manhattan and QQ plots for GWAS results
- Gene-level association summaries
- Effect size visualizations
- Minor allele frequency comparisons
- Statistical tables and reports

*Note: These are demonstration outputs to validate the analytical pipeline. Real data analysis will be conducted using the identified public datasets.*

---

## 🗓️ Project Timeline

- **Months 1-6**: Data acquisition, quality control, genomic analysis
- **Months 7-12**: Proteomic analysis and integration with genomics
- **Months 13-18**: Metabolomic analysis and multi-omics integration
- **Months 19-24**: Model validation, manuscript preparation, dissemination

---

## 🛠️ Technical Requirements

### Software & Tools
- **Genomics**: PLINK, GCTA, EIGENSOFT, ANNOVAR, MAGMA
- **Proteomics**: MaxQuant, Perseus, STRING
- **Metabolomics**: XCMS, MetaboAnalyst, mummichog
- **Integration**: R (mixOmics, MOFA+), Python (scikit-learn, TensorFlow)
- **Visualization**: ggplot2, plotly, Cytoscape

### Computational Resources
- High-performance computing cluster (recommended)
- Minimum: 64GB RAM, 16 cores
- Storage: ~5TB for raw data and results

---

## 📖 How to Use This Repository

1. **Start with Literature Review**: Understand the research landscape
2. **Review Aims Paper**: Grasp the central hypothesis and specific aims
3. **Explore Datasets**: Familiarize yourself with available data sources
4. **Study Computational Plan**: Understand the analytical workflow
5. **Run Analysis Pipeline**: Execute scripts in `computational_analysis/genomics_analysis/`
6. **Review Presentation**: See how findings are communicated

---

## 📧 Contact & Collaboration

For questions, collaborations, or data access inquiries:
- Repository: [ej777spirit/Abacus-VitD-DM2](https://github.com/ej777spirit/Abacus-VitD-DM2)
- Issues: Use GitHub Issues for technical questions

---

## 📄 Citation

If you use this research framework or analysis pipelines, please cite:

```
[Author]. (2025). Vitamin D and Type 2 Diabetes in African Ancestry Males: 
A Multi-Omics Research Project. GitHub repository: 
https://github.com/ej777spirit/Abacus-VitD-DM2
```

---

## 🙏 Acknowledgments

This research framework was developed using Abacus.AI's DeepAgent for comprehensive literature review, dataset curation, analytical pipeline development, and project organization.

---

## 📜 License

This project is shared for academic and research purposes. Please refer to individual dataset licenses for data usage restrictions.

---

## 🔄 Project Status

**Current Phase**: Foundation Complete
- ✅ Literature review completed
- ✅ Datasets identified and documented
- ✅ Research framework established
- ✅ Aims paper written
- ✅ Computational pipeline designed
- ✅ Analysis scripts developed
- ⏳ Data acquisition in progress
- ⏳ Full-scale analysis pending

---

**Last Updated**: October 2025

---

*This repository represents a comprehensive PhD-level research project investigating critical health disparities through innovative multi-omics approaches.*
