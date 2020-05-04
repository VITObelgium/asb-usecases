import logging
import json
import shapely.geometry
import openeo
#import shapefile

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
