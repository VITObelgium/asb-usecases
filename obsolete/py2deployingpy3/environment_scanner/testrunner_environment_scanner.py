'''
Created on Mar 18, 2020

@author: banyait
'''
from pprint import pprint
from environment_scanner import process_wrapper

if __name__ == '__main__':
    result=process_wrapper.execute('','')
    print(result)    
    pprint(result)
