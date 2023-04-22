while True:
    num = int(input("ingrese un numero entero mayor a cero  "))
    if num> 0:
        break
    else:
        print("Numero invalido")
triangulo = " "
for i in range(1, num+1):

    triangulo += str(i) + " "
    print(triangulo)
