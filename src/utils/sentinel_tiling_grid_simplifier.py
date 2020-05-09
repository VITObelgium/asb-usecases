import json
from shapely.geometry.geo import shape

# PRE STEPS:
# 1.: download https://sentinel.esa.int/documents/247904/1955685/S2A_OPER_GIP_TILPAR_MPC__20151209T095117_V20150622T000000_21000101T000000_B00.kml/ec05e22c-a2bc-4a13-9e84-02d5257b09a8
# 2.: ogr2ogr -skipFailures -f GeoJSON tiles_rich.json S2A_OPER_GIP_TILPAR_MPC__20151209T095117_V20150622T000000_21000101T000000_B00.kml


if __name__ == '__main__':

    tiles={}
    shapes={}
    with open('../resources/tiles_rich.json') as f:
        d=json.load(f)
        for i in d['features']:
            tiles[i['properties']['Name']]=i['geometry']
            shapes[i['properties']['Name']]=shape(i['geometry'])

    with open('../resources/tiles.json','w') as f:
        json.dump(tiles, f)
    
    print("HI")