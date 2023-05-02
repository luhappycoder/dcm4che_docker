
HUB_ACCOUNT=luhappycoder
NAME=dcm4che
VERSION = 0.4
FULL_NAME=${HUB_ACCOUNT}/${NAME}:${VERSION}
DCM4CHE_VERSION := $(shell head -n 1 dcm4che_version.txt)

test_version:
	@echo DCM4CHE_VERSION IS $(DCM4CHE_VERSION)

build: 
	docker build -t $(NAME) --rm . --build-arg DCM4CHE_VERSION=${DCM4CHE_VERSION}

test:
	docker run --rm ${NAME} findscu -h

tag:
	docker tag ${NAME} ${FULL_NAME}

push:
	#docker login
	docker push ${FULL_NAME}
