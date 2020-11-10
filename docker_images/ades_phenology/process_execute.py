'''
Created on Sep 7, 2020

@author: banyait
'''
import requests

url='https://mep-wps.vgt.vito.be/ades/rest'
job='banyait_ades_test'

if __name__ == '__main__':
    with open('executejob.json') as f:
        execdata=f.read()
    resp=requests.post(
        url+'/processes/'+job+'/jobs',
        data = execdata,
        headers={
            'Content-type': 'application/json'
        }
    )
    print(resp)
    print(resp.json())


