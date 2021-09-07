FROM python:3.9.7-slim-buster


################################################################################
################### Set the environment required by this app ###################
################################################################################

# Default flask port
EXPOSE 5001

# We will store our source code here
ENV APP_DIR /home/rappiml

################################################################################
##################### Copy the source code into the image  #####################
################################################################################

RUN mkdir ${APP_DIR}
COPY . ${APP_DIR}

# ################################################################################
# ################ Install general purpose system-level libraries ################
# ################################################################################

# RUN apt-get update -y && apt-get install -y curl

################################################################################
########## Install system-level libraries for this particular project ##########
################################################################################
WORKDIR ${APP_DIR}

# Install ccapps as a python package so it can be called from anywhere 
RUN python3.9 -m pip install --upgrade pip
RUN python3.9 -m pip install -e .

################################################################################
################## Run the app with the built-in flask server ##################
################################################################################

WORKDIR /
ENV FLASK_APP=rappiml

# ENTRYPOINT [ "flask" ]
# CMD ["run", "-h", "0.0.0.0", "-p" 5001 ]
