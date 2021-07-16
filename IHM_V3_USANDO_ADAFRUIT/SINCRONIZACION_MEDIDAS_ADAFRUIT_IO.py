from Adafruit_IO import *
import random
archivo = open('PROYECTOS/Medidas.txt', "r")
lista = archivo.readlines()
archivo.close()

lista= list(filter(lambda x: x !=';\n', lista)) #Boramos datos del arreglo que no nos sirven
ult=len(lista)					#Tomamos la longitud el areglo
V_act=lista[ult-1]				#Tomamos la ultima posición
print (lista)
V_act= V_act.split(';')				#Hacemos un arreglo separado por ";"
print (V_act)
V_act = [c.replace(',', '.') for c in V_act]	#Reemplazamos las "," por "."
V_B=(V_act[1])					#Tomamos el primer valor
print (ult)
print (V_B)
"""
#Solo lo usamos para ver el valor completo de la matriz:
archivo=open("Medidas.txt","r")
datos=archivo.read()
print(datos)
archivo.close()

"""
aio=Client('Javier_Munoz','aio_Tkxf89BauReHiQupXivyfLTnT7KU')
aio.send("tem-panel",V_B)			#Subimos el valor a la nube
