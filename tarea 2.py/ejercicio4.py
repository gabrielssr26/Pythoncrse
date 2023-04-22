def cubo(lista):
    lista_cuad = []
    for item in lista:
        lista_cuad.append(item ** 3)

    return lista_cuad

print(cubo([6, 8, 10, 12, 14]))