'''
Created on May 1, 2020

@author: banyait
'''
import unittest
import pprint
from asb_usecases.wrappers.sentinel_product_query import process_wrapper
import os


class Test(unittest.TestCase):

    def setUp(self):
        os.environ['USERNAME']=''
        os.environ['USERPWD']=''

    def testSentinelProductQuery(self):
        test_fields='{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[5.499979, 51.129149], [5.499888, 51.129161], [5.499839, 51.129169], [5.499648, 51.129197], [5.499634, 51.1292], [5.499546, 51.129212], [5.499009, 51.129308], [5.498956, 51.129317], [5.498885, 51.12933], [5.498871, 51.129332], [5.498803, 51.12911], [5.4988, 51.1291], [5.498535, 51.128159], [5.498528, 51.128136], [5.498856, 51.127991], [5.498863, 51.127988], [5.498972, 51.127898], [5.498993, 51.127889], [5.499418, 51.127716], [5.499734, 51.127587], [5.499746, 51.127582], [5.499744, 51.127638], [5.499752, 51.127664], [5.499858, 51.128008], [5.500164, 51.128014], [5.500565, 51.128021], [5.500475, 51.128617], [5.500474, 51.128625], [5.50045, 51.128766], [5.500404, 51.129038], [5.500392, 51.1291], [5.500369, 51.129214], [5.500327, 51.129242], [5.500246, 51.129202], [5.500212, 51.129186], [5.500169, 51.129172], [5.500123, 51.129159], [5.500107, 51.129156], [5.500094, 51.12915], [5.500077, 51.129142], [5.500039, 51.129147], [5.500027, 51.129146], [5.499979, 51.129149]]]}, "properties": {}}, {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[5.498312, 51.130314], [5.496896, 51.130537], [5.49671, 51.130149], [5.497791, 51.129982], [5.498962, 51.129803], [5.498995, 51.129925], [5.498998, 51.129933], [5.498928, 51.129943], [5.498639, 51.130263], [5.498366, 51.130305], [5.49836, 51.130278], [5.498329, 51.130282], [5.498327, 51.130275], [5.498309, 51.130278], [5.498312, 51.130314]]]}, "properties": {}} ]}'
        test_daterange='{"start": "2019-12-01", "end": "2019-12-31"}'
        test_result='{"products": ["S2A_MSIL2A_20191202T105421_N0213_R051_T31UFS_20191202T122334", "S2B_MSIL2A_20191204T104319_N0213_R008_T31UFS_20191204T112920", "S2B_MSIL2A_20191207T105329_N0213_R051_T31UFS_20191207T121847", "S2A_MSIL2A_20191209T104431_N0213_R008_T31UFS_20191209T121731", "S2A_MSIL2A_20191212T105441_N0213_R051_T31UFS_20191212T122231", "S2B_MSIL2A_20191214T104339_N0213_R008_T31UFS_20191214T121213", "S2B_MSIL2A_20191217T105349_N0213_R051_T31UFS_20191217T123333", "S2A_MSIL2A_20191219T104441_N0213_R008_T31UFS_20191219T121223", "S2A_MSIL2A_20191222T105441_N0213_R051_T31UFS_20191222T122245", "S2B_MSIL2A_20191224T104349_N0213_R008_T31UFS_20191224T123641", "S2B_MSIL2A_20191227T105349_N0213_R051_T31UFS_20191227T121122", "S2A_MSIL2A_20191229T104441_N0213_R008_T31UFS_20191229T120309"], "tilesAndDates": {"31UFS": ["2019-12-02", "2019-12-04", "2019-12-07", "2019-12-09", "2019-12-12", "2019-12-14", "2019-12-17", "2019-12-19", "2019-12-22", "2019-12-24", "2019-12-27", "2019-12-29"]}}'

        output=process_wrapper.execute('', test_fields, test_daterange)
        print(output)
        pprint.pprint(output)
         
        self.assertEqual(output['products_json'],test_result)