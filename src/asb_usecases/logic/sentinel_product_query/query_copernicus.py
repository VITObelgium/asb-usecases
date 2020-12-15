from asb_usecases.logic.sentinel_product_query.base_query import BaseQuery
from sentinelsat.sentinel import SentinelAPI, geojson_to_wkt
import os

class CopernicusQuery(BaseQuery):
    
    def _query(self, fields_geojson, startDate, endDate, cloudCover):
        api = SentinelAPI(os.environ.get('USERNAME', ''), os.environ.get('USERPWD',''), 'https://scihub.copernicus.eu/dhus')
        
        # search by polygon, time, and SciHub query keywords
        footprint = geojson_to_wkt(fields_geojson)
        products = api.query(footprint,
                             date=(startDate.replace('-',''), endDate.replace('-','')),
                             cloudcoverpercentage=(0,float(cloudCover)),
                             processinglevel='Level-2A',
                             platformname='Sentinel-2')
        # get tile ids
        productids=sorted(list(set(map(lambda t: t[1]['identifier'],products.items()))))
        return productids

#         
#         for i in productids: print(i)
#         print('finished, number of products: '+str(len(productids)))
        