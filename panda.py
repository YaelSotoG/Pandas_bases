# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 14:09:02 2021

@author: Yael UwU
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

##diferencias entre series y dataframes
obj =pd.Series([2,1,-7,3])
print(obj)##imprime un mapa normal
##sirve para agrupar y trabajar con datos
obj.index#sirve para saber el rango de la serie
##como guarda los datos como lista 0=num 1=num, se pueden cambiar los index
obj2=pd.Series([2,1,-7,3],index=['a','b','c','d'])
print(obj2)
print(obj2['c'])#imprime el valor que se necesita
print(obj2[obj2>1])#para hacer filtrado de datos
print(obj2*8)#tambien nos ayuda a multiplicar los datos
print('a' in obj2)#tambien podemos preguntar que datos hay
##
##tambien podemos agregar diccionarios (mapas en flutter)

diccionario={'peras':2, 'manzanas':3,'mango':5}
obj3=pd.Series(diccionario)
print (obj3)#imprime el diccionario ya pasado a una tabla
robots=['x','zero','axl']
obj4=pd.Series(diccionario, index=robots)#puedes cambiar tambien el index
print(obj4)
print(pd.isnull(obj4))#nos detecta cuales son nulos
print(pd.notnull(obj4))#nos detecta cuales son los no nulos


######################################################################################################
######################################################################################################
#que son dataframes

#para entenderlos facil son mapas de mapas, como en json, los acomoda en un cuadro

data={'id':[2,1,-7,3],'name':['pablo','paty','yisus','negro'],'robots':['x','zero','axl','ciel']}
print(data)
frames=pd.DataFrame(data)##cuadro con muchas columnas
print(frames)
print(frames.head())#imprime la cabecera
print(frames.name)#imprime solo los nombres
frames2=pd.DataFrame(data,columns=['name','id','clase'])
print (frames2)#podemos cambiar el nombre de las columnas
print(frames.loc[0])##imprimimos la fila 0 
location=['ecatepunk','jm','la laguna','elementos']
frames['locacion']=location#se le agrega una nueva columna
print(frames)
print(frames.T)#cambia filas por columnas
print(frames.values)#nos imprime los valores
index=frames.index
print(index)#imprime los rangos del index
#nota los valores de index no son inmutables(modificables) solo los de las tablas



######################################################################################################
######################################################################################################
##########
#agrupaciones
df=pd.DataFrame({'key1':['a','a','b','b','b'],'key2':['one','two','one','one','two',],'data1':[1,1,2,3,4,],'data2':['a','a','b','b','d',]})
print(df)
grupo1=df['data1'].groupby(df['key1'])##hace que todos los datos se agrupen por similitudes, ejemplo
##agrupa los a en la key y los b
print(grupo1)
print(grupo1.mean())##saca la media de los valores



#################################################################################################
####################################################################################################
#agrupaciones con arrays
paise=np.array(['mexico','mexico','grecia','grecia','mexico'])
anos=np.array([2005,1999,3000,2000,2000])
print(df['data1'].groupby([paise,anos]).mean())##agrupa por pais y año y saca la media
print(df)



#################################################################################################
####################################################################################################
#iteracion con ordenamiento
#agrupar mas de un campo
for name, group in df.groupby('key1'):##mueve las 'a' a name y los 'b' a group
    print(name)
    print (group)
    
for (k1,k2), group in df.groupby(['key1', 'key2']):##acomoda cuando key1 y key2 son iguales
    print((k1,k2))
    print(group)



#################################################################################################
####################################################################################################
#filtros

people=pd.DataFrame(np.random.randn(5,5),columns=['a','b','c','d','e'],index=['pablo','yael','paty','yisus','mayli',])
print(people)
#el random genera una mattriz de numeros aleatorios
people.iloc[1:3,[1,2]]=np.nan#en las filas 1 a 3 con columna 1y2 pon nulos
print(people)

mapping={'a':'azul','b':'azul','c':'amarillo','d':'amarillo','e':'violeta','f':'amarillo',}
by_column=people.groupby(mapping,axis=1)
#agarra los valores con los a y b y hace la media y cambia los valores por los colores
print(by_column.sum())

#################################################################################################
####################################################################################################
#agrupacion de series

map_series=pd.Series(mapping)#nos ordena las series
print(map_series)
print(people.groupby(map_series,axis=1).count())#cuenta los valores de map seres en la primera columna
