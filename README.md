# US-Visa-Prediction

performed created a folder structure templet.py

wrote setup.py to create a local package us_visa_prediction

wrote mongodb atlas connection with python driver

wrote logging 

wrote exceptions

frist run tremplet file then write requirements and setup files and run them our local package is created then write logging and exceptions and write a mongodb connection in configuration

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
```



after data ingestion we performed data drift detection with evidently.
if we detect we have to use distribution techniques to distribute evenly, mostly used "powerdistribution technique"

### tools we are using
1. MongoDB to store the data
2. evidently to monitor the data drift
3. 