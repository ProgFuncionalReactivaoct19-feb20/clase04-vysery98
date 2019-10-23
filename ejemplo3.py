"""
    @vysery98
    
    Ejemplo 3
"""

lista = [(100, 2), (20, 4), (30,1)]
lista2 = ["b", "a", "c"]

# Upper - Mayuscula
f = lambda x: x.upper()

print(list(zip(sorted(lista), sorted(map(f, lista2), reverse = True))))