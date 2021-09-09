# nginx v1.21.1 is the latest at the time of creation of this file
FROM nginx:1.21.1

# Remove default Nginx config
RUN rm /etc/nginx/nginx.conf

# Copy the modified Nginx config
COPY config/nginx.conf /etc/nginx/
# COPY config/mlflow.conf /etc/nginx/sites-enabled/
COPY config/rappiml.conf /etc/nginx/sites-enabled/
