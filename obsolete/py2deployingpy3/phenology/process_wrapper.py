#!/usr/bin/python

import logging
import pandas
import json

# --------------------------------------------------------------------------------------
# Save this code in file "process_wrapper.py" and adapt as indicated in inline comments.
#
# Notes:
#  - This is a Python 3 script.
#  - The inputs will be given values by name, thus their order has no importance ...
#  - ... except that the inputs with a default value must be listed last.
#  - Parameter names are automatically converted into valid Python variable names.
#  - Any empty line or line starting with a '#' character will be ignored.
# --------------------------------------------------------------------------------------

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PhenologypParams:
    def __init__(self,):
        self.sStart=pandas.DateOffset(months=4, days=2)  # Start date of interval for start of season
        self.sEnd=  pandas.DateOffset(months=6, days=10) # End date of tart interval for start of season
        self.mStart=pandas.DateOffset(months=6, days=10) # Start date of interval for mid of season
        self.mEnd=  pandas.DateOffset(months=9, days=1) # End date of tart interval for mid of season
        self.eStart=pandas.DateOffset(months=9, days=1) # Start date of interval for end of season
        self.eEnd=  pandas.DateOffset(months=12,days=31) # End date of tart interval for end of season
        self.tSos=  10.          # Threshold for start of season
        self.tEos=  10.          # Threshold for end of season


"""
    sStartDate: First date of the interval for getting season start
    sEndDate: Last date of the interval for getting season start

    mStartDate: First date of the interval for getting maximum greenness
    mEndDate: Last date of the interval for getting maximum greenness

    eStartDate: First date of the interval for getting season end
    eEndDate: Last date of the interval for getting season end

    tSos: The offset (%) to add to the start date minimum to set the start of the season
    tEos: The offset (%) to subtract from the end date minimum to set the end of the season
"""
class CropPhenology:

    def __init__(self):
        self.params = ['sos', 'eos']

    def smooth(self, timeseries, method=['Rolling Mean', 'SWETS'], window_size=10):
        smoothed = timeseries.copy()

        if method == 'Rolling Mean':
            smoothed.Greenness = timeseries.Greenness.rolling(window_size, center=True).mean()
        return smoothed


    def extractSeasonDates(self, timeseries, args):

        result = {'sos': {'time': '', 'greenness': ''}, 'eos': {'time': '', 'greenness': ''}}

        if timeseries is None:
            return None
        else:
            year=2019
            
            #timeseries = self.ts.smooth(timeseries, method='Rolling Mean')
            timeseries = self.smooth(timeseries, method='Rolling Mean')
            timeseries.dropna(inplace=True)

            # Get the local maximum greenness
            mMax = self.getLocalMax(timeseries, pandas.Timestamp(year,args.mStart.months,args.mStart.days), pandas.Timestamp(year,args.mEnd.months,args.mEnd.days))
            dmMax = mMax['Times']
            ymMax = mMax['Greenness']

            # Get the start of season dates
            sos = self.getStartOfSeason(timeseries, pandas.Timestamp(year,args.sStart.months,args.sStart.days), pandas.Timestamp(year,args.sEnd.months,args.sEnd.days), float(args.tSos), float(ymMax))
            result['sos']['time'] = sos[3].strftime('%Y-%m-%d')
            result['sos']['greenness'] = sos[2]

            # Get the end of season dates
            eos = self.getEndOfSeason(timeseries, pandas.Timestamp(year,args.eStart.months,args.eStart.days), pandas.Timestamp(year,args.eEnd.months,args.eEnd.days), float(args.tEos), float(ymMax))
            result['eos']['time'] = eos[3].strftime('%Y-%m-%d')
            result['eos']['greenness'] = eos[2]

            return result

    def getLocalMax(self, df, start, end):
        df_range = df.loc[df['Times'].between(start, end)]
        return df_range.loc[df_range['Greenness'].idxmax()]

    """
        Calculate the start of the season based on selected interval [start, end] and a greenness curve (df). 
        Within this interval we will first look for the local minimum greenness, marked by (dsMin, ysMin). In the
        second step we will use the offset (%) to calculate the amount greenness offset that needs to be applied to 
        the minumum value in order to get the start of the season. This offset is calculated as a percentage of the 
        difference between the maximum greenness and the local minimum.
    """

    def getStartOfSeason(self, df, start, end, offset, yMax):
        # Get the local minimum greenness in the start season interval
        df_sRange = df.loc[df['Times'].between(start, end)]
        sMin = df_sRange.loc[df_sRange['Greenness'].idxmin()]
        dsMin = sMin['Times']
        ysMin = sMin['Greenness']

        # Calculate the greenness value corresponding to the start of the season
        ySos = ysMin + ((yMax - ysMin) * (offset / 100.0))

        # Get the closest value to this greenness
        df_sRange = df_sRange.loc[df_sRange['Times'] >= dsMin]
        sos = df_sRange.iloc[(df_sRange['Greenness'] - ySos).abs().argsort()[:1]]
        return (dsMin, ysMin, ySos, pandas.to_datetime(str(sos['Times'].values[0])))

    """
        Calculate the end of the season based on selected interval [start, end] and a greenness curve (df). 
        Within this interval we will first look for the local minimum greenness, marked by (deMin, yeMin). In the
        second step we will use the offset (%) to calculate the amount greenness offset that needs to be applied to 
        the minumum value in order to get the start of the season. This offset is calculated as a percentage of the 
        difference between the maximum greenness and the local minimum.
    """

    def getEndOfSeason(self, df, start, end, offset, yMax):
        # Get the local minimum greenness in the start season interval
        df_eRange = df.loc[df['Times'].between(start, end)]
        eMin = df_eRange.loc[df_eRange['Greenness'].idxmin()]
        deMin = eMin['Times']
        yeMin = eMin['Greenness']

        # Calculate the greenness value corresponding to the start of the season
        yEos = yeMin + ((yMax - yeMin) * (offset / 100.0))

        # Get the closest value to this greenness
        df_eRange = df_eRange.loc[df_eRange['Times'] <= deMin]
        eos = df_eRange.iloc[(df_eRange['Greenness'] - yEos).abs().argsort()[:1]]
        return (deMin, yeMin, yEos, pandas.to_datetime(str(eos['Times'].values[0])))


def execute(out_dir, timeseries_json):
    """
    Inputs:
    timeseries_json -- timeseries_json -- 45/User String

    Outputs:
    phenology_json -- phenology_json -- 45/User String

    Main Dependency:
    mep-wps/uc-bundle-1

    Software Dependencies:
    pywps-4

    Processing Resources:
    ram -- 1
    disk -- 1
    cpu -- 1
    """

    phenology_json = None

    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------

    logger.info("Starting...")


    try:
        params=PhenologypParams()
        ts=json.loads(timeseries_json)
        for iserie in ts['features']:
            timeseries=pandas.DataFrame(
                data={
                    #list(map(lambda x: parse(x['date'], "%Y-%m-%d"), iserie["timeseries"])),
                    'Times':     [pandas.Timestamp(i[0]).tz_convert(None) for i in iserie["timeseries"]],  
                    'Greenness': [                                  i[1]  for i in iserie["timeseries"]] # json loads already converted to float
                }
            )
            cp=CropPhenology()
            iserie['phenology']=cp.extractSeasonDates(timeseries, params)
            del iserie['timeseries']
        phenology_json=json.dumps(ts)
    except Exception as e:
        phenology_json="ERROR + "+str(e)
        raise e

    # ...


    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "phenology_json": phenology_json
    }