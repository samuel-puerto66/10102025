import random
 # numero aleatorio entre 0 al 1
print(random.random())

#numero entero entre 1 y 10
print(random.randint(1,10))

#seleccioonar un color al azar
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(random.choice(colores))

#mezclar una lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)