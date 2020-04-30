'''
Created on Mar 18, 2020

@author: banyait
'''
from pprint import pprint
from command_runner import process_wrapper

if __name__ == '__main__':
    result=process_wrapper.execute('','env | grep PYTHON')
    print(result)    
