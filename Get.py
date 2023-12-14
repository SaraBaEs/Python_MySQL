#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd
import pandas as rsd
import numpy as np
import sqlalchemy as db


# In[2]:


# Crear una conexión a la base de datos
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

#Verificar conexión
print(db)

print("-------------------------------")
print("Bases de Datos MySQL")

cursor = db.cursor()

#Recorrer y mostrar las bases de datos
query = 'show databases'
cursor.execute(query)

data_bases = cursor.fetchall()

for data in data_bases :
    print (data)


# In[3]:


#Navegar en la base de datos que requerimos
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_prueba'  
)

cursor = db.cursor()

from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:@localhost/db_prueba')

print("-------------------------------")
print("Tablas disponibles de db_prueba")

#Recorrer y mostrar las bases de datos
query = 'show tables'
cursor.execute(query)

tablas = cursor.fetchall()

for table in tablas :
    print (table)


# In[4]:


#Navegar en la tabla que queremos
query = 'SELECT * from dataset'
cursor.execute(query)


# In[5]:


#Obtener la tabla de MySQL a un Data Frame
data_frame = pd.read_sql(query, con=engine)
display(data_frame)


# In[ ]:




