#juego de adivinar e numero, todos juntos
#adivinar un numero generado aleatoriamente,
#ir introduciendo por teclado el dato a adivinar


from random import randint
generado=randint(0,10)
print (generado)
condicion=True
intento=10
while condicion:
    if intento>0:
        numero=input("dame un numero del 0 al 10: ")
        intento=iintento-1
        if generado==int(numero):
            print("ganaste una anvorgesa que lore paga")
            condicion=False
        else:
            print("el perdedor compra pizza a lore")
            print("te quedan",intento,"intentos")
    else:
        condicion=False
        print("perdiste")
        
