FROM vito-docker-mep-wps.artifactory.vgt.vito.be/asbuserwps.admin/asbwps-py3.6-buster:latest

ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

RUN apt update && apt -y install mc && pip3 install -U openeo
COPY ades_ndvi_query/*.py /asb/user/

#CMD ["python3"]
#CMD ["sleep","infinity"]

#/asb/core
#/asb/etc
#/asb/log
#/asb/requirements
#/asb/run
#
#/asb/user
#/asb/user/process_wrapper.py
#/asb/user/pywps_process.py
#/asb/user/user_process.py
#
#/asb/user/asb_usecases
#/asb/user/parcel
#/asb/user/resources
#/asb/user/resources/__init__.py
#/asb/user/resources/tiles.json
#/asb/user/utils
#
#/asb/wps
#/asb/wps/inputs
#/asb/wps/outputs
#/asb/wps/workdir



