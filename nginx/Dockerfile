FROM nginx:1.13.5

RUN apt-get update -y && \
apt-get install -y vim && \
apt-get clean

ADD ./conf.d /etc/nginx/conf.d
WORKDIR /etc/nginx
