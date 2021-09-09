################################################################################
################################## BASE IMAGE ##################################
################################################################################
FROM continuumio/miniconda3


################################################################################
################################# ENVIRONMENT  #################################
################################################################################

ARG RAPPI_WORKSPACE
# ENV RAPPI_WORKSPACE /home/rappiml
RUN mkdir ${RAPPI_WORKSPACE}

################################################################################
############################# PYTHON DEPENDENCIES  #############################
################################################################################

RUN python -m pip install --upgrade pip
RUN python -m pip install mlflow pymysql cryptography

################################################################################
############################### INSTALL OUR PKG  ###############################
################################################################################

COPY python/utils ${RAPPI_WORKSPACE}/utils

# Install python packages

WORKDIR ${RAPPI_WORKSPACE}/utils
RUN python setup.py bdist_wheel
RUN cp dist/rappiml-0.0.1-py3-none-any.whl ${RAPPI_WORKSPACE}
RUN pip install ${RAPPI_WORKSPACE}/rappiml-0.0.1-py3-none-any.whl

################################################################################
################ COPY DATA AND SCRIPTS TO TRAIN AND SAVE MODEL  ################
################################################################################

RUN mkdir -p ${RAPPI_WORKSPACE}/models/

COPY scripts ${RAPPI_WORKSPACE}/scripts
COPY data ${RAPPI_WORKSPACE}/data
COPY docker/mlflow/config/requirements.txt ${RAPPI_WORKSPACE}/requirements.txt
