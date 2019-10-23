"""
	@vysery98

    Ejercicio 4:
    
    Manejo de colecciones y tuplas

	Encontrar la siguiente estructura
		
	[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]

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

# Salida
print(list(zip(map(promedio, paraleloA),nombres)))