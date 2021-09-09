################################################################################
################################## BASE IMAGE ##################################
################################################################################

# v1.21.1 is the latest at the time of creation of this file
FROM nginx:1.21.1

################################################################################
######################### ADD AND REPLACE CONFIG FILES  ########################
################################################################################

# Remove default Nginx config and copy the new one
RUN rm /etc/nginx/nginx.conf
COPY config/nginx.conf /etc/nginx/

# Copy the RappiML config file (web endpoint)
COPY config/rappiml.conf /etc/nginx/sites-enabled/
