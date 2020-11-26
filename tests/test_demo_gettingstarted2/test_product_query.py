'''
Created on Nov 12, 2020

@author: banyait
'''
import unittest
import demo_gettingstarted2.product_query.process_wrapper
import demo_gettingstarted2.compute_maxndvi.process_wrapper
import demo_gettingstarted2.collect_and_max.process_wrapper
import json
from pathlib import Path
import uuid
import os

#POLYGON ((4.35063754016089 51.1109821138821,4.349236449732 51.0885462577691,4.369552260951 51.0729227147166,4.36009490055595 51.0310872783578,4.38391343784719 50.9905369345799,4.66588288666266 50.9905369345799,4.66588288666266 51.1103223911625,4.35063754016089 51.1109821138821))
poly_wkt='POLYGON((4.665785 51.110600, 4.350147 51.111254, 4.344939 50.990762, 4.664744 50.990762, 4.665785 51.110600))'
products=[
    "file:///data/MTDA/TERRASCOPE_Sentinel2/TOC_V2/2018/06/05/S2B_20180605T105029_31UFS_TOC_V200/S2B_20180605T105029_31UFS_TOC-B0+4_10M_V200.tif+8_10M_V200.tif",
    "file:///data/MTDA/TERRASCOPE_Sentinel2/TOC_V2/2018/06/15/S2B_20180615T105029_31UFS_TOC_V200/S2B_20180615T105029_31UFS_TOC-B0+4_10M_V200.tif+8_10M_V200.tif",
    "file:///data/MTDA/TERRASCOPE_Sentinel2/TOC_V2/2018/06/25/S2B_20180625T105029_31UFS_TOC_V200/S2B_20180625T105029_31UFS_TOC-B0+4_10M_V200.tif+8_10M_V200.tif"
]

class TestProductQuery(unittest.TestCase):

    tempfiles=[]
    temppath=Path('/tmp',uuid.uuid4().hex)
    query_result=""

    def test01_PQ(self):
        self.__class__.query_result=demo_gettingstarted2.product_query.process_wrapper.execute(
            None,
            '{"start":"2018-06-01T00:00:00", "end":"2018-06-30T00:00:00"}', 
            poly_wkt, 
            'urn:eop:VITO:TERRASCOPE_S2_TOC_V2',
            '["B04","B08"]'
        )
        print(self.__class__.query_result)
        print(len(json.loads(self.__class__.query_result['products'])))
        
    def test02_NDVI(self):
        os.mkdir(self.temppath)
        results=[]
        #for iproduct in products:
        for iproduct in [ i for i in json.loads(self.__class__.query_result['products']) if "31UFS" in i ]:
            results.append(demo_gettingstarted2.compute_maxndvi.process_wrapper.execute(
                self.temppath,
                poly_wkt,
                iproduct
            ))
        self.tempfiles = [ i["result"] for i in results ]
        print(self.tempfiles)
 
    def test03_maxCollect(self):
        results=demo_gettingstarted2.collect_and_max.process_wrapper.execute(
            self.temppath,
            "success",
            'mergedResults.nc'
        )
        print(results)
