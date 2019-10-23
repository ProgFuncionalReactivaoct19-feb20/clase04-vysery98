"""
    @vysery98
    
    Ejercicio 6:

    Manejo de colecciones y tuplas

	Encontrar la siguiente estructura
	
	[(4.333333333333333, 13, 'Ángel'), (4.666666666666667, 14, 'Ana')]

	Dadas las siguientes estructuras

	paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
	nombres = ["Luis", "Ángel", "José", "Ana"]
"""

# Estructuras
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]

# Salida:
# 1: zip <- Se une las listas paraleloA, nombres como una sola lista mediante 'list'
# 2: map <- Recibe funcion lambda e itera con los datos de la lista generada previamente
# 3: Presente unicamente aquellos que sea menores a 5 en la posición 0dio bajo
print(list(filter(lambda x: x[0] < 5, map(lambda x: (sum(x[0])/3, sum(x[0]), x[1]), 
    list(zip(paraleloA, nombres))))))