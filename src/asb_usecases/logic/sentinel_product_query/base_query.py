'''
Created on May 4, 2020

@author: banyait
'''
from abc import ABC, abstractmethod
from collections import OrderedDict
import logging
import json
from shapely.geometry.geo import shape
from shapely.geometry import mapping
from resources import tiles_json_path

class BaseQuery(ABC):
    '''
    This is an abstract class for querying tile ids and taken dates based on date range and geojson specification of the areas of interest.
    Subclasses should implement __query__ and call super().__init__() in the ctor.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.logger=logging.getLogger(self.__class__.__name__)
        self.clean()
                
    @abstractmethod
    def _query(self, fields_geojson, startDate, endDate, cloudCover):
        '''
        Launches a query and returns a dict with the processed results. This is an additive operation, results will be appended to the existing until clean() is called.
        
        Args:
            fields (dict): geometries to look for in geojson format
            startDate (string): starting date in %Y%m%d format
            endDate (string): end date in %Y%m%d format
            cloudCover (int): exclude results above the cloud coverage percentage
            
        Returns:
            list of strings containing the sentinel tile ids
        '''
        raise NotImplementedError("__query__ is not implemented")

    def query(self, fields, startDate, endDate, cloudCover):
        self.logger.info("Starting query for {} feature(s)".format(str(len(fields['features']))))
        with tiles_json_path() as tilesjsonpath:
            with open(tilesjsonpath) as f:
                tileinfos=json.load(f)
                for ifield in fields['features']:
                    # getting the products
                    iproducts=self._query(ifield, startDate, endDate, cloudCover)
                    # splitting products to  useful infor
                    self.logger.info("Query found {} products.".format(str(len(iproducts))))
                    iproductIds=sorted(list(set(iproducts)),key=lambda k: ''.join(k.split('_')[5:1:-3]))
                    itileIds=OrderedDict()
                    for i in iproductIds:
                        ifields=i.split('_')
                        itakendate=ifields[2].split('T')[0]
                        itileid=ifields[5].split('T')[1]
                        idatelist=itileIds.get(itileid,[])
                        idatelist.append('-'.join([itakendate[0:4],itakendate[4:6],itakendate[6:8]]))
                        itileIds[itileid]=idatelist
                    self.logger.info("There are {} products and {} tiles in the feature.".format(str(len(iproductIds)),str(len(itileIds))))
                    # associating bounding boxes of the geometry within tile
                    iintersections=OrderedDict()
                    ifieldshape=shape(ifield['geometry'])
                    for itile in itileIds.keys():
                        itileshape=shape(tileinfos[itile])
                        iintersections[itile]=[{'type': 'Feature', 'properties': {}, 'geometry': mapping(itileshape.intersection(ifieldshape))}]                     
                    # appending to dataset
                    self.tileIds.append(itileIds)
                    self.productIds.append(iproductIds)
                    self.shapes.append(iintersections)
            
    def getTileIds(self):
        return list(self.tileIds.keys())
#        return sorted(list(self.tileIds.keys()))

    def getTakenDatesPerTileIds(self):
        return self.tileIds

    def getShapesPerTileIds(self):
        return self.shapes
    
    def getProductIds(self):
        return list(self.productIds)
#        return sorted(list(self.productIds))

    def clean(self):
        self.logger.info("Resetting query dataset.")
        self.productIds=[]
        self.tileIds=[]
        self.shapes=[]
