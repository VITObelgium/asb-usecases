import unittest
import requests
import json

url='https://mep-wps.vgt.vito.be/ades/rest'
#url='http://mep-wps01.vgt.vito.be/ades/rest'

class TestADES(unittest.TestCase):

    def test01Home(self):
        resp=requests.get(url)
        print(resp)
        print(json.dumps(resp.json(),indent=2))

    def test02API(self):
        resp=requests.get(url+'/api')
        print(resp)
        #print(json.dumps(resp.json(),indent=2))

    def test03Conformance(self):
        resp=requests.get(url+'/conformance')
        print(resp)
        print(json.dumps(resp.json(),indent=2))

    def test04GetProcesses(self):
        resp=requests.get(url+'/processes')
        print(resp)
        print(json.dumps(resp.json(),indent=2))
        
    def test05GetJobs(self):
        resp=requests.get(url+'/processes')
        processes=resp.json()
        for i in processes:
            ijob=requests.get(url+'/processes/'+i["id"]+'/jobs')
            print(ijob)
            print(json.dumps(ijob.json(),indent=2))        

