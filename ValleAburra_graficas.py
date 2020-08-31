# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:48:38 2020

@author: Usuario
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Lectura de datos 
pts = pd.read_excel('valle_aburra-quads.xlsx')/1000
quads = pd.read_excel('elementos_aburra.xlsx')

# REPRESENTACIÓN DE DATOS

c_pts = pts.iloc[:, :]  # Se selccionan las columnas de la matriz de puntos 

# Se grafican los puntos 

fig= plt.figure(figsize=(20,20)) 
ax=fig.add_subplot(111,projection='3d') 
ax.scatter(c_pts['cordx'], c_pts['cordy'], c_pts['cordz'], c='blue', linewidth=0.001, marker='.')

ax.set(xlim=(0, 25), ylim=(0, 25)), ax.set_zlim([0, 25/3])

ax.set_xlabel('x') 
ax.set_ylabel('y')
ax.set_zlabel('z')

x_value1= []
y_value1= []
z_value1= []

x_value2= []
y_value2= []
z_value2= []

x_value3= []
y_value3= []
z_value3= []

x_value4= []
y_value4= []
z_value4= []


# Se relacionan los elementos, según sus coordenadas y puntos de conectividad  

for i in range (0, len(quads)):
  a=quads.iloc[i,0]
  b=quads.iloc[i,1]
  c=quads.iloc[i,2]
  d=quads.iloc[i,3]
  
  x_value1.append(np.array([c_pts.iloc[a,0], c_pts.iloc[b,0]]))
  y_value1.append(np.array([c_pts.iloc[a,1], c_pts.iloc[b,1]]))
  z_value1.append(np.array([c_pts.iloc[a,2], c_pts.iloc[b,2]]))
  
  x_value2.append(np.array([c_pts.iloc[b,0], c_pts.iloc[c,0]]))
  y_value2.append(np.array([c_pts.iloc[b,1], c_pts.iloc[c,1]]))
  z_value2.append(np.array([c_pts.iloc[b,2], c_pts.iloc[c,2]]))
  
  x_value3.append(np.array([c_pts.iloc[c,0], c_pts.iloc[d,0]]))
  y_value3.append(np.array([c_pts.iloc[c,1], c_pts.iloc[d,1]]))
  z_value3.append(np.array([c_pts.iloc[c,2], c_pts.iloc[d,2]]))
  
  x_value4.append(np.array([c_pts.iloc[d,0], c_pts.iloc[a,0]]))
  y_value4.append(np.array([c_pts.iloc[d,1], c_pts.iloc[a,1]]))
  z_value4.append(np.array([c_pts.iloc[d,2], c_pts.iloc[a,2]]))
  
# Se visualizan los elementos   
 
fig=plt.figure(figsize=(30,30))
ax = plt.axes(projection='3d')
ax.view_init(30, 0) 

ax.set(xlim=(0, 25), ylim=(0, 25))
ax.set_zlim([0, 25/3])

for i in range(len(quads)):
  ax.plot3D(x_value1[i], y_value1[i], z_value1[i], 'b', linewidth=0.2)
  ax.plot3D(x_value2[i], y_value2[i], z_value2[i], 'b', linewidth=0.2)
  ax.plot3D(x_value3[i], y_value3[i], z_value3[i], 'b', linewidth=0.2)
  ax.plot3D(x_value4[i], y_value4[i], z_value4[i], 'b', linewidth=0.2)
  
