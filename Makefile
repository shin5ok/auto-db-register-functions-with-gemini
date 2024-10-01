STORAGE := $(STORAGE)
REGION := $(REGION)
PROJECT_ID := $(PROJECT_ID)


.PHONY: sa
sa:
	gcloud iam service-accounts create gcs-trigger
	gcloud functions add-invoker-policy-binding gcs_trigger --member=serviceAccount:gcs-trigger@${PROJECT_ID}.iam.gserviceaccount.com --region=${REGION}
	gcloud projects add-iam-policy-binding ${PROJECT_ID} --role=roles/datastore.user --member=serviceAccount:gcs-trigger@${PROJECT_ID}.iam.gserviceaccount.com
	gcloud projects add-iam-policy-binding ${PROJECT_ID} --role=roles/aiplatform.user --member=serviceAccount:gcs-trigger@${PROJECT_ID}.iam.gserviceaccount.com
	gcloud projects add-iam-policy-binding ${PROJECT_ID} --role=roles/eventarc.eventReceiver --member=serviceAccount:gcs-trigger@${PROJECT_ID}.iam.gserviceaccount.com

.PHONY: deploy
deploy:
	gcloud functions deploy \
	--service-account=gcs-trigger@${PROJECT_ID}.iam.gserviceaccount.com \
	--gen2 --region=$(REGION) --runtime=python312 --allow-unauthenticated --cpu=1 --memory=1GiB --set-env-vars=PROJECT_ID=$(PROJECT_ID) --trigger-bucket=$(STORAGE) gcs_trigger


