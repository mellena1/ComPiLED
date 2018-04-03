FROM tobi312/rpi-nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-available/default
COPY default.conf /etc/nginx/conf.d/

EXPOSE 80
EXPOSE 443
