'''
Created on Mar 18, 2020

@author: banyait
'''
from phenology import process_wrapper
from pprint import pprint

timeseries_json='{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {}, "timeseries": [["2019-01-21T00:00:00Z", 178.1605415860735], ["2019-02-07T00:00:00Z", 14.970684039087947], ["2019-02-15T00:00:00Z", 181.52702702702703], ["2019-02-17T00:00:00Z", 153.71042471042472], ["2019-02-25T00:00:00Z", 174.86486486486487], ["2019-02-27T00:00:00Z", 175.90733590733592], ["2019-03-07T00:00:00Z", 31.329457364341085], ["2019-03-17T00:00:00Z", 167.64478764478764], ["2019-03-19T00:00:00Z", 168.0791505791506], ["2019-03-22T00:00:00Z", 169.77606177606177], ["2019-03-24T00:00:00Z", 166.2934362934363], ["2019-03-29T00:00:00Z", 172.82239382239382], ["2019-04-01T00:00:00Z", 173.34169884169884], ["2019-04-11T00:00:00Z", 187.5772200772201], ["2019-04-16T00:00:00Z", 176.98262548262548], ["2019-04-18T00:00:00Z", 183.04054054054055], ["2019-04-21T00:00:00Z", 150.32239382239382], ["2019-05-11T00:00:00Z", 44.05813953488372], ["2019-05-13T00:00:00Z", 30.405405405405407], ["2019-05-16T00:00:00Z", 47.05960264900662], ["2019-05-18T00:00:00Z", 45.26447876447877], ["2019-06-07T00:00:00Z", 72.45752895752896], ["2019-06-10T00:00:00Z", 57.05035971223022], ["2019-06-17T00:00:00Z", 66.63706563706563], ["2019-06-22T00:00:00Z", 66.91698841698842], ["2019-06-27T00:00:00Z", 65.93629343629344], ["2019-07-05T00:00:00Z", 96.62548262548262], ["2019-07-07T00:00:00Z", 85.34169884169884], ["2019-07-17T00:00:00Z", 136.45366795366795], ["2019-07-22T00:00:00Z", 146.4903474903475], ["2019-07-25T00:00:00Z", 134.5057915057915], ["2019-07-30T00:00:00Z", 156.007722007722], ["2019-08-04T00:00:00Z", 162.26640926640925], ["2019-08-14T00:00:00Z", 169.67760617760618], ["2019-08-16T00:00:00Z", 73.43346774193549], ["2019-08-19T00:00:00Z", 171.14671814671814], ["2019-08-21T00:00:00Z", 164.63320463320463], ["2019-08-24T00:00:00Z", 165.64671814671814], ["2019-08-26T00:00:00Z", 148.47683397683397], ["2019-08-29T00:00:00Z", 101.97598253275109], ["2019-08-31T00:00:00Z", 151.23938223938225], ["2019-09-10T00:00:00Z", 151.1119691119691], ["2019-09-15T00:00:00Z", 139.67374517374517], ["2019-09-20T00:00:00Z", 130.7953667953668], ["2019-09-28T00:00:00Z", 62.56115107913669], ["2019-10-10T00:00:00Z", 21.428571428571427], ["2019-10-13T00:00:00Z", 43.295366795366796], ["2019-10-23T00:00:00Z", 44.955598455598455], ["2019-10-25T00:00:00Z", 44.411764705882355], ["2019-10-28T00:00:00Z", 53.445945945945944], ["2019-11-04T00:00:00Z", 32.46666666666667], ["2019-11-19T00:00:00Z", 60.447876447876446], ["2019-11-22T00:00:00Z", 61.51544401544402], ["2019-12-02T00:00:00Z", 22.64957264957265], ["2019-12-04T00:00:00Z", 33.0], ["2019-12-09T00:00:00Z", 54.71313672922252], ["2019-12-12T00:00:00Z", 54.75], ["2019-12-14T00:00:00Z", 61.0], ["2019-12-19T00:00:00Z", 70.97683397683397], ["2019-12-24T00:00:00Z", 29.266666666666666], ["2019-12-27T00:00:00Z", 19.0], ["2019-12-29T00:00:00Z", 35.888888888888886]]}, {"type": "Feature", "properties": {}, "timeseries": [["2019-01-21T00:00:00Z", 95.67469879518072], ["2019-02-15T00:00:00Z", 108.42391304347827], ["2019-02-17T00:00:00Z", 87.40760869565217], ["2019-02-25T00:00:00Z", 98.91304347826087], ["2019-02-27T00:00:00Z", 102.95108695652173], ["2019-03-07T00:00:00Z", 19.64673913043478], ["2019-03-17T00:00:00Z", 35.833333333333336], ["2019-03-19T00:00:00Z", 115.2336956521739], ["2019-03-22T00:00:00Z", 50.17391304347826], ["2019-03-24T00:00:00Z", 49.255434782608695], ["2019-03-29T00:00:00Z", 51.5], ["2019-04-01T00:00:00Z", 48.15217391304348], ["2019-04-11T00:00:00Z", 46.04347826086956], ["2019-04-13T00:00:00Z", 42.08522727272727], ["2019-04-16T00:00:00Z", 37.95108695652174], ["2019-04-18T00:00:00Z", 28.51086956521739], ["2019-04-21T00:00:00Z", 40.90760869565217], ["2019-05-11T00:00:00Z", 35.411764705882355], ["2019-05-13T00:00:00Z", 44.05434782608695], ["2019-05-16T00:00:00Z", 54.93478260869565], ["2019-05-18T00:00:00Z", 58.15217391304348], ["2019-05-31T00:00:00Z", 50.62068965517241], ["2019-06-07T00:00:00Z", 129.69565217391303], ["2019-06-17T00:00:00Z", 158.79891304347825], ["2019-06-22T00:00:00Z", 162.45108695652175], ["2019-06-27T00:00:00Z", 146.27173913043478], ["2019-07-05T00:00:00Z", 93.3905325443787], ["2019-07-07T00:00:00Z", 103.92934782608695], ["2019-07-17T00:00:00Z", 104.9836956521739], ["2019-07-22T00:00:00Z", 102.07608695652173], ["2019-07-25T00:00:00Z", 91.91304347826087], ["2019-07-30T00:00:00Z", 93.67391304347827], ["2019-08-04T00:00:00Z", 101.375], ["2019-08-14T00:00:00Z", 115.15760869565217], ["2019-08-19T00:00:00Z", 124.61413043478261], ["2019-08-21T00:00:00Z", 117.28804347826087], ["2019-08-24T00:00:00Z", 117.83695652173913], ["2019-08-26T00:00:00Z", 110.07065217391305], ["2019-08-29T00:00:00Z", 75.58], ["2019-08-31T00:00:00Z", 112.67934782608695], ["2019-09-10T00:00:00Z", 114.67934782608695], ["2019-09-15T00:00:00Z", 114.90760869565217], ["2019-09-20T00:00:00Z", 114.32065217391305], ["2019-09-28T00:00:00Z", 62.024193548387096], ["2019-10-13T00:00:00Z", 88.1304347826087], ["2019-10-23T00:00:00Z", 107.7554347826087], ["2019-10-28T00:00:00Z", 137.42934782608697], ["2019-11-04T00:00:00Z", 34.880434782608695], ["2019-11-19T00:00:00Z", 69.34239130434783], ["2019-11-22T00:00:00Z", 107.1413043478261], ["2019-12-02T00:00:00Z", 28.619718309859156], ["2019-12-04T00:00:00Z", 40.7410071942446], ["2019-12-09T00:00:00Z", 46.46195652173913], ["2019-12-12T00:00:00Z", 77.50549450549451], ["2019-12-19T00:00:00Z", 95.6086956521739], ["2019-12-27T00:00:00Z", 23.53211009174312], ["2019-12-29T00:00:00Z", 39.34586466165413]]}]}'

if __name__ == '__main__':
    result=process_wrapper.execute('', timeseries_json)
    print(result)    
    pprint(result)
