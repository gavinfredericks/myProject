#!/usr/bin/env Rscript
# build_trees.R
#
# Reproducible Script for Estimating Distance-Based and Parsimony-Based Trees
#
# This script uses the ape and phangorn R packages to estimate two phylogenetic trees
# from an aligned dataset.
#
# Chosen Methods:
# ----------------
# 1. Distance-Based Tree (Neighbor Joining)
#    - Algorithm: The Neighbor Joining (NJ) method computes a distance matrix from the data 
#      and then iteratively clusters sequences based on minimal evolution.
#    - Assumptions:
#         * The distances reflect the true evolutionary divergence between sequences.
#         * The chosen substitution model adequately describes the evolutionary process.
#    - Limitations:
#         * NJ does not explicitly model the evolution process.
#         * It may be less accurate when the distance estimates are biased.
#
# 2. Parsimony-Based Tree
#    - Algorithm: Parsimony methods search for the tree topology that minimizes the total 
#      number of evolutionary changes (steps) required to explain the data.
#    - Assumptions:
#         * Evolution proceeds with the minimum number of changes.
#         * Characters evolve independently.
#    - Limitations:
#         * Parsimony can be susceptible to long-branch attraction.
#         * It may oversimplify complex evolutionary processes.
#
# Instructions:
# - Ensure that the ape and phangorn packages are installed.
# - Place your aligned sequences in a file (e.g., "aligned_sequences.fasta") in your working directory.
# - Run this script from the command line: Rscript build_trees.R
# - Commit your updated script to GitHub frequently, and submit your commit link as required.
#


# Load required libraries
library(ape)
library(phangorn)

# Define file paths (adjust these paths to match your system/environment)
alignment_file <- "aligned_sequences.fasta"  # Input alignment file in FASTA format

# Read the alignment into a phyDat object for parsimony analysis
alignment_phydat <- read.phyDat(alignment_file, format = "fasta")

# For the distance-based tree, we can also use ape's read.dna
alignment_dna <- read.dna(alignment_file, format = "fasta")

# Estimate a distance matrix using a simple model (e.g., Kimura 2-parameter)
dist_matrix <- dist.dna(alignment_dna, model = "K80")

# Build a distance-based tree using the Neighbor Joining (NJ) method
nj_tree <- nj(dist_matrix)
# Plot and save the NJ tree
pdf("NJ_tree.pdf")
plot(nj_tree, main = "Distance-Based Tree (Neighbor Joining)")
dev.off()
cat("Distance-based (NJ) tree saved to NJ_tree.pdf\n")

# Estimate a parsimony-based tree
# First, get a starting tree (e.g., from NJ tree) for parsimony search
starting_tree <- nj_tree

# Perform a parsimony score calculation on the starting tree
parsimony_score <- parsimony(starting_tree, alignment_phydat)
cat("Parsimony score for the starting tree: ", parsimony_score, "\n")

# Optimize tree topology using the parsimony criterion with a heuristic search
parsimony_tree <- optim.parsimony(starting_tree, alignment_phydat)
# Calculate parsimony score for the optimized tree
opt_parsimony_score <- parsimony(parsimony_tree, alignment_phydat)
cat("Optimized parsimony score: ", opt_parsimony_score, "\n")

# Plot and save the parsimony-based tree
pdf("Parsimony_tree.pdf")
plot(parsimony_tree, main = "Parsimony-Based Tree")
dev.off()
cat("Parsimony-based tree saved to Parsimony_tree.pdf\n")

# Save trees in Newick format
write.tree(nj_tree, file = "NJ_tree.newick")
write.tree(parsimony_tree, file = "Parsimony_tree.newick")
cat("Trees saved in Newick format.\n")
