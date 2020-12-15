#!/usr/bin/python

import logging
import os
import json
import io

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
stream = io.StringIO()
handler = logging.StreamHandler(stream)
logger.addHandler(handler)

def execute(out_dir, segmentedfiles_json):
    """
    Inputs:
    segmentedfiles_json -- segmentedfiles_json -- 45/User String

    Outputs:
    vectorizedfiles_json -- vectorizedfiles_json -- 45/User String
    exceptionLog -- exceptionLog -- 45/User String

    Main Dependency:
    mep-wps/uc-bundle-1

    Software Dependencies:
    pywps-4

    Processing Resources:
    ram -- 8
    disk -- 10
    cpu -- 1
    """

    vectorizedfiles_json = None

    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------

    try:

        logger.info("Starting...")
        logger.info("Contents of out_dir: "+str(os.listdir(path=str(out_dir))))
    
        from parcel.feature.segmentation import raster2polygon
    
        logger.info("Loading json input(s)...")

        segmentedfiles=json.loads(segmentedfiles_json)
     
        logger.info("Computing...")

        vectorizedfiles=[]
        for i in range(len(segmentedfiles)):
            iresults={}
            for tile,segfile in segmentedfiles[i].items():
                workdir=os.path.dirname(segfile)
                outshp=raster2polygon.main(
                    workdir, 
                    tile=tile, 
                    overwrite=True
                )
                iresults[tile]=outshp[0]
            vectorizedfiles.append(iresults)

        logger.info("Contents of out_dir: "+str(os.listdir(path=str(out_dir))))
        logger.info("Dumping results into json...")
        
        vectorizedfiles_json=json.dumps(vectorizedfiles)

        logger.info("Finished...")

    except Exception as e:
        logger.exception("Exception in wrapper.")

    logging.shutdown()
    stream.flush()
    exceptionLog=stream.getvalue()

    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "vectorizedfiles_json": vectorizedfiles_json,
        "exceptionLog": exceptionLog
    }