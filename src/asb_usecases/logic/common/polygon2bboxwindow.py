import rasterio
from shapely.geometry.geo import shape
from rasterio.crs import CRS
from rasterio.warp import transform
import glob

# returns a standard window [startx,starty,endx,endy]
def compute(searchglob,polygons):
    # get a file with a matching tileid
    ref_file=glob.glob(searchglob, recursive=True)[0]
    with rasterio.open(ref_file) as finp: profile=finp.profile
    # get the portion that the geoms are touching
    bbox=[0,0,profile['width'],profile['height']]
    for igeom in polygons:
        s=shape(igeom['geometry'])
        xy=transform(CRS.from_epsg(4326),profile['crs'],*s.exterior.coords.xy)
        rc=rasterio.transform.rowcol(profile['transform'], *xy)
        bbox=[
            max([bbox[0],min(rc[0])]),
            max([bbox[1],min(rc[1])]),
            min([bbox[2],max(rc[0])]),
            min([bbox[3],max(rc[1])])
        ]
    return bbox
