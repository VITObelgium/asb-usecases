#!/usr/bin/python

import logging
import json
import shapely.geometry
import openeo
#import shapefile

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

class TimeSeriesQuery():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
#        self.url='http://openeo-dev.vgt.vito.be/openeo/0.4.0/'
        self.url='http://openeo.vgt.vito.be/openeo/0.4.0/'
    
    def getQuery(self, layer, fields, start_date, end_date):

        conn = openeo.connect(self.url)
        
        # for shapefile
        #shps=list(filter(lambda i: i.shapeTypeName=='POLYGON',shapefile.Reader("../utils/test.shp").shapes()))
        #polys=shapely.geometry.GeometryCollection([shapely.geometry.shape(i) for i in shps])
        
        # for geojson, geometrycollection should automagically work on both polygons and multipolygons
        # NOTE: buffer(0) is a trick for fixing scenarios where polygons have overlapping coordinates: https://medium.com/@pramukta/recipe-importing-geojson-into-shapely-da1edf79f41d
        features = fields["features"]
        polys = shapely.geometry.GeometryCollection([shapely.geometry.shape(feature["geometry"]).buffer(0) for feature in features])
          
        bbox = polys.bounds
    
        result = (
            conn
                .load_collection(layer)
                .filter_temporal(start_date, end_date)
                .filter_bbox(crs="EPSG:4326", **dict(zip(["west", "south", "east", "north"], bbox)))
                .polygonal_mean_timeseries(polys)
                .execute()
        )
        
        logger.info(json.dumps(result))
        
        for ipoly in range(len(fields["features"])):
            ts= sorted(
                    list(
                        filter(
                            lambda g: g[1] is not None,
                            map(
                                lambda i: (i[0],i[1][ipoly][0]),
                                filter(
                                    lambda f: len(f[1][ipoly])>0,
                                    result.items()
                                )
                            )
                        )
                    ),
                    key=lambda k: k[0]
                )
            fields["features"][ipoly]["timeseries"]=ts
            del fields["features"][ipoly]["geometry"]
        
        return fields


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