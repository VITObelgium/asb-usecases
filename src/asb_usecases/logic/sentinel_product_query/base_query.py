'''
Created on May 4, 2020

@author: banyait
'''
from abc import ABC, abstractmethod
from collections import OrderedDict
import logging

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
            fields_geojson (dict): geometries to look for in geojson format
            startDate (string): starting date in %Y%m%d format
            endDate (string): end date in %Y%m%d format
            cloudCover (int): exclude results above the cloud coverage percentage
            
        Returns:
            list of strings containing the sentinel tile ids
        '''
        raise NotImplementedError("__query__ is not implemented")

    def query(self, fields_geojson, startDate, endDate, cloudCover):
        self.logger.info("Starting query")
        products=self._query(fields_geojson, startDate, endDate, cloudCover)
        self.logger.info("Query found {} products.".format(str(len(products))))
        self.productIds=sorted(list(set(products+self.productIds)),key=lambda k: ''.join(k.split('_')[5:1:-3]))
        self.tileIds=OrderedDict()
        for i in self.productIds:
            ifields=i.split('_')
            itakendate=ifields[2].split('T')[0]
            itileid=ifields[5].split('T')[1]
            idatelist=self.tileIds.get(itileid,[])
            idatelist.append('-'.join([itakendate[0:4],itakendate[4:6],itakendate[6:8]]))
            self.tileIds[itileid]=idatelist
#         for k in self.tileIds.keys():
#             self.tileIds[k]=sorted(self.tileIds[k])
        self.logger.info("There are {} products and {} tiles in the dataset.".format(str(len(self.productIds)),str(len(self.tileIds))))
            
    def getTileIds(self):
        return list(self.tileIds.keys())
#        return sorted(list(self.tileIds.keys()))

    def getTakenDatesPerTileIds(self):
        return self.tileIds
    
    def getProductIds(self):
        return list(self.productIds)
#        return sorted(list(self.productIds))

    def clean(self):
        self.logger.info("Resetting query dataset.")
        self.productIds=[]
        self.tileIds=OrderedDict()
