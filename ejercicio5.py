"""
    @vysery98

    Ejercicio 5:
    
    Manejo de colecciones y tuplas

	Encontrar la siguiente estructura
	
	[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
	(16.666666666666668, 'José')
	[(13.0, 'Ana'), (16.666666666666668, 'José'), (16.333333333333332, 'Ángel')]

	Dadas las siguientes estructuras:

	paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
	nombres = ["Ángel", "José", "Ana"]
"""

# Estructuras
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]

# Promedio de las posiciones 0, 1 y 2 de las tuplas
# Ej: 19 + 10 + 20 = 16.33333333...
promedio = lambda x: (x[0] + x[1] + x[2])/3

# Salida de 3 diferentes listas

# 1: promedio de posiciones 0, 1, 2 + nombre 
print(list(zip(map(promedio, paraleloA),nombres)))

# 2: Se presenta unicamente el que tenga mayor promedio junto al nombre correspondiente
print(max(list(zip(map(promedio, paraleloA),nombres))))

# 3: Se presenta la lista a partir de la posición [1]
print(list(sorted(zip(map(promedio, paraleloA), nombres), key = lambda x: x[1])))

