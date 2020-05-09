import sys

if sys.version_info.minor<7:
    from importlib_resources import path
else:
    from importlib.resources import path

import resources

def tiles_json_path():
    file=path(resources, 'tiles.json')
    #third_party_api_requiring_file_system_path(maskfile)
    return file
