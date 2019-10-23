"""
    author: @vysery98

    Ejemplo 2
"""

lista = [(100, 2), (20, 4), (30,1)]
lista2 = ["b", "a", "c"]

# sorted: para ordenar datos en orden ascendente, reverse: descendente
print(list(zip(sorted(lista2), 
    sorted(lista, key = lambda x: x[1]))))