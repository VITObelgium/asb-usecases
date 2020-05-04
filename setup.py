#!/usr/bin/env python3
from setuptools import setup, find_packages
import tarfile
import os
import sys
import subprocess
import glob
import zipfile
import io

# initial config
parcel_dir='../parcel'
currcwd=os.getcwd()
  
# build and get parcel
os.chdir(parcel_dir)
subprocess.call('{} setup.py {}'.format(sys.executable,' '.join(sys.argv[1:])), shell=True)
os.chdir(currcwd)
 
#build this
tests_require = ['pytest']
setup(
    name='asb-usecases',
    version='0.0.1',
    author='Tamas Banyai',
    author_email='tamas.banyai@vito.be',
    description='Codebase for ASB/MEP-WPS',
    url='https://git.vito.be/scm/biggeo/asb-usecases',
    include_package_data=True,
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    package_data={
        'resources': []
    },
    setup_requires=['pytest-runner', 'wheel'],
    install_requires=[
    ],
    tests_require=tests_require,
    test_suite='tests'
)

# create tar.gz by concatenating the wheels
fparcel=sorted(glob.glob(parcel_dir+'/dist/parcel-*.whl'))[-1]
print(fparcel)
fasbuse=sorted(glob.glob('dist/asb_usecases-*.whl'))[-1]
print(fasbuse)
with tarfile.open('dist/asb_codes.tar.gz', mode="w:gz") as dest:
    files={}
    zparcel=zipfile.ZipFile(fparcel)
    for i in zparcel.namelist(): files[i]=zparcel 
    zasbuse=zipfile.ZipFile(fasbuse)
    for i in zasbuse.namelist(): files[i]=zasbuse 
    for ifile,iarchive in files.items():
        b=iarchive.read(ifile)
        t=tarfile.TarInfo(ifile)
        t.size=len(b)
        dest.addfile(t,io.BytesIO(b))        
    zparcel.close()
    zasbuse.close()

print('FINISHED')

