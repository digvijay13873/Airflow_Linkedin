from airflow import DAG
from airflow.models import dag
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import os 
script_dir_path = os.path.dirname(os.path.realpath(__file__))
import time
from time import sleep

from xlwt import Workbook
import pandas as pd
from csv import writer
from csv import DictReader
from datetime import datetime
from selenium import webdriver
import psycopg2

import pandas as pd 
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

opt = webdriver.FirefoxOptions()
       
wb=Workbook()
sheet1=wb.add_sheet('Sheet 1',cell_overwrite_ok=False)
i=0
j=0
default_args = {
     'owner': 'airflow',
     'retries': 1
    }

dag = DAG( 'Extract_Source',
            default_args=default_args,
            description='fetching_source',
            catchup=False, 
            start_date= datetime.now(), 
            schedule_interval= '* 7 * * *'  
          )  

def extract():
			#Create Webdriver

			
			driver = webdriver.Remote("http://selenium:4444/wd/hub", options=opt)

#Use login link to start a session on LinkedIn 
#This session shall be used for accessing all other links associated with www.linkedin.com

			driver.get("https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in")

			#Sign-in Automation
			email = "ankurpankur4@gmail.com"
			pwd = "ankur@pankur"
			username = driver.find_element(By.ID,"username")
			username.send_keys(email)
			username.send_keys(Keys.RETURN)

			password = driver.find_element(By.ID,"password")
			password.send_keys(pwd)
			password.send_keys(Keys.RETURN)

			#wait time after page loading

			time.sleep(10)

			#get dataset file with names and url(s)
			#add your test set path here
			df = pd.read_csv(r"./data/Yash_test_set.csv")

			#loop for iterating through dataset and extraction of page source
			i = 758

			while(i <= 833):

				# Get Name and URL from each row
				name = df['Column1'][i]
				url = df['Column2'][i]
				
				# open given URL

				driver.get(url)

				#code for scrolling down to the end of the page to ensure that the entire page is loaded

				
				i_scroll = 0
				f_scroll = 1000
				start = time.time()
				count = 0
				while True:
					count += 1
					driver.execute_script(f"window.scrollTo({i_scroll}, {f_scroll})")
					i_scroll = f_scroll
					f_scroll += 1000
					time.sleep(1)
					end = time.time()

					if round(end - start) > 20 :
						break
			
				time.sleep(10)

				# get source code of page as text

				pg_src = driver.page_source
				i += 1
				# create file name and path for text file

				file_name = name+'.txt'
				#add the file path of the output folder
				file_path = r"./data/linkedin_source/"+file_name+".txt"

				# save source code into text file
				try:
					f = open(file_path , "x" , encoding = 'utf-8')
					f.write(pg_src)
					f.close()
					print((df['Unnamed: 0'][i])-1,'- Done')

				except OSError:
					print((df['Unnamed: 0'][i])-1,'- Skipped')
					continue
					
			driver.quit()

extract_task = PythonOperator(task_id = 'extract_task', 
                              python_callable = extract, 
                              provide_context = True,
                              dag= dag )

extract_task
