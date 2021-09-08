FROM continuumio/miniconda3


ENV RAPPI_WORKSPACE /home/rappiml

RUN mkdir ${RAPPI_WORKSPACE}

RUN python -m pip install --upgrade pip
RUN python -m pip install mlflow pymysql cryptography

COPY python/utils ${RAPPI_WORKSPACE}/utils

# RUN apt update && apt upgrade && apt install -y curl
# RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --output /tmp/Miniconda3-latest-Linux-x86_64.sh
# RUN bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p ${HOME}/miniconda

# Install python packages

WORKDIR ${RAPPI_WORKSPACE}/utils
RUN python setup.py bdist_wheel
RUN cp dist/rappiml-0.0.1-py3-none-any.whl ${RAPPI_WORKSPACE}
RUN pip install ${RAPPI_WORKSPACE}/rappiml-0.0.1-py3-none-any.whl
RUN mkdir -p ${RAPPI_WORKSPACE}/models/

COPY scripts ${RAPPI_WORKSPACE}/scripts
COPY data ${RAPPI_WORKSPACE}/data
COPY docker/mlflow/config/requirements.txt ${RAPPI_WORKSPACE}/requirements.txt
