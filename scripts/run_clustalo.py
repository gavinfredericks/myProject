"""
Reproducible Script for Multiple Sequence Alignment (MSA) using MAFFT and MUSCLE

This script takes an input FASTA file containing sequences and performs a multiple sequence alignment
using either MAFFT or MUSCLE. The aligned output is saved to a specified file.

Chosen Algorithms: MAFFT and MUSCLE
---------------------------------------
Description:
Both MAFFT and MUSCLE are progressive alignment methods. MAFFT provides several modes (the '--auto'
option selects the best algorithm based on your data), while MUSCLE uses iterative refinement methods.
These tools assume the input sequences are homologous and that a progressive alignment method is sufficient
to capture the overall evolutionary relationships.

Assumptions:
- The input sequences are homologous and share some evolutionary relationship.
- Default parameters are generally effective for many datasets, though they may need adjustment for specific cases.
- MAFFT and MUSCLE are installed and available in your system PATH.

Limitations:
- Extremely divergent sequences may not align optimally using default settings.
- MUSCLE may require specific handling on some architectures.
- The quality of the alignment relies on the inherent limitations of the chosen algorithm.

Instructions:
1. Ensure MAFFT and MUSCLE are installed on your system.
   For example, on Ubuntu:
       sudo apt install mafft muscle
2. Make sure the input file is located in your project directory. For this example, the project directory is:
   "C:\Users\gavin\Downloads\Botany563\myProject" (adjust the path accordingly for Ubuntu).
3. Run the script from the command line as follows:
       python run_msa.py <aligner> <input_fasta> <output_alignment>
   where <aligner> is either "mafft" or "muscle".
4. Commit your updated script to GitHub regularly. For example:
       git add run_msa.py
       git commit -m "Added reproducible MSA script using MAFFT and MUSCLE"
       git push
5. Submit your GitHub commit link as required.
"""

import subprocess
import sys
import os

def run_mafft(input_fasta, output_alignment):
    """
    Runs MAFFT on the input FASTA file and writes the alignment to the output file.
    
    Parameters:
    - input_fasta: str, path to the input FASTA file.
    - output_alignment: str, path where the aligned sequences will be saved.
    """
    command = ["mafft", "--auto", input_fasta]
    try:
        print(f"Running MAFFT on {input_fasta}...")
        # Use a file handle to capture stdout and write to output_alignment.
        with open(output_alignment, "w") as outf:
            subprocess.run(command, stdout=outf, check=True)
        print(f"MAFFT alignment complete. Results saved to {output_alignment}")
    except subprocess.CalledProcessError:
        print("Error: MAFFT did not run successfully.", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: MAFFT is not installed or not found in your PATH.", file=sys.stderr)
        sys.exit(1)

def run_muscle(input_fasta, output_alignment):
    """
    Runs MUSCLE on the input FASTA file and writes the alignment to the output file.
    
    Parameters:
    - input_fasta: str, path to the input FASTA file.
    - output_alignment: str, path where the aligned sequences will be saved.
    
    Note: MUSCLE (v5) may require input redirection.
    """
    command = ["muscle"]
    try:
        print(f"Running MUSCLE on {input_fasta}...")
        # Open the input file and set it as the standard input for MUSCLE.
        with open(input_fasta, "r") as inf, open(output_alignment, "w") as outf:
            subprocess.run(command, stdin=inf, stdout=outf, check=True)
        print(f"MUSCLE alignment complete. Results saved to {output_alignment}")
    except subprocess.CalledProcessError:
        print("Error: MUSCLE did not run successfully.", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("Error: MUSCLE is not installed or not found in your PATH.", file=sys.stderr)
        sys.exit(1)

def main():
    # Expect three arguments: aligner, input_fasta, and output_alignment
    if len(sys.argv) != 4:
        print("Usage: python run_msa.py <aligner> <input_fasta> <output_alignment>")
        print("       <aligner> should be either 'mafft' or 'muscle'")
        sys.exit(1)

    aligner = sys.argv[1].lower()
    input_fasta = sys.argv[2]
    output_alignment = sys.argv[3]

    # Verify the input FASTA file exists
    if not os.path.isfile(input_fasta):
        print(f"Error: The file '{input_fasta}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Choose the alignment tool based on the provided argument
    if aligner == "mafft":
        run_mafft(input_fasta, output_alignment)
    elif aligner == "muscle":
        run_muscle(input_fasta, output_alignment)
    else:
        print("Error: Unknown aligner. Please choose 'mafft' or 'muscle'.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()


