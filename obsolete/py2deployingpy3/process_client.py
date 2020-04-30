'''
Created on Mar 22, 2020

@author: banyait
'''
import sys
import importlib
import base64
import json

if __name__ == '__main__':
    wrapped_lib=importlib.import_module(sys.argv[1])
    arglist=json.loads(base64.b64decode(sys.argv[2]))
    retval=wrapped_lib.execute(*[i[1] for i in arglist])
    retlist=base64.b64encode(json.dumps(retval).encode()).decode()
    print('RETURN_VALUE_STRING='+retlist)