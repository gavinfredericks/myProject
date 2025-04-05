# iqtree_ml.sh
#
# Reproducible Script for Maximum Likelihood (ML) Phylogenetic Analysis using IQ‐Tree
#
# Chosen Method: IQ‐Tree Maximum Likelihood Analysis with ModelFinder and Ultra‐Fast Bootstrap (UFBoot)
#
# Description:
# IQ‐Tree is a fast and efficient maximum likelihood phylogenetic inference tool that integrates
# ModelFinder to automatically select the best-fit substitution model. It further estimates branch
# support using the Ultra-Fast Bootstrap method, which provides robust support values in a fraction
# of the time required by traditional bootstrap approaches.
#
# Assumptions:
# - The input alignment file (deer alignment.fas) is high quality and contains homologous sequences.
# - The substitution models tested by ModelFinder sufficiently describe the evolutionary process.
# - The dataset is appropriate for ML methods, and the likelihood model is a good approximation
#   of the evolutionary history.
#
# Limitations:
# - ML methods, including those implemented in IQ‐Tree, can be computationally intensive for very large datasets.
# - The quality of the ML tree is highly dependent on the accuracy of the alignment and the chosen substitution model.
# - Ultra-Fast Bootstrap values are approximations and may not capture all aspects of true branch support,
#   especially in cases of complex evolutionary scenarios.
#
# How to Use This Script:
#
# Prepare Your Environment:
#
# 1. Ensure IQ‐Tree is installed on your Ubuntu system. If not, install it using:
#      sudo apt-get install iqtree
#
# Verify the File Path:
#
# 2. Confirm that your deer alignment file is accessible at:
#      /mnt/c/Users/gavin/Downloads/Botany563/myProject/deer alignment.fas
#    (or update the path in the script accordingly).
#
# Make the Script Executable:
#
# 3. Open a terminal in your project directory and run:
#      chmod +x iqtree_ml.sh
#
# Run the Script:
#
# 4. Execute the script:
#      ./iqtree_ml.sh
#
# Version Control:
#
# 5. Commit this script to your GitHub repository and push the changes:
#      git add iqtree_ml.sh
#      git commit -m "Added reproducible ML analysis script using IQ-Tree on deer alignment"
#      git push
#
# 6. Submit the GitHub commit link via Canvas as required.
#

# Define the alignment file path (convert Windows path to Ubuntu format)
ALIGNMENT_FILE="/mnt/c/Users/gavin/Downloads/Botany563/myProject/deer alignment.fas"

# Check if the alignment file exists
if [ ! -f "$ALIGNMENT_FILE" ]; then
    echo "Error: Alignment file not found at $ALIGNMENT_FILE"
    exit 1
fi

echo "Running IQ‐Tree analysis on file: $ALIGNMENT_FILE"

# Run IQ‐Tree:
# - -s: Specifies the input alignment file.
# - -m MFP: Activates ModelFinder Plus for automatic model selection.
# - -bb 1000: Runs 1000 ultrafast bootstrap replicates.
# - -pre: Sets the prefix for output files.
iqtree -s "$ALIGNMENT_FILE" -m MFP -bb 1000 -pre iqtree_deer

echo "IQ‐Tree analysis complete. Output files with prefix 'iqtree_deer' have been generated."

