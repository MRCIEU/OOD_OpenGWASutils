#!/usr/bin/python3

"""
Pre-requisites: 
    - Install samtools (http://www.htslib.org/), which provides tools to support VCF file reading/writing:
        - Ubuntu: sudo apt-get install -y samtools
        - MacOS: brew install samtools
        - Others: download and compile from http://www.htslib.org/download/
    - Install pygwasvcf (https://github.com/MRCIEU/pygwasvcf):
        - pip install git+https://github.com/mrcieu/pygwasvcf
"""

import pygwasvcf


def get_metadata(databatch, dataset):
    """Retrieves meta-data from a VCF file in OpenGWAS"""
    with pygwasvcf.GwasVcf(
        f"https://objectstorage.us-ashburn-1.oraclecloud.com/n/idrvm4tkz2a8/b/OpenGWAS/o/{databatch}/{dataset}/{dataset}.vcf.gz"
    ) as g:
        return g.get_metadata()


def query_variant(databatch, dataset, contig, start, stop):
    """Retrieves data for a variant from a VCF file in OpenGWAS"""
    with pygwasvcf.GwasVcf(
        f"https://objectstorage.us-ashburn-1.oraclecloud.com/n/idrvm4tkz2a8/b/OpenGWAS/o/{databatch}/{dataset}/{dataset}.vcf.gz"
    ) as g:
        results = []
        for variant in g.query(contig=contig, start=start, stop=stop):
            results.append(variant)
        return results