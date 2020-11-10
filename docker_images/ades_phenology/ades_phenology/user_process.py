from pywps import LiteralInput, LiteralOutput
from asb.wps import WrappedProcess
 
 
class UserProcess(WrappedProcess):
    def __init__(self):
        inputs = [
            LiteralInput("layer_id", "layer_id", data_type="string"),
            LiteralInput("field_geojson", "field_geojson", data_type="string"),
            LiteralInput("daterange_json", "daterange_json", data_type="string"),
        ]
        outputs = [
            LiteralOutput("ndvicube_json", "ndvicube_json", data_type="string"),
        ]
 
        super(UserProcess, self).__init__(
            identifier="tamas-banyai/test_ades_ndvi_query",
            version="v1",
            title="tamas-banyai/test_ades_ndvi_query",
            inputs=inputs,
            outputs=outputs,
        )
