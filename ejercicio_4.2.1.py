import numpy as np
import os
os.system("cls")
suma=0
promedio=0
cantidad=0
unidos= np.arange(1,10).reshape(3,3)
minimo=np.amin(unidos)
maximo=np.amax(unidos)
for elemento in np.nditer(unidos):
    cantidad=cantidad + 1
    suma=suma+elemento
    promedio=round(promedio+elemento/cantidad)
print("Elemento Mayor: ",maximo)
print("Elemento Menor: ",minimo)
print("Suma de los Elementos: ",suma)
print("Promedio de los Elementos",promedio)
print(unidos)
