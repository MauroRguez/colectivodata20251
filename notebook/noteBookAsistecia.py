import pandas as pd

#Leyendo los datos de asistecias
asistenciaDataFrame=pd.read_csv("./data/asistencia_estudiantes_completo.csv")
#print(asistenciaDataFrame)

#Obteniendo informacion basica de dataframe

#print(asistenciaDataFrame.info())

#print(asistenciaDataFrame.tail())

#print(asistenciaDataFrame.head())

#print(asistenciaDataFrame.describe())

#print(asistenciaDataFrame.isnull().sum())
#print(asistenciaDataFrame["estado"].value_counts())
print(asistenciaDataFrame["estrato"].value_counts().head())


