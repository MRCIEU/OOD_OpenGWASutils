#!/bin/bash

    # ------------------------------------------------------------------------
    # Pre-requisites
    # ==============

    # Install samtools (http://www.htslib.org/), which provides tools to support VCF file reading/writing
    # Ubuntu: sudo apt-get install -y samtools
    # MacOS: brew install samtools
    # Others: download and compile from http://www.htslib.org/download/
    # ------------------
    # Usage
    # =====

    # Command format:
    #     bash queryVCF.sh     
    # Command-line arguments are optional, but positional (you must include all preceding arguments if specifying arguments after ):
    # Example: 
    #     bash queryVCF.sh bbj-a bbj-a-1 1 1000000 2000000
    # ------------------------------------------------------------------------

# Specify variables that take command line arguments or default values if absent
databatch=${1:-bbj-a}
dataset=${2:-bbj-a-1}
chromosome=${3:-1}
startpos=${4:-1000000}
endpos=${5:-2000000}

# Run tabix to extract the specified (or default) chromosome region from the specified (or default) dataset
tabix "https://objectstorage.us-ashburn-1.oraclecloud.com/n/idrvm4tkz2a8/b/OpenGWAS/o/${databatch}/${dataset}/${dataset}.vcf.gz" "${chromosome}:${startpos}-${endpos}"