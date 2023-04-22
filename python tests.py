num = int(input("Ingrese un numero mayor o igual a 0: \n"))
def calcular_factorial(num):
    if num < 0:
        return "El factorial de un negativo no existe"
    elif num == 0:
        return 1
    else:
      factorial = 1
      for i in range(1, num+1):
          factorial = factorial * i
    return factorial
print(calcular_factorial(num))
