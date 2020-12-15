import requests

url='https://mep-wps.vgt.vito.be/ades/rest'

if __name__ == '__main__':
    with open('deployprocess.json') as f:
        deploydata=f.read()
    resp=requests.post(
        url+'/processes',
        data = deploydata,
        headers={
            'Content-type': 'application/json'
        }
    )
    print(resp)
    print(resp.json())

