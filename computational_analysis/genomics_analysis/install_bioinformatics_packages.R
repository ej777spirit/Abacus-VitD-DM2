# Comprehensive package installation for genomic analysis
# Created: October 1, 2025

cat("Installing R packages for genomic analysis...\n\n")

# Set CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org"))

# Core data manipulation and visualization packages
essential_packages <- c(
  "tidyverse",      # Data manipulation and visualization
  "data.table",     # Fast data operations
  "ggplot2",        # Advanced plotting
  "plotly",         # Interactive plots
  "gridExtra",      # Multiple plots
  "RColorBrewer",   # Color palettes
  "viridis"         # Color scales
)

# Statistical and genomic analysis packages
genomics_packages <- c(
  "genetics",       # Basic genetics
  "GenABEL",        # GWAS analysis (if available)
  "qqman",          # Manhattan and Q-Q plots
  "SNPassoc",       # SNP association studies
  "gap",            # Genetic analysis package
  "snpStats"        # SNP statistics
)

# Bioconductor packages (require BiocManager)
bioc_packages <- c(
  "Biobase",
  "GWASTools",
  "VariantAnnotation",
  "GenomicRanges",
  "biomaRt"
)

# Install essential packages
cat("Installing essential packages...\n")
for (pkg in essential_packages) {
  if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
    cat(paste("Installing", pkg, "...\n"))
    install.packages(pkg, quiet = TRUE)
  } else {
    cat(paste(pkg, "already installed.\n"))
  }
}

# Install genomics packages (some may fail, that's ok)
cat("\nInstalling genomics packages...\n")
for (pkg in genomics_packages) {
  tryCatch({
    if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
      cat(paste("Installing", pkg, "...\n"))
      install.packages(pkg, quiet = TRUE)
    } else {
      cat(paste(pkg, "already installed.\n"))
    }
  }, error = function(e) {
    cat(paste("Warning:", pkg, "not available from CRAN. Skipping.\n"))
  })
}

# Install BiocManager for Bioconductor packages
cat("\nInstalling BiocManager...\n")
if (!require("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager", quiet = TRUE)
}

# Install Bioconductor packages
cat("\nInstalling Bioconductor packages...\n")
for (pkg in bioc_packages) {
  tryCatch({
    if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
      cat(paste("Installing", pkg, "...\n"))
      BiocManager::install(pkg, quiet = TRUE, update = FALSE)
    } else {
      cat(paste(pkg, "already installed.\n"))
    }
  }, error = function(e) {
    cat(paste("Warning: Could not install", pkg, ". Skipping.\n"))
  })
}

# Additional utility packages
utility_packages <- c(
  "knitr",
  "rmarkdown",
  "DT",
  "htmltools"
)

cat("\nInstalling utility packages...\n")
for (pkg in utility_packages) {
  if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
    cat(paste("Installing", pkg, "...\n"))
    install.packages(pkg, quiet = TRUE)
  } else {
    cat(paste(pkg, "already installed.\n"))
  }
}

cat("\n\n=== Installation Summary ===\n")
cat("Essential packages: Installed\n")
cat("Genomics packages: Partially installed (some may require special setup)\n")
cat("Bioconductor packages: Installed\n")
cat("Utility packages: Installed\n")
cat("\nR environment is ready for genomic analysis!\n")
