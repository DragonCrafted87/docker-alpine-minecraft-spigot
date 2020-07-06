FROM dragoncrafted87/alpine:latest

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="DragonCrafted87 Alpine Supervisord" \
      org.label-schema.description="Alpine Image with additional controls from supervisord to enable gracefull server shudown." \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/DragonCrafted87/docker-alpine-supervisord" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

COPY root/. /

RUN apk add --no-cache --update \
    git \
    openjdk8-jre \
    tini && \
    pip3 --no-cache-dir install mcrcon && \
    rm  -rf /tmp/* /var/cache/apk/* && \
    mkdir /minecraft && \
    chmod +x -R /scripts/*

ENV SPIGOT_VERSION latest
