#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
# Note this base image is based on debian
ARG BIMS_TAG=latest
FROM kartoza/kbims_uwsgi:${BIMS_TAG}
MAINTAINER Dimas Ciputra<dimas@kartoza.com>

ARG RBIS_TAG=develop
WORKDIR /usr/src
RUN git clone --depth=1 --branch ${RBIS_TAG} git://github.com/dimasciput/RBIS.git /usr/src/RBIS_BIMS
RUN mkdir -p /usr/src/rbis
RUN cp -r RBIS_BIMS/django_project/* /usr/src/rbis

WORKDIR /usr/src/rbis

ADD uwsgi.conf /usr/src/rbis/uwsgi.conf

CMD ["uwsgi", "--ini", "/usr/src/rbis/uwsgi.conf"]
