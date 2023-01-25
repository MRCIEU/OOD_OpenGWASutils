#!/usr/local/bin/python
'''
Script to pull a complete file listing from Oracle Open Data OpenGWAS object storage
'''

import json
import requests as req

def get_page(url, start=None):
    '''
    Query Oracle Open Data for a JSON page of filenames
    '''
    if start:
        response = req.get(url+f"?start={start}")
    else:
        response = req.get(url)
    data = response.json()
    try:
        nextstart = data['nextStartWith'] 
    except:
        nextstart = "End"
    return(data['objects'], nextstart)


def get_filelist(url):
    '''
    Compile a list of filenames by looping over pages (get_page)
    '''
    with open("opengwasfiles.txt",'w') as f:
        nextstart = None
        while True:                         # Loop until the last page
            filelist, nextstart = get_page(url, nextstart)
            for file in filelist:
                f.write(file['name'] + "\n")
            if nextstart == "End":
                break                      # Break on the last page 


if __name__ == "__main__":
    url = "https://objectstorage.us-ashburn-1.oraclecloud.com/n/idrvm4tkz2a8/b/OpenGWAS/o/"
    get_filelist(url)
        
        






