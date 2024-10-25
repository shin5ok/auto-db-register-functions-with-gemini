# Auto DB register functions with Gemini

## Setup

Set your some environment values.
```bash
export PROJECT_ID=<your PROJECT ID>
export PROJECT_NUMBER=<your PROJECT NUMBER>
export STORAGE=<your storage bucket without "gs://">
```

Type as below, to create database, configure a service account for Functions, and deploy with it.
```bash
make db
make sa
make deploy
```

Just try it!
