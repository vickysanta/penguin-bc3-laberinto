#creamos un nuevo archivo nuevo
#guardamos en la carpeta del repositorio
#con la extension py.
#uso de numeros aleatorios
from random import randint  #importamos la libreria randint
aleatorio=randint(0,20)     #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)            #imprimimos el numero generado
#ejercicio
#escribir una funcion sorteo() que reciba una lista de participantes , y elegir a uno de los participantes
#aleatoriamente, y retornar esa persona elegida
#desafio: no volver a retornar una persona ya sorteada

from random import randint   #importamos la funcion randint de libreria random
def sorteo_fin_de_anho(lista):  #definimos una funcion
    cant=len(lista)-1  #utilizamos len saber la cantidad de personas que hay en la lista y guardamos en cant
    #para que no salga del rango
    indice=randint(0,cant) #generamos un indice aleatorio 
    ganador=lista[indice] #sellecionamos un elemento de la lista y guardamos variable ganador
    return ganador #retornamos ganador
    print(ganador)   #esto no se ejecuta
participantes=["pau","kami","lucas","vale","sarita","mandy","fede","vero"] #creamos la lista de participantes
ganar=sorteo_fin_de_anho(participantes) #llamammos a la funcion y guardamos en una variable el resultado 
#retornado por la funcion
print(ganar)







üiio=[]
