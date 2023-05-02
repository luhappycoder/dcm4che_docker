
FROM ubuntu:lunar

ARG DCM4CHE_VERSION

COPY ./*.py /
COPY ./*.txt /

RUN echo $DCM4CHE_VERSION

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    sudo \
    wget \
    zip \
    unzip \
    openssh-client

#RUN pip install -U pip setuptools

#needed when install dcm4che
RUN apt-get install -y default-jre

#install dcm4che
ENV DEBIAN_FRONTEND=noninteractive
RUN python3 install_dcm4che.py /opt
RUN rm /*.py

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PATH=/opt/dcm4che-${DCM4CHE_VERSION}/bin:$PATH

#########
#fix error if run the singuairity image on graham:
#   Error occurred during initialization of VM
#   java.lang.OutOfMemoryError: unable to create new native thread
ENV _JAVA_OPTIONS="-Xmx2048m"