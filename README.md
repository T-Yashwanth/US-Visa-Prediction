# US-Visa-Prediction

performed created a folder structure templet.py

wrote setup.py to create a local package us_visa_prediction

wrote mongodb atlas connection with python driver

wrote logging 

wrote exceptions

frist run tremplet file then write requirements and setup files and run them our local package is created then write logging and exceptions and write a mongodb connection in configuration next we have to write data ingestion and we have to validate the data then find the data drift using evidently(its a package) next we have to do next data transformation was done 

## Work flow
1. constant    #contains variable
2. config_entity    #contains all paths (its a path management)
3. artifact_entity  #contains outputs from the component 
4. component        #stages of execution
5. pipeline         #hear we will write all flow of execution
6. app.py / demo.py # we call the pipline from this


for mongodb use the git bash 

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
 
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```




after data ingestion we performed data drift detection with evidently.
if we detect we have to use distribution techniques to distribute evenly, mostly used "powerdistribution technique"

### tools we are using
1. MongoDB to store the data
2. evidently to monitor the data drift
3. model Trainer
4. model evaluater
5. model pusher
6. prediction pipline and using app
7. Deployment



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image
    - Save the URI: 136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject


## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:


	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade

	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker

# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:
1. AWS_ACCESS_KEY_ID
2. AWS_SECRET_ACCESS_KEY
3. AWS_DEFAULT_REGION
4. ECR_REPO