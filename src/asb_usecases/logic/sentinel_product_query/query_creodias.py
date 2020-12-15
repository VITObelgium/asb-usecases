from asb_usecases.logic.sentinel_product_query.base_query import BaseQuery
from sentinelsat.sentinel import geojson_to_wkt
from datetime import datetime
import requests

class CreoDiasQuery(BaseQuery):

    def _query(self, fields_geojson, startDate, endDate, cloudCover):

        ep='https://finder.creodias.eu/resto/api/collections/Sentinel2/search.json'
        itemsPerPage=100
    
        geodata=fields_geojson
        geometry = geojson_to_wkt(geodata)
    
        query_params = [
            ('processingLevel', 'LEVEL2A'),
            ('sortParam', 'startDate'),
            ('sortOrder', 'ascending'),
            ('status', 'all'),
            ('dataset', 'ESA-DATASET'),
            ('maxRecords', itemsPerPage),
            ('cloudCover','[0,'+str(int(cloudCover))+']'),
            ('startDate', datetime.strptime(startDate, "%Y-%m-%d").isoformat()),
            ('completionDate', datetime.strptime(endDate, "%Y-%m-%d").isoformat()),
            ('geometry', geometry)
        ]
    
        # since int(response['properties']['totalResults']) does not always return exact count, therefore need to query until features is empty
        productids=[]
        for i in range(int(10000/itemsPerPage)):
            response = requests.get(ep, params=query_params+[('page',str(i+1))]).json()
            if len(response['features'])==0: break
            productids+=list(map(lambda j: j['properties']['productIdentifier'].split('/')[-1].replace('.SAFE',''),response['features']))
        if len(productids)>=10000:
            raise Exception("Total hits larger than 10000, which is not supported by paging: either split your job to multiple smaller or implement scroll or search_after.")

        return productids
        
    

