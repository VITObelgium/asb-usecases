#!/usr/bin/python

import logging
import xarray
from pathlib import Path
import glob

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

def execute(out_dir, status, outputFile):
    """
    Inputs:
    status -- status -- 45/User String
    outputFile -- outputFile -- 45/User String

    Outputs:
    result -- result -- 95/User String

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

    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------

    logger.info("Starting...")
    
    if status=="success":
    
        # combine using max
        rxr=None
        for ifile in glob.glob(str(Path(out_dir,'part_*'))):
            with open(ifile,'r') as f:
                logger.info("Merging: "+ifile)
                ds=xarray.open_dataset(ifile, engine='h5netcdf')
                iarr=ds.to_array(dim='band')
                #iarr=xarray.DataArray.from_dict(jsonarry=json.load(f,default=str))
                if rxr is None: 
                    rxr=iarr
                    rxr=rxr.assign_coords({'band':['maxNDVI']})
                else:
                    rxr=xarray.concat([rxr,iarr], dim='band',join='outer').max(dim='band').expand_dims({'band':['maxNDVI']})
                logger.info("Shape:   "+str(rxr.shape));
                logger.info("X-range: "+str(rxr.x.min().values)+" ... "+str(rxr.x.max().values));
                logger.info("Y-range: "+str(rxr.y.min().values)+" ... "+str(rxr.y.max().values));
    
        # write to netcdf, with switching x&y (for example QGIS displays the image otherwise rotated)
        if rxr is not None:
            if rxr.dims[-2]=='x' and rxr.dims[-1]=='y':
                l=list(rxr.dims[:-2])
                rxr=rxr.transpose(*(l+['y','x']))
            result=rxr.to_dataset('band')
            result.to_netcdf(str(Path(out_dir,outputFile)), engine='h5netcdf')    
            logger.info("Combined result saved to: "+str(Path(out_dir,outputFile)))
        else: 
            outputFile="<EMPTY>"
            logger.info("Combined result is empty, skipping")

    logger.info("Finished...")

    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "result": outputFile
    }