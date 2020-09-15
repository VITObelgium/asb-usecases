# Example:
# https://gitlab.spaceapplications.com/eos/asb-applications/blob/develop/processing-services/ucl.rgb2hsv/process/ucl/rgb2hsv_tileconverter.py
 
from abstract_process import AbstractProcess
 
class Process(AbstractProcess):

    PROCESS_DESC = {
        'identifier': 'tamas-banyai/test_ades_ndvi_query',
        'name': 'tamas-banyai/test_ades_ndvi_query',
        'version': 'v1',
        'abstract': '',
        'inputs': [
            {'name': 'layer_id', 'desc': 'layer_id'},
            {'name': 'field_geojson', 'desc': 'field_geojson'},
            {'name': 'daterange_json', 'desc': 'daterange_json'},
        ],
        'outputs': [
            {'name': 'ndvicube_json', 'desc': 'ndvicube_json'},
        ],
        'executor': 'python_executor.execute_process'
    }
     
    def __init__(self):
        AbstractProcess.__init__(self, self.PROCESS_DESC)