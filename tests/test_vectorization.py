'''
Created on May 1, 2020

@author: banyait
'''
import unittest
import pprint
from asb_usecases.wrappers.vectorization import process_wrapper


class Test(unittest.TestCase):

    def testSentinelProductQuery(self):
        test_segmentedfiles='[{"31UFS": "/home/banyait/test_segmentation_data/02_output_for_segmentation_post/0/31UFS_segmentedImage.tif"}]'
        test_result='[{"31UFS": "/home/banyait/test_segmentation_data/02_output_for_segmentation_post/0/31UFS/31UFS_segmentedImage_felzenszwalbRAG_015threshold_025haSelected_4500mCropped_Buffer10m.shp"}]'
        
        output=process_wrapper.execute('', test_segmentedfiles)        
        print(output)
        pprint.pprint(output)
         
        self.assertEqual(output['vectorizedfiles_json'],test_result)
