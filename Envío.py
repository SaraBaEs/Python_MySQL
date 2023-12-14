#!/usr/bin/env python
# coding: utf-8

# In[29]:


get_ipython().system('pip install mysql-connector-python')


# In[30]:


import mysql.connector
import pandas as pd
import numpy as np
import sqlalchemy as db


# In[34]:


#Conexion al sistema de dbs
db = mysql.connector.connect(
    
    host='localhost',
    user='root',
    password=''
)

#Verificar conexión
print(db)


# In[35]:


# Cargar datos desde un archivo CSV
data = pd.read_csv('NFLX.csv', sep=',')


# In[36]:


data.shape


# In[16]:


data.info()


# In[43]:


# Crear una conexión a la base de datos
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_prueba'  
)

# Crear una tabla en la base de datos si no existe
cursor = db.cursor()

# Modifica el nombre de la columna "Open" a algo no reservado o enciérralo entre comillas/backticks
cursor.execute("CREATE TABLE IF NOT EXISTS DataSet (Date DATE, `Open` FLOAT, High FLOAT, Low FLOAT, Close FLOAT, Adj FLOAT, Close2 FLOAT, Volume FLOAT)")
db.commit()

from sqlalchemy import create_engine

# Crea un motor SQLAlchemy a partir de la conexión MySQL
engine = create_engine('mysql+mysqlconnector://root:@localhost/db_prueba')


# Subir los datos desde el DataFrame a la tabla MySQL
data.to_sql('dataset', con=engine, if_exists='replace', index=False)


# In[ ]:




