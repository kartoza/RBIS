#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
# Note this base image is based on debian
FROM kartoza/kbims_uwsgi:latest
MAINTAINER Dimas Ciputra<dimas@kartoza.com>

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ADD uwsgi.conf /home/web/uwsgi.conf
