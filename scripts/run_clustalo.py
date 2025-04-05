"""
Reproducible Script for Multiple Sequence Alignment (MSA) using Clustal Omega

This script takes an input FASTA file containing sequences and performs a multiple sequence alignment
using Clustal Omega. The aligned output is saved to a specified file.

Chosen Algorithm: Clustal Omega
-----------------------------------
Description:
Clustal Omega is a progressive alignment method that uses a guide tree to align sequences in a stepwise fashion.
It builds a distance matrix from pairwise sequence comparisons and then uses Hidden Markov Models (HMMs) to refine
the alignment as the sequences are progressively added.

Assumptions:
- The input sequences are homologous and share some evolutionary relationship.
- A guide tree generated from pairwise sequence distances is a reasonable approximation for the evolutionary history.
- Default parameters are generally effective for many datasets, though they may need to be fine-tuned for specific cases.

Limitations:
- Clustal Omega may not perform as well when the sequences are extremely divergent.
- It does not offer extensive iterative refinement as some other methods might.
- The quality of the alignment is largely dependent on the accuracy of the guide tree, which may be less reliable
  for complex datasets.

Instructions:
1. Ensure Clustal Omega is installed on your Ubuntu system (e.g., `sudo apt-get install clustalo`).
2. Make sure the input file is located in your project directory. In this example, the project directory is:
   "C:\Users\gavin\Downloads\Botany563\myProject"
   (on Ubuntu, adjust the path accordingly).
3. Run the script from the command line as follows:
      python run_clustalo.py <input_fasta> <output_alignment>
4. Commit your updated script to GitHub regularly. For example:
      git add run_clustalo.py
      git commit -m "Added reproducible MSA script using Clustal Omega"
      git push
5. Submit your GitHub commit link as required.

Author: [Your Name]
Date: [Today's Date]
"""

import subprocess
import sys
import os

def run_clustalo(input_fasta, output_alignment):
    """
    Runs Clustal Omega on the input FASTA file and writes the alignment to the output file.
    
    Parameters:
    - input_fasta: str, path to the input FASTA file containing sequences.
    - output_alignment: str, path to the output file where the aligned sequences will be saved.
    """
    # Build the Clustal Omega command.
    # --force: overwrite output file if exists
    # --outfmt: output format (fasta in this case)
    command = [
        'clustalo',
        '-i', input_fasta,
        '-o', output_alignment,
        '--force',
        '--outfmt', 'fasta'
    ]

    try:
        print(f"Running Clustal Omega on {input_fasta}...")
        subprocess.run(command, check=True)
        print(f"Alignment complete. Results saved to {output_alignment}")
    except subprocess.CalledProcessError as e:
        print("Error: Clustal Omega did not run successfully.", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Clustal Omega is not installed or not found in your PATH.", file=sys.stderr)
        sys.exit(1)

def main():
    # Expect exactly two arguments: input_fasta and output_alignment
    if len(sys.argv) != 3:
        print("Usage: python run_clustalo.py <input_fasta> <output_alignment>")
        sys.exit(1)
    
    input_fasta = sys.argv[1]
    output_alignment = sys.argv[2]
    
    # Check if the input FASTA file exists
    if not os.path.isfile(input_fasta):
        print(f"Error: The file {input_fasta} does not exist.", file=sys.stderr)
        sys.exit(1)

    # Run Clustal Omega to generate the alignment
    run_clustalo(input_fasta, output_alignment)

if __name__ == '__main__':
    main()

