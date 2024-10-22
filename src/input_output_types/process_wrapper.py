#!/usr/bin/python

import logging

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

def execute(out_dir, istring, ibbox, idaterange, iobject):
    """
    Inputs:
    istring -- iString -- 45/User String
    ibbox -- iBBox -- 43/BoundingBox
    idaterange -- iDateRange -- 44/DateRange
    iobject -- iObject -- 95/Object Type

    Outputs:
    ostring -- oString -- 45/User String
    oobject -- oObject -- 95/Object Type
    ocommonformatpicture -- oCommonFormatPicture -- 48/CommonFormatPicture
    odate -- oDate -- 40/Date
    owkt -- oWKT -- 92/WKT String

    Main Dependency:
    mep-wps/uc-bundle-1

    Software Dependencies:
    pywps-4

    Processing Resources:
    ram -- 4
    disk -- 1
    cpu -- 1
    gpu -- 0
    """

    ostring = None
    oobject = None
    ocommonformatpicture = None
    odate = None
    owkt = None

    # ----------------------------------------------------------------------------------
    # Insert your own code below.
    # The files generated by your code must be stored in the "out_dir" folder.
    # Only the content of that folder is persisted in the datastore.
    # Give appropriate values to the output parameters. These will be passed to the next
    # process(es) following the workflow connections.
    # ----------------------------------------------------------------------------------

    logger.info("Starting...")

    # ...


    # ----------------------------------------------------------------------------------
    # The wrapper must return a dictionary that contains the output parameter values.
    # ----------------------------------------------------------------------------------
    return {
        "ostring": ostring,
        "oobject": oobject,
        "ocommonformatpicture": ocommonformatpicture,
        "odate": odate,
        "owkt": owkt
    }