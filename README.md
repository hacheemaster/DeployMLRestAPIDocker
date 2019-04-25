# DeployMLRestAPIDocker
This is the code for "Deploy a Containerized Machine Learning Model as a REST API with Docker" by Hasan Cheema on https://hacheemaster.github.io/DeployRESTAPIDocker/ 

## Overview
The purpose of this project is to deploy a containerized machine learning model as REST API with Docker.

### Methods Used
* Random Forest

### Technologies
* Python
* Flask
* Docker
* cURL

### Dependencies
* flask
* numpy
* sklearn

### Usage
1. Create model.joblib file: 
```python
python model.py
```
2. Build the docker container: 
```python 
docker build . -t docker_flask:v1
```
3. Run the docker container: 
```python
docker run --name test-api -p 5000:5000 -d docker_flask:v1
```
4. Test API: 
```python
curl -v -H "Content-Type: application/json" -d '{"X":"3,3,3,3"}' http://127.0.0.1:5000/predict
```
