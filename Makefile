export PROJECT_ID=glo-tech-dev-sebas
export APP_NAME=dv3-manage-tool
export ARTIFACT_REGISTRY=europe-west4-docker.pkg.dev/${PROJECT_ID}/docker/${APP_NAME}

connect_to_project:
	@gcloud config set project ${PROJECT_ID}

build_and_push_docker_image: connect_to_project
	gcloud builds submit . --tag ${ARTIFACT_REGISTRY}

deploy_cloud_run: connect_to_project
	gcloud run deploy ${APP_NAME} \
		--image=${ARTIFACT_REGISTRY}:latest \
		--region=europe-west1 \
		--allow-unauthenticated