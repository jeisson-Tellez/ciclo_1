import pandas as pd
from pandas.io.clipboards import read_clipboard
from pandas.io.parsers import read_csv

datos_ejemplo= {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

dataframe_ejemplo= pd.DataFrame(datos_ejemplo)

dataframe_ejemplo.to_csv("ejemplo.cvs") # sep=";"
df=pd.read_csv("ejemplo.cvs")
print(df)
print()
df=pd.read_csv("ejemplo.cvs", skiprows=1 ,names=["primer nombre",
 "Apellido", "edad"," mes 1", " mes 2"]
 , na_values="?")
print(df)

