'''
Created on May 5, 2020

@author: banyait
'''
from shapely.geometry.geo import shape
import matplotlib.pyplot as plt

if __name__ == '__main__':
    test={'type': 'Polygon', 'coordinates': [[
        [4.435528732, 51.332782628], 
        [4.445484504, 51.357014747], 
        [4.480426502, 51.441562218], 
        [6.017025009, 51.412342655], 
        [5.953869713, 50.426293661], 
        [4.40871511, 50.455272161], 
        [4.435528732, 51.332782628]
    ]]}
    bla=shape(test)
    bnds=bla.bounds
    plt.plot(*bla.boundary.coords.xy)
    plt.scatter(*bla.boundary.coords.xy)
    plt.show()
    
    print("2HI")