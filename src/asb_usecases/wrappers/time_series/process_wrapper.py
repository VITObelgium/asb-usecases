#!/usr/bin/python

import logging
import json
from asb_usecases.logic.time_series.openeo_query import TimeSeriesQuery

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

def execute(out_dir, layer_id, fields_geojson, daterange_json):
    """
    Inputs:
    layer_id -- layer_id -- 45/User String
    fields_geojson -- fields_geojson -- 45/User String
    daterange_json -- daterange_json -- 45/User String

    Outputs:
    timeseries_json -- timeseries_json -- 45/User String

    Main Dependency:
    mep-wps/uc-bundle-1

    Software Dependencies:
    pywps-4

    Processing Resources:
    ram -- 1
    disk -- 1
    cpu -- 1
    """

    timeseries_json = None

    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------

    logger.info("Starting...")
    
    fields=json.loads(fields_geojson)
    daterange=json.loads(daterange_json)

    tsq=TimeSeriesQuery()
    timeseries_json=json.dumps(tsq.getQuery(layer_id,fields,daterange['start'],daterange['end']))


    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "timeseries_json": timeseries_json
    }