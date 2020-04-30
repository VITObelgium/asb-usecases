#!/usr/bin/env python3
from setuptools import setup, find_packages
import tarfile
import os
import sys
import subprocess
import glob

# # initial config
# parcel_dir='../parcel'
# currcwd=os.getcwd()
# 
# # build and get parcel
# os.chdir(parcel_dir)
# subprocess.call('{} setup.py {}'.format(sys.executable,' '.join(sys.argv[1:])), shell=True)
# os.chdir(currcwd)

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

# # create tar.gz 
# tar = tarfile.open("dist/asb-collection.tar.gz", "w:gz")
# fparcel=glob.glob(parcel_dir+'/dist/parcel-*.whl')[0]
# print('Adding '+fparcel)
# tar.add(fparcel)
# 
# tar.add(glob.glob('dist/asb_usecases-*.whl')[0])
# 
# tar.close()
