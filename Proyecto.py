#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sqlite3


# In[5]:


# Cargar datos desde un archivo CSV
data = pd.read_csv('ejecucion-presupuestaria_nivel-partida_a-octubre-2023.csv', sep=';')


# In[12]:


# Realizar manipulaciones de datos con Pandas
# 
filtered_data = data[(data['Partida'] < 40) & (data['Subtítulo'] > 15)]
selected_columns = filtered_data[['Partida', 'Nombre Subtítulo']]

# Ejemplo: Agregar una nueva columna calculada
selected_columns = selected_columns.copy() 
selected_columns.loc[:, 'Nueva_Columna'] = selected_columns['Nombre Subtítulo'] * 2

# Imprimir las primeras filas del DataFrame resultante
print("DataFrame resultante ", selected_columns.head())

# Conectar a la base de datos (creará la base de datos si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')

# Guardar el DataFrame manipulado como una tabla en la base de datos
selected_columns.to_sql('mi_tabla', conn, if_exists='replace', index=False)

# Ejemplo de consulta SQL con los datos filtrados
query = "SELECT * FROM mi_tabla WHERE Nueva_Columna > 20"
resultado = pd.read_sql_query(query, conn)

# Mostrar los resultados de la consulta
print("Resultados: ", resultado)


# In[ ]:




