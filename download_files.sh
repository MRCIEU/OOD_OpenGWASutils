#!/bin/bash

    # ------------------------------------------------------------------------
    # Usage
    # =====

    # Command format:
    #     bash download_dataset.sh   
    # Command-line arguments are optional, but positional (you must include all preceding arguments if specifying arguments after ):
    # Example: 
    #     bash download_dataset.sh bbj-a bbj-a-1 
    # ------------------------------------------------------------------------

# Specify variables that take command line arguments or default values if absent
databatch=${1:-bbj-a}
dataset=${2:-bbj-a-1}

# Run tabix to extract the specified (or default) chromosome region from the specified (or default) dataset
curl "https://objectstorage.us-ashburn-1.oraclecloud.com/n/idrvm4tkz2a8/b/OpenGWAS/o/${databatch}/${dataset}/${dataset}.vcf.gz"
curl "https://objectstorage.us-ashburn-1.oraclecloud.com/n/idrvm4tkz2a8/b/OpenGWAS/o/${databatch}/${dataset}/${dataset}.vcf.gz.tbi"