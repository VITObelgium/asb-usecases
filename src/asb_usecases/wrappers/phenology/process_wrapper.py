#!/usr/bin/python

import logging
import json
import pandas

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

def execute(out_dir, timeseries_json):
    """
    Inputs:
    timeseries_json -- timeseries_json -- 45/User String

    Outputs:
    phenology_json -- phenology_json -- 45/User String

    Main Dependency:
    mep-wps/uc-bundle-1

    Software Dependencies:
    pywps-4

    Processing Resources:
    ram -- 1
    disk -- 1
    cpu -- 1
    """

    phenology_json = None

    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------

    logger.info("Starting...")

    from asb_usecases.logic.phenology.cropphenology import PhenologypParams,CropPhenology

    params=PhenologypParams()
    ts=json.loads(timeseries_json)
    for iserie in ts['features']:
        timeseries=pandas.DataFrame(
            data={
                #list(map(lambda x: parse(x['date'], "%Y-%m-%d"), iserie["timeseries"])),
                'Times':     [pandas.Timestamp(i[0]).tz_convert(None) for i in iserie["timeseries"]],  
                'Greenness': [                                  i[1]  for i in iserie["timeseries"]] # json loads already converted to float
            }
        )
        cp=CropPhenology()
        iserie['phenology']=cp.extractSeasonDates(timeseries, params)
        del iserie['timeseries']
    phenology_json=json.dumps(ts)

    # ...


    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "phenology_json": phenology_json
    }