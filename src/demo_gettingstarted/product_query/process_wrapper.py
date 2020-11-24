#!/usr/bin/python

import logging
import requests
import json

# --------------------------------------------------------------------------------------
# Save this code in file "process_wrapper.py" and adapt as indicated in inline comments.
#
# Notes:
#  - This is a Python 3 script.
#  - The inputs will be given values by name, thus their order has no importance ...
#  - ... except that the inputs with a default value must be listed last.
#  - Parameter names are automatically converted into valid Python variable names.
#  - Any empty line or line starting with a '#' character will be ignored.
# --------------------------------------------------------------------------------------


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def execute(out_dir, daterange, wkt, collection, bands):
    """
    Inputs:
    daterange -- daterange -- 44/DateRange
    wkt -- wkt -- 92/WKT String
    collection -- collection -- 45/User String
    bands -- bands -- 45/User String

    Outputs:
    products -- products -- 95/Object Type
    wkt -- wkt -- 92/WKT String

    Main Dependency:
    mep-wps/uc-bundle-1

    Software Dependencies:
    pywps-4

    Processing Resources:
    ram -- 4
    disk -- 10
    cpu -- 1
    gpu -- 0
    """

    products = []

    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------

    logger.info("Starting...")
    logger.info("Date range: "+daterange)
    logger.info("WKT string: "+wkt)
    logger.info("Bands:      "+bands)
    
    d=json.loads(daterange)
    b=json.loads(bands)
    startIndex=1
    
    rs=  'https://services.terrascope.be/catalogue/products'\
        +'?collection='+collection\
        +'&accessedFrom=MEP'\
        +'&start='+d['start']\
        +'&end='+d['end']\
        +'&geometry='+wkt
    while(True):
        response = requests.get(rs+'&startIndex='+str(startIndex))
        if response.status_code<200 or response.status_code>=300:
            raise Exception("Bad response from server: "+response.reason+' ('+str(response.status_code)+')')
        response = json.loads(response.text)
        for product in response['features']:
            p=[]
            for ibnd in b:
                for iprod in product['properties']['links']['data']:
                    if ibnd in iprod['href']:
                        p.append(iprod['href'])
            products.append(p)
        startIndex+=response['itemsPerPage']
        if startIndex>response['totalResults']: break
        
    #products=json.dumps(products)

    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "products": str(products),
        "wkt": wkt
    }