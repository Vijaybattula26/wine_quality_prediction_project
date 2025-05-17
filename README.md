# End-to-end-Machine-Learning-Project-with-MLflow
Workflows
Update config.yaml

Update schema.yaml

Update params.yaml

Update the entity

Update the configuration manager in src config

Update the components

Update the pipeline

Update the main.py

Update the app.py

How to run?
STEPS:
Clone the repository

bash
Copy
Edit
https://github.com/Vijaybattula26/End-to-end-Machine-Learning-Project-with-MLflow
STEP 01- Create a conda environment after opening the repository
bash
Copy
Edit
conda create -n mlproj python=3.8 -y
bash
Copy
Edit
conda activate mlproj
STEP 02- Install the requirements
bash
Copy
Edit
pip install -r requirements.txt
bash
Copy
Edit
# Finally, run the following command
python app.py
Now,

bash
Copy
Edit
open up your local host and port
MLflow
Documentation

cmd
bash
Copy
Edit
mlflow ui
dagshub
dagshub

bash
Copy
Edit
MLFLOW_TRACKING_URI=https://dagshub.com/Vijaybattula26/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=Vijaybattula26 \
MLFLOW_TRACKING_PASSWORD=50f0e77d8eeb2802dd3eb6be8f280c6cab44efa5 \
python script.py
Run this to export as env variables:

bash
Copy
Edit
export MLFLOW_TRACKING_URI=https://dagshub.com/Vijaybattula26/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=Vijaybattula26 

export MLFLOW_TRACKING_PASSWORD=50f0e77d8eeb2802dd3eb6be8f280c6cab44efa5
AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
markdown
Copy
Edit
# with specific access

1. EC2 access : It is a virtual machine

2. ECR: Elastic Container Registry to save your Docker image in AWS

# Description: About the deployment

1. Build the Docker image of the source code

2. Push your Docker image to ECR

3. Launch Your EC2

4. Pull Your image from ECR in EC2

5. Launch your Docker image in EC2

# Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save Docker image
Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install Docker in EC2 Machine:
perl
Copy
Edit
# Optional

```bash
sudo apt-get update -y
sudo apt-get upgrade
```

# Required

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
6. Configure EC2 as self-hosted runner:
settings > actions > runner > new self-hosted runner > choose OS > then run commands one by one

7. Setup GitHub secrets:
ini
Copy
Edit
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY

AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_KEY

AWS_REGION=us-east-1

AWS_ECR_LOGIN_URI=demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME=simple-app
About MLflow
It's production-grade

Trace all of your experiments

Logging & tagging your model
