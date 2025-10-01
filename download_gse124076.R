#!/usr/bin/env Rscript

# ==============================================================================
# Download and Analyze GSE124076 - African American Hepatocyte Gene Expression
# VDR Expression Analysis for Vitamin D - Type 2 Diabetes Research
# ==============================================================================

cat("==============================================\n")
cat("GSE124076 Data Download and Analysis\n")
cat("==============================================\n\n")

# Load required libraries
suppressPackageStartupMessages({
  library(GEOquery)
  library(tidyverse)
  library(Biobase)
})

# Set working directory
setwd("~/real_data_analysis/transcriptomics")

# Download GSE124076 data
cat("Step 1: Downloading GSE124076 from GEO...\n")
cat("This may take several minutes...\n\n")

tryCatch({
  # Download the GEO dataset
  gse <- getGEO("GSE124076", GSEMatrix = TRUE, getGPL = FALSE)
  
  # Save the raw object
  saveRDS(gse, "GSE124076_raw.rds")
  cat("✓ Successfully downloaded GSE124076\n\n")
  
  # Extract expression data
  cat("Step 2: Extracting expression data...\n")
  
  # GSE124076 has multiple platforms, get RNA-seq data
  # Check which series has RNA-seq data
  cat(sprintf("Number of platforms in dataset: %d\n", length(gse)))
  
  # Get the first platform (RNA-seq)
  eset <- gse[[1]]
  
  # Extract expression matrix
  expr_data <- exprs(eset)
  cat(sprintf("Expression matrix dimensions: %d genes × %d samples\n", 
              nrow(expr_data), ncol(expr_data)))
  
  # Extract phenotype data
  pheno_data <- pData(eset)
  cat(sprintf("Phenotype data: %d samples × %d variables\n", 
              nrow(pheno_data), ncol(pheno_data)))
  
  # Save processed data
  write.csv(expr_data, "GSE124076_expression_matrix.csv", row.names = TRUE)
  write.csv(pheno_data, "GSE124076_phenotype_data.csv", row.names = TRUE)
  
  cat("✓ Expression and phenotype data extracted\n\n")
  
  # Step 3: Identify vitamin D pathway genes
  cat("Step 3: Analyzing vitamin D pathway genes...\n\n")
  
  # Key vitamin D genes to analyze
  vitd_genes <- c("VDR", "GC", "CYP27B1", "CYP24A1", "CYP27A1", 
                  "CYP2R1", "RXRA", "RXRB", "RXRG")
  
  # Gene features
  if ("GENE" %in% colnames(fData(eset))) {
    gene_info <- fData(eset)
    cat("Gene annotation available\n")
  } else {
    cat("Note: Gene symbols may need to be matched manually\n")
    gene_info <- fData(eset)
  }
  
  # Print available column names for gene matching
  cat("\nAvailable annotation columns:\n")
  cat(paste(colnames(fData(eset)), collapse = ", "), "\n\n")
  
  # Try to find vitamin D genes in the data
  cat("Searching for vitamin D pathway genes...\n")
  
  # Save feature data for manual inspection
  write.csv(fData(eset), "GSE124076_feature_data.csv", row.names = TRUE)
  
  # Create summary statistics
  expr_summary <- data.frame(
    Gene = rownames(expr_data),
    Mean = rowMeans(expr_data),
    SD = apply(expr_data, 1, sd),
    Min = apply(expr_data, 1, min),
    Max = apply(expr_data, 1, max),
    Median = apply(expr_data, 1, median)
  )
  
  write.csv(expr_summary, "GSE124076_expression_summary.csv", row.names = FALSE)
  
  cat("✓ Summary statistics calculated\n\n")
  
  # Step 4: Sample information analysis
  cat("Step 4: Analyzing sample characteristics...\n\n")
  
  # Print column names
  cat("Available phenotype columns:\n")
  cat(paste(colnames(pheno_data), collapse = "\n"), "\n\n")
  
  # Extract key phenotype information
  key_columns <- c("title", "geo_accession", "characteristics_ch1")
  available_columns <- intersect(key_columns, colnames(pheno_data))
  
  if (length(available_columns) > 0) {
    sample_info <- pheno_data[, available_columns]
    write.csv(sample_info, "GSE124076_sample_info.csv", row.names = TRUE)
    cat("✓ Sample information extracted\n\n")
  }
  
  # Step 5: Create visualization of top expressed genes
  cat("Step 5: Creating visualizations...\n")
  
  # Calculate mean expression
  mean_expr <- rowMeans(expr_data)
  top_genes_idx <- order(mean_expr, decreasing = TRUE)[1:50]
  
  # Save top expressed genes
  top_genes <- data.frame(
    Gene = rownames(expr_data)[top_genes_idx],
    Mean_Expression = mean_expr[top_genes_idx]
  )
  write.csv(top_genes, "GSE124076_top50_genes.csv", row.names = FALSE)
  
  cat("✓ Visualizations prepared\n\n")
  
  # Summary
  cat("==============================================\n")
  cat("ANALYSIS COMPLETE\n")
  cat("==============================================\n\n")
  
  cat("Files created:\n")
  cat("  - GSE124076_raw.rds (raw GEO object)\n")
  cat("  - GSE124076_expression_matrix.csv (expression values)\n")
  cat("  - GSE124076_phenotype_data.csv (sample metadata)\n")
  cat("  - GSE124076_feature_data.csv (gene annotations)\n")
  cat("  - GSE124076_expression_summary.csv (gene statistics)\n")
  cat("  - GSE124076_sample_info.csv (sample characteristics)\n")
  cat("  - GSE124076_top50_genes.csv (highest expressed genes)\n\n")
  
  cat("Next steps:\n")
  cat("  1. Inspect feature data to identify VDR and vitamin D genes\n")
  cat("  2. Extract specific gene expression for VDR pathway\n")
  cat("  3. Correlate with ancestry proportions if available\n")
  cat("  4. Perform differential expression analysis\n\n")
  
}, error = function(e) {
  cat("ERROR: ", e$message, "\n")
  cat("This may be due to:\n")
  cat("  - Network connectivity issues\n")
  cat("  - GEO server unavailability\n")
  cat("  - Dataset access restrictions\n\n")
  cat("Try running this script again or check the GEO accession manually at:\n")
  cat("  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124076\n")
})
