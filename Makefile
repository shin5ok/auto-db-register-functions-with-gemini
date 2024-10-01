STORAGE := $(STORAGE)

.PHONY: deploy
deploy:
	gcloud functions deploy --gen2 --region=us-central1 --runtime=python312 --trigger-bucket=$(STORAGE) cli
