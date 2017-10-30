FROM python:3.6.2

RUN apt-get update -y && \
apt-get install -y vim && \
apt-get clean && \
useradd -ms /bin/bash soda

USER soda
ADD ./ /usr/local/lazy-teacher
WORKDIR /usr/local/lazy-teacher

ENV WORKON_HOME=~/.virtualenvs
ENV PROJECT_HOME=~/Devel

RUN pip install --user -r requirements.txt
