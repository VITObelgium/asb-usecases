#!/usr/bin/python

import logging
import os
import json
import io
import uuid

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
stream = io.StringIO()
handler = logging.StreamHandler(stream)
logger.addHandler(handler)

max_cpu=8

def execute(out_dir, collection_dir, models_dir, tilesAndShapes_json, daterange_json):
    """
    Inputs:
    collection_dir -- collection_dir -- 45/User String
    models_dir -- models_dir -- 45/User String
    tilesAndShapes_json -- tilesAndShapes_json -- 45/User String
    daterange_json -- daterange_json -- 45/User String

    Outputs:
    segmentedfiles_json -- segmentedfiles_json -- 45/User String
    exceptionLog -- exceptionLog -- 45/User String

    Main Dependency:
    mep-wps/uc-bundle-1

    Software Dependencies:
    pywps-4

    Processing Resources:
    ram -- 15
    disk -- 10
    cpu -- 8
    """
    
    segmentedfiles_json = None
    exceptionLog=None
    
    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------
        
    try: 
        logger.info("Starting...")
        out_dir=os.path.join('/'.join(models_dir.split('/')[:-1]),'output',str(uuid.uuid4().hex))
        os.makedirs(out_dir,exist_ok=True)
        logger.info("Overriding out_dir to "+str(out_dir))
        logger.info("Contents of out_dir: "+str(os.listdir(path=str(out_dir))))

        #os.environ['JAVA_HOME']='/usr/local/jre'
        #os.environ['JRE_HOME']='/usr/local/jre'

        ncpu=1
        import subprocess
        try: ncpu=int(subprocess.check_output("/usr/bin/nproc"))
        except: pass
        if ncpu>max_cpu: ncpu=max_cpu
        logger.info("Using {} cores".format(str(ncpu)))
                        
        logger.info("Loading dependencies...")

        #sys.path.append('/data/public/banyait/code')
        from parcel.feature.segmentation.segmentation_filebased import main_segmentation
        from asb_usecases.logic.common import polygon2bboxwindow
    
        logger.info("Loading input jsons...")

        tilesAndShapes=json.loads(tilesAndShapes_json)
        daterange=json.loads(daterange_json)

        logger.info("Computing...")

        segmentedfiles=[]
        for i in range(len(tilesAndShapes)):
            workdir=os.path.join(str(out_dir),str(i))
            #workdir=os.path.join(models_dir,str(i))
            os.makedirs(workdir,exist_ok=True)
            iresults={}
            for tile,shape in tilesAndShapes[i].items():
                # TODO this needs to be merged with segmentation, not to glob twice
                bbox=polygon2bboxwindow.compute(collection_dir+'/*/01/*/*'+tile+'*/**/*'+tile+'*.tif', shape)
                outimg=main_segmentation(
                    imgdir=collection_dir,
                    maskdir=os.path.join(models_dir,'convmasks10m'),
                    modeldir=os.path.join(models_dir,'models'),
                    outdir=workdir,
                    tiles=tile,
                    startdate=daterange['start'],
                    enddate=daterange['end'],
                    maxcloudcover=int(100),
                    bbox=bbox,
                    #nwindowspermodel=5,
                    ncpu=ncpu
                )
                iresults[tile]=outimg
            segmentedfiles.append(iresults)
        
        logger.info("Contents of out_dir: "+str(os.listdir(path=str(out_dir))))
        logger.info("Dumping results into json...")
        
        segmentedfiles_json=json.dumps(segmentedfiles)

        logger.info("Finished...")

    except Exception as e:
        logger.exception("Exception in wrapper.")
        
    logging.shutdown()
    stream.flush()
    exceptionLog=stream.getvalue()

    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "segmentedfiles_json": segmentedfiles_json,
        "exceptionLog": exceptionLog
    }