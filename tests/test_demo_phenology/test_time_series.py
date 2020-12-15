import unittest
from demo_phenology.step1_timeseries import process_wrapper
import pprint


class Test(unittest.TestCase):

    def testTimeSeries(self):
        test_fields='{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[5.014834,51.234689],[5.01518,51.231222],[5.019777,51.229975],[5.020372,51.231445],[5.020372,51.231445],[5.022222,51.231269],[5.023174,51.234371],[5.014834,51.234689]]]}},{"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[5.498312,51.130314],[5.496896,51.130537],[5.49671,51.130149],[5.497791,51.129982],[5.498962,51.129803],[5.498995,51.129925],[5.498998,51.129933],[5.498928,51.129943],[5.498639,51.130263],[5.498366,51.130305],[5.49836,51.130278],[5.498329,51.130282],[5.498327,51.130275],[5.498309,51.130278],[5.498312,51.130314]]]},"properties":{}}]}'
        test_daterange='{"start": "2019-01-01", "end": "2019-12-31"}'
        test_layer_id="TERRASCOPE_S2_FAPAR_V2"
        test_result='{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {}, "timeseries": [["2019-01-06T00:00:00Z", 50.714285714285715], ["2019-01-13T00:00:00Z", 42.25], ["2019-01-21T00:00:00Z", 117.79816513761467], ["2019-02-07T00:00:00Z", 50.169736842105266], ["2019-02-12T00:00:00Z", 26.2], ["2019-02-15T00:00:00Z", 115.42468239564428], ["2019-02-25T00:00:00Z", 105.96597096188748], ["2019-02-27T00:00:00Z", 103.92649727767694], ["2019-03-07T00:00:00Z", 74.18689581095596], ["2019-03-17T00:00:00Z", 40.23974255832663], ["2019-03-22T00:00:00Z", 98.23003629764065], ["2019-03-29T00:00:00Z", 95.75862068965517], ["2019-04-01T00:00:00Z", 96.43647912885662], ["2019-04-11T00:00:00Z", 66.49850597609561], ["2019-04-13T00:00:00Z", 71.16666666666667], ["2019-04-16T00:00:00Z", 40.37174721189591], ["2019-04-18T00:00:00Z", 60.577586206896555], ["2019-04-21T00:00:00Z", 56.60889292196007], ["2019-05-11T00:00:00Z", 30.54063926940639], ["2019-05-13T00:00:00Z", 37.137023593466424], ["2019-05-18T00:00:00Z", 34.327132486388386], ["2019-05-23T00:00:00Z", 32.5], ["2019-06-07T00:00:00Z", 66.55036297640653], ["2019-06-17T00:00:00Z", 102.76860254083485], ["2019-06-22T00:00:00Z", 98.4530844997408], ["2019-06-27T00:00:00Z", 140.97640653357533], ["2019-06-30T00:00:00Z", 114.56591974986972], ["2019-07-02T00:00:00Z", 52.09803921568628], ["2019-07-05T00:00:00Z", 83.19514388489209], ["2019-07-07T00:00:00Z", 151.13453389830508], ["2019-07-17T00:00:00Z", 130.62822384428225], ["2019-07-20T00:00:00Z", 175.51769509981852], ["2019-07-25T00:00:00Z", 153.71778584392015], ["2019-07-30T00:00:00Z", 141.33803479078514], ["2019-08-01T00:00:00Z", 66.42391304347827], ["2019-08-04T00:00:00Z", 159.09981851179674], ["2019-08-19T00:00:00Z", 112.12130479102956], ["2019-08-21T00:00:00Z", 165.9193302891933], ["2019-08-24T00:00:00Z", 167.6592558983666], ["2019-08-26T00:00:00Z", 158.94963702359345], ["2019-08-31T00:00:00Z", 147.4959165154265], ["2019-09-05T00:00:00Z", 116.62740384615384], ["2019-09-08T00:00:00Z", 112.82074613284804], ["2019-09-10T00:00:00Z", 153.8448275862069], ["2019-09-15T00:00:00Z", 144.7872050816697], ["2019-09-18T00:00:00Z", 133.91152450090743], ["2019-09-20T00:00:00Z", 132.30326876513317], ["2019-10-10T00:00:00Z", 59.437252311756936], ["2019-10-13T00:00:00Z", 60.991833030852995], ["2019-10-18T00:00:00Z", 100.42288557213931], ["2019-10-23T00:00:00Z", 48.87477313974592], ["2019-10-28T00:00:00Z", 46.24500907441016], ["2019-11-02T00:00:00Z", 33.28503562945368], ["2019-11-09T00:00:00Z", 46.2228181374939], ["2019-11-19T00:00:00Z", 36.236092265943014], ["2019-11-22T00:00:00Z", 62.15448275862069], ["2019-11-29T00:00:00Z", 36.58711433756806], ["2019-12-04T00:00:00Z", 64.37522686025409], ["2019-12-09T00:00:00Z", 49.85386996904025], ["2019-12-12T00:00:00Z", 63.50984883188273], ["2019-12-14T00:00:00Z", 21.357142857142858], ["2019-12-24T00:00:00Z", 30.263297872340427], ["2019-12-27T00:00:00Z", 1.36328125], ["2019-12-29T00:00:00Z", 55.01179673321234]]}, {"type": "Feature", "properties": {}, "timeseries": [["2019-01-21T00:00:00Z", 116.0909090909091], ["2019-02-15T00:00:00Z", 105.78787878787878], ["2019-02-25T00:00:00Z", 96.21212121212122], ["2019-02-27T00:00:00Z", 104.18181818181819], ["2019-03-07T00:00:00Z", 18.803030303030305], ["2019-03-17T00:00:00Z", 39.0], ["2019-03-19T00:00:00Z", 117.16666666666667], ["2019-03-22T00:00:00Z", 45.333333333333336], ["2019-03-29T00:00:00Z", 48.303030303030305], ["2019-04-01T00:00:00Z", 46.59090909090909], ["2019-04-11T00:00:00Z", 36.36363636363637], ["2019-04-13T00:00:00Z", 41.58064516129032], ["2019-04-16T00:00:00Z", 29.545454545454547], ["2019-04-18T00:00:00Z", 36.25757575757576], ["2019-04-21T00:00:00Z", 38.696969696969695], ["2019-05-11T00:00:00Z", 28.714285714285715], ["2019-05-13T00:00:00Z", 52.333333333333336], ["2019-05-16T00:00:00Z", 50.696969696969695], ["2019-05-18T00:00:00Z", 59.40909090909091], ["2019-05-31T00:00:00Z", 43.90909090909091], ["2019-06-07T00:00:00Z", 135.0], ["2019-06-17T00:00:00Z", 164.56060606060606], ["2019-06-22T00:00:00Z", 164.27272727272728], ["2019-06-27T00:00:00Z", 152.66666666666666], ["2019-07-05T00:00:00Z", 90.4090909090909], ["2019-07-07T00:00:00Z", 105.5909090909091], ["2019-07-17T00:00:00Z", 108.0909090909091], ["2019-07-25T00:00:00Z", 87.72727272727273], ["2019-07-30T00:00:00Z", 93.77272727272727], ["2019-08-04T00:00:00Z", 92.63636363636364], ["2019-08-14T00:00:00Z", 106.71212121212122], ["2019-08-19T00:00:00Z", 122.0], ["2019-08-21T00:00:00Z", 110.62121212121212], ["2019-08-24T00:00:00Z", 113.5909090909091], ["2019-08-26T00:00:00Z", 114.68181818181819], ["2019-08-29T00:00:00Z", 74.84210526315789], ["2019-08-31T00:00:00Z", 108.16666666666667], ["2019-09-10T00:00:00Z", 120.54545454545455], ["2019-09-15T00:00:00Z", 117.92424242424242], ["2019-09-20T00:00:00Z", 118.34848484848484], ["2019-09-28T00:00:00Z", 125.47058823529412], ["2019-10-23T00:00:00Z", 119.43939393939394], ["2019-10-28T00:00:00Z", 145.28787878787878], ["2019-11-12T00:00:00Z", 0.4642857142857143], ["2019-11-19T00:00:00Z", 78.16666666666667], ["2019-12-02T00:00:00Z", 30.0], ["2019-12-04T00:00:00Z", 36.431372549019606], ["2019-12-12T00:00:00Z", 75.51515151515152], ["2019-12-27T00:00:00Z", 20.5], ["2019-12-29T00:00:00Z", 36.583333333333336]]}]}'
        test_layer_id_old="S2_FAPAR_V102_WEBMERCATOR2"
        test_result_old='{"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {}, "timeseries": [["2019-01-03T00:00:00Z", 45.93333333333333], ["2019-01-21T00:00:00Z", 115.94790636333663], ["2019-01-23T00:00:00Z", 61.02498048399688], ["2019-02-07T00:00:00Z", 50.20284237726098], ["2019-02-12T00:00:00Z", 32.18518518518518], ["2019-02-15T00:00:00Z", 114.49910583644936], ["2019-02-17T00:00:00Z", 88.12661119269049], ["2019-02-20T00:00:00Z", 73.30954316371322], ["2019-02-25T00:00:00Z", 105.76296537148431], ["2019-02-27T00:00:00Z", 104.14046496504633], ["2019-03-07T00:00:00Z", 70.39752252252252], ["2019-03-17T00:00:00Z", 43.74183976261128], ["2019-03-22T00:00:00Z", 97.84100146317672], ["2019-03-29T00:00:00Z", 100.43976589172492], ["2019-04-01T00:00:00Z", 96.74930905543815], ["2019-04-11T00:00:00Z", 71.78069732187974], ["2019-04-13T00:00:00Z", 61.4141689373297], ["2019-04-16T00:00:00Z", 61.46902942610958], ["2019-04-18T00:00:00Z", 64.50268249065192], ["2019-04-21T00:00:00Z", 62.39587059014794], ["2019-05-11T00:00:00Z", 38.67307066102247], ["2019-05-13T00:00:00Z", 42.63111689156235], ["2019-05-18T00:00:00Z", 48.43992846691595], ["2019-05-23T00:00:00Z", 42.38790440578768], ["2019-06-02T00:00:00Z", 47.0], ["2019-06-07T00:00:00Z", 72.59535034953666], ["2019-06-17T00:00:00Z", 105.39018045846204], ["2019-06-22T00:00:00Z", 105.47657270860556], ["2019-06-25T00:00:00Z", 90.40237359778898], ["2019-06-27T00:00:00Z", 141.2609331815965], ["2019-06-30T00:00:00Z", 115.3689429373246], ["2019-07-02T00:00:00Z", 58.62799263351749], ["2019-07-05T00:00:00Z", 84.72730352303523], ["2019-07-07T00:00:00Z", 150.58364661654136], ["2019-07-17T00:00:00Z", 128.90083798882682], ["2019-07-20T00:00:00Z", 172.19200130060153], ["2019-07-22T00:00:00Z", 145.0137008644593], ["2019-07-25T00:00:00Z", 153.7006990733214], ["2019-07-30T00:00:00Z", 139.41185384744907], ["2019-08-01T00:00:00Z", 65.65289256198348], ["2019-08-04T00:00:00Z", 153.60299138351488], ["2019-08-06T00:00:00Z", 74.7966573816156], ["2019-08-16T00:00:00Z", 101.84469952734639], ["2019-08-19T00:00:00Z", 115.61766809728184], ["2019-08-21T00:00:00Z", 164.1795560329395], ["2019-08-24T00:00:00Z", 168.09201755812063], ["2019-08-26T00:00:00Z", 148.2420744594375], ["2019-08-31T00:00:00Z", 144.79206633067793], ["2019-09-05T00:00:00Z", 93.9257191927866], ["2019-09-08T00:00:00Z", 110.06124776022153], ["2019-09-10T00:00:00Z", 149.2931230694196], ["2019-09-13T00:00:00Z", 51.32983794089609], ["2019-09-15T00:00:00Z", 143.8649000162575], ["2019-09-18T00:00:00Z", 138.90278003576654], ["2019-09-20T00:00:00Z", 128.0899040806373], ["2019-10-10T00:00:00Z", 62.836715431807455], ["2019-10-13T00:00:00Z", 59.82051698910746], ["2019-10-18T00:00:00Z", 99.32223222322233], ["2019-10-23T00:00:00Z", 53.97301251828971], ["2019-10-25T00:00:00Z", 38.355226792391484], ["2019-10-28T00:00:00Z", 47.64265973012518], ["2019-11-02T00:00:00Z", 32.613454466796455], ["2019-11-09T00:00:00Z", 48.17623451404641], ["2019-11-17T00:00:00Z", 43.32734761120263], ["2019-11-19T00:00:00Z", 37.917993246502654], ["2019-11-22T00:00:00Z", 63.96426218708827], ["2019-11-29T00:00:00Z", 41.828320598276704], ["2019-12-04T00:00:00Z", 69.64217200455211], ["2019-12-09T00:00:00Z", 29.949291914116035], ["2019-12-12T00:00:00Z", 66.60758247168883], ["2019-12-14T00:00:00Z", 44.833333333333336], ["2019-12-17T00:00:00Z", 75.9188894937398], ["2019-12-24T00:00:00Z", 30.370558375634516], ["2019-12-27T00:00:00Z", 7.951923076923077], ["2019-12-29T00:00:00Z", 58.842302064704924]]}, {"type": "Feature", "properties": {}, "timeseries": [["2019-01-21T00:00:00Z", 95.67469879518072], ["2019-02-15T00:00:00Z", 108.42391304347827], ["2019-02-17T00:00:00Z", 87.40760869565217], ["2019-02-25T00:00:00Z", 98.91304347826087], ["2019-02-27T00:00:00Z", 102.95108695652173], ["2019-03-07T00:00:00Z", 19.64673913043478], ["2019-03-17T00:00:00Z", 35.833333333333336], ["2019-03-19T00:00:00Z", 115.2336956521739], ["2019-03-22T00:00:00Z", 50.17391304347826], ["2019-03-24T00:00:00Z", 49.255434782608695], ["2019-03-29T00:00:00Z", 51.5], ["2019-04-01T00:00:00Z", 48.15217391304348], ["2019-04-11T00:00:00Z", 46.04347826086956], ["2019-04-13T00:00:00Z", 42.08522727272727], ["2019-04-16T00:00:00Z", 37.95108695652174], ["2019-04-18T00:00:00Z", 28.51086956521739], ["2019-04-21T00:00:00Z", 40.90760869565217], ["2019-05-11T00:00:00Z", 35.411764705882355], ["2019-05-13T00:00:00Z", 44.05434782608695], ["2019-05-16T00:00:00Z", 54.93478260869565], ["2019-05-18T00:00:00Z", 58.15217391304348], ["2019-05-31T00:00:00Z", 50.62068965517241], ["2019-06-07T00:00:00Z", 129.69565217391303], ["2019-06-17T00:00:00Z", 158.79891304347825], ["2019-06-22T00:00:00Z", 162.45108695652175], ["2019-06-27T00:00:00Z", 146.27173913043478], ["2019-07-05T00:00:00Z", 93.3905325443787], ["2019-07-07T00:00:00Z", 103.92934782608695], ["2019-07-17T00:00:00Z", 104.9836956521739], ["2019-07-22T00:00:00Z", 102.07608695652173], ["2019-07-25T00:00:00Z", 91.91304347826087], ["2019-07-30T00:00:00Z", 93.67391304347827], ["2019-08-04T00:00:00Z", 101.375], ["2019-08-14T00:00:00Z", 115.15760869565217], ["2019-08-19T00:00:00Z", 124.61413043478261], ["2019-08-21T00:00:00Z", 117.28804347826087], ["2019-08-24T00:00:00Z", 117.83695652173913], ["2019-08-26T00:00:00Z", 110.07065217391305], ["2019-08-29T00:00:00Z", 75.58], ["2019-08-31T00:00:00Z", 112.67934782608695], ["2019-09-10T00:00:00Z", 114.67934782608695], ["2019-09-15T00:00:00Z", 114.90760869565217], ["2019-09-20T00:00:00Z", 114.32065217391305], ["2019-09-28T00:00:00Z", 62.024193548387096], ["2019-10-13T00:00:00Z", 88.1304347826087], ["2019-10-23T00:00:00Z", 107.7554347826087], ["2019-10-28T00:00:00Z", 137.42934782608697], ["2019-11-04T00:00:00Z", 34.880434782608695], ["2019-11-19T00:00:00Z", 69.34239130434783], ["2019-11-22T00:00:00Z", 107.1413043478261], ["2019-12-02T00:00:00Z", 28.619718309859156], ["2019-12-04T00:00:00Z", 40.7410071942446], ["2019-12-09T00:00:00Z", 46.46195652173913], ["2019-12-12T00:00:00Z", 77.50549450549451], ["2019-12-19T00:00:00Z", 95.6086956521739], ["2019-12-27T00:00:00Z", 23.53211009174312], ["2019-12-29T00:00:00Z", 39.34586466165413]]}]}'

        output=process_wrapper.execute('', test_layer_id, test_fields, test_daterange)
        print(output)
        pprint.pprint(output)
        
        self.assertEqual(output['time_series'],test_result)
