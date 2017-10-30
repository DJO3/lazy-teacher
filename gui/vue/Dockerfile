FROM node:8.7.0

ADD ./ /usr/local/lazy-teacher

RUN apt-get update -y && \
apt-get install -y vim && \
apt-get clean && \
useradd -ms /bin/bash soda && \
chown -R soda /usr/local/lazy-teacher

USER soda
RUN cd /usr/local/lazy-teacher && npm install
WORKDIR /usr/local/lazy-teacher
