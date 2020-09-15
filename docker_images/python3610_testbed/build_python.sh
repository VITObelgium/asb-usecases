export PYTHON_VERSION=3.6.10
export PYTHON_MAJOR=3
export PYTHON_INSTALL_PATH=$(pwd)

#curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
#tar -xvzf Python-${PYTHON_VERSION}.tgz
#cd Python-${PYTHON_VERSION}
#./configure \
#    --prefix=$PYTHON_INSTALL_PATH \
#    --enable-shared \
#    --enable-optimizations \
#    LDFLAGS=-Wl,--disable-new-dtags
#make -j4
#make install

#curl -O https://bootstrap.pypa.io/get-pip.py
#${PYTHON_INSTALL_PATH}/bin/python${PYTHON_MAJOR} get-pip.py

${PYTHON_INSTALL_PATH}/bin/pip3 install virtualenv
