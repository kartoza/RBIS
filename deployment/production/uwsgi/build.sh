#!/usr/bin/env bash

if [ -z "$REPO_NAME" ]; then
	REPO_NAME=dimasciput
fi

if [ -z "$IMAGE_NAME" ]; then
	IMAGE_NAME=rbis_uwsgi
fi

if [ -z "$TAG_NAME" ]; then
	TAG_NAME=latest
fi

if [ -z "$BUILD_ARGS" ]; then
	BUILD_ARGS="--pull --no-cache"
fi

# Build Args Environment

if [ -z "$RBIS_TAG" ]; then
	RBIS_TAG=develop
fi

if [ -z "$BIMS_TAG" ]; then
	BIMS_TAG=latest
fi

echo "RBIS_TAG=${RBIS_TAG}"

echo "Build: $REPO_NAME/$IMAGE_NAME:$TAG_NAME"

docker build -t ${REPO_NAME}/${IMAGE_NAME} \
	--build-arg RBIS_TAG=${RBIS_TAG} --build-arg BIMS_TAG=${BIMS_TAG} \
	${BUILD_ARGS} .
docker tag ${REPO_NAME}/${IMAGE_NAME}:latest ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}
docker push ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}
