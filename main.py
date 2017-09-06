import numpy as np 
import pylab as pl 

# crea un vector con los valores en el eje y para cada valor del eje x
x=[6000,7000,8000,9000,10000]
# crea un vector con los valores del eje x
y=[73,80,85,87,89]
#grafica el vector x contra el vectory
pl.plot(x,y)
# crea un areglo con los valores del eje x
x1=[7000,8000,9000,10000,11000]
# crea un vector con los valores del eje y para cada valor del eje x
y2=[80,83,85,86,88]
# grafica el vector x contra el vector y
pl.plot(x1,y2)
# dar nombre a los ejes 
pl.xlabel('Voltage[V]')
pl.ylabel('Eficiecia[%]')
#guarda la imagen 
pl.savefig('temp1.png')
