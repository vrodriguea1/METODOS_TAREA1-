import numpy as np 
from matplotlib import cm
import matplotlib.pyplot as plt
import pandas as pd
from sympy import * 

pts = np.loadtxt("valle_aburra-quads.pts")/1000
quads = np.loadtxt("valle_aburra-quads.quad", dtype=np.int)
codx, cody, codz = pts[:,0], pts[:,1], pts[:,2]
print(pts)
print(quads)


#COMANDOS PARA GRAFICAR 

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(codx, cody, codz, cmap=cm.viridis, linewidth=1, antialiased=False)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()


con1, con2, con3, con4 = quads[:,0], quads[:,1], quads[:,2], quads[:,3]

##SE DEFINEN TODOS LOS VALORES:

r = 0.577350269189626 ##Valor en n=2 para ecuación de segundo grado en dos dimensiones para r
s = 0.577350269189626 ##Valor en n=2 para ecuación de segundo grado en dos dimensiones para s
wi= 1 ##Ponderación de w para ecuación en dos dimensiones con n=2

##Se definen las funciones base de interpolación:
N0 = (1/4)*(1-r)*(1-s)
N1 = (1/4)*(1+r)*(1-s)
N2 = (1/4)*(1+r)*(1+s)
N3 = (1/4)*(1-r)*(1+s)
Nt = np.array([N0, N1, N2, N3])  ##Matriz de nodos transpuesta 1x4
##Se define la matriz D transpuesta, para hallar el Jacobiano de la función:
DT = np.array([[(s-1)/4, (-s+1)/4, (s+1)/4, (-s-1)/4 ],[(r-1)/4, (-r-1)/4, (r+1)/4, (-r+1)/4]])
X = np.array([[codx,cody]]) ##Matriz de puntos de coordenadas x,y
F = np.ones(shape = (1,4)) ##Matriz de 1s para vector de funciones


##PARA HALLAR EL ÁREA

a_total = 0.0 #Se define el área total igual a cero

V_total = 0.0 #Se define el volumen total igual a cero

nxy = np.zeros((4,2)) #Matriz 4x2 donde se almacenan los elementos de los datos quads

for q in range (0, quads.shape[0]):
    for f in range (0, 4):
        for c in range (0,2):
            nxy[f,c] = pts[quads[q,f],c]
    B = np.dot(Nt, nxy)        
    J = np.dot(DT,nxy[:,:])
    detJ = np.linalg.det(J)
    a = detJ*4*wi
    a_total = a_total + a
    
    #Se halla el punto mínimo de las coordenadas Z (altura mínima):
    hmin = np.amin(codz)
    #Se halla el promedio de la altura en Z de los puntos (promedio altura):
    mediaz = codz.mean()-hmin
    ##Para encontrar el volumen, se multiplica el área de cada cuadrilatero por su altura promedio
    ## ya que el área está proyectada en el plano x,y, y al obtener su altura, tendríamos su volumen
    ## en 3 dimensiones con la altura Z
    v_total = a_total*(mediaz)

      
print('El area proyectada en el plano xy del valle de Aburrá es, ', a_total,'km^2')

print('El volumen total en km^3 es,', v_total,'km^3' )


