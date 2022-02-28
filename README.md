# Airflow For Data Extraction From Linkedin

![image](https://user-images.githubusercontent.com/71278693/155889010-af56c5dc-1fb2-4682-b020-e64ac15520a5.png)

## Objective : Extract Data from Linkedin

### Steps for Extracting Data :



### Explore Sample Repository Here :
https://github.com/digvijay13873/airflow_Linkedin.git

### Steps To set up above sample repository on your local machine :

### Prerequisites :
Docker Desktop Installed on local machine

Step : 1
Create Docker Image
```docker build -t airflowlinkedin .```

Step : 2
Give reference of created image in docker compose file.

![image](https://user-images.githubusercontent.com/71278693/155971409-542adc25-8cc8-49fc-8454-cc16cee67ba5.png)

Step : 3
``` docker-compose up ```
This command creates all services needed for airflow under a single container

![image](https://user-images.githubusercontent.com/71278693/155971464-9cda6297-0d99-455e-bdc4-f5e9415adf59.png)

Step : 4
Login to the airflow web UI from your browser.(http://localhost:8080/)

Default Id : airflow

Default pass : airflow

![image](https://user-images.githubusercontent.com/71278693/155887888-0fc50eee-988d-426b-8e03-a7a873c7f8cc.png)


Iniatial Setup For Airflow Environment on Local machine is Completed.


### Working With Dags

A DAG (Directed Acyclic Graph) is the core concept of Airflow, collecting Tasks together, organized with dependencies and relationships to say how they should run.

https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html

Here defined mainly three DAGS in airflow :

1. Extract_Source Dag : To extract source code and save it in .txt file

2. Extract_Profiles : To extract data from Source files and save in .csv


### How to run DAGS ?

DAGs will run in one of two ways:

1. When they are triggered either manually or via the API

![image](https://user-images.githubusercontent.com/71278693/155890883-d0e563cc-a53a-477b-9993-b6397ff035ed.png)

2. On a defined schedule, which is defined as part of the DAG
Click on run dag button(for manually starting dags).If instances of dags are pending you can goto Graph tab and then click on instance to clear it or to get the logs.You can see success and failed dags in airflow UI home screen.

![image](https://user-images.githubusercontent.com/71278693/155888209-5efddc5c-d352-43aa-a923-e31ded9928f3.png)

### Exploring Extracted Data

Goto ./data/results/Linkedin_data_1.4.csv

![image](https://user-images.githubusercontent.com/71278693/155971978-9b5b1f09-f689-4148-af7c-0094ff1cd5ac.png)

![image](https://user-images.githubusercontent.com/71278693/155972040-01a47e72-3a9b-4e3d-ba7e-618840006cfb.png)

## Conclusion :

Airflow along with docker saves a lot of time and effort by automating the tasks.

## Happy Learning !!!







