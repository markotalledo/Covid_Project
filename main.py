# ANALISIS DE LOS FALLECIDOS POR COVID PERU

# %%
# Basics
import dtale
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
# Data Ingesta; obtenido de https://www.datosabiertos.gob.pe/
import requests

# %%
# Extraemos los datos de los fallecidos
csv_url = 'https://cloud.minsa.gob.pe/s/nqF2irNbFomCLaa/download'
req = requests.get(csv_url)
url_content = req.content
csv_file = open('data/in/dataset.csv', 'wb')
csv_file.write(url_content)
csv_file.close()


# %%
# Extraemos el diccionario de las variables del dataset
dict_url = 'https://www.datosabiertos.gob.pe/sites/default/files/Diccionario_Datos_SINADEF.xlsx'
req = requests.get(dict_url)
url_content = req.content
dict_file = open('data/in/dictionary.xlsx', 'wb')
dict_file.write(url_content)
dict_file.close()


# %%

# Visualizamos el dataset
in_path = "data/in/"
file_name = "dataset.csv"
dataset = pd.read_csv(in_path + file_name, sep='|')
dataset.head()


# %%
d = dtale.show(dataset)
d.open_browser()

# %%

sns.set_style('whitegrid')
dataset.groupby(by='FECHA').count()['Nº'].plot()

# %%
dataset['FECHA'] = pd.to_datetime(dataset['FECHA'])


# %
# %%
pandata = dataset.loc[dataset['FECHA'] > '2020-03-14', :]


# %%
pandata.groupby(by='FECHA').count()['Nº'].plot()
# %%
