#Funciones de calculadora 
#crea una funcion de suma con un ingreso de una lista en la cual uno selecciona el numero de valores a sumar 
def suma():
    numbers = int(input("Ingrese el rango de valores: "))
    resultado = 0
    lista = []
# el append agrega los numero seleccionados a la lista de acuerdo al rango seleccionado
    for number in range(numbers):
        numero_ingresado = int(input("Ingrese un numero: "))
        lista.append(numero_ingresado)
        resultado += numero_ingresado
#generador lexico crea un archivo en el cual se representan las operaciones realizadas en una lista regular 
    operacion =generador_lexico(lista, "+")

    with open("operaciones.txt", "a") as archivo:
        archivo.write(operacion + " = " + str(resultado))
        archivo.write("\n")
        
    return print(f"{operacion} = {resultado}")

# la resta conlleva solo dos valores por lo tanto requiere dos inputs de num1 y num2 
def resta():
    number_1 = int(input("Primer valor: "))
    number_2 = int(input("Valor que le gustaria restar al primer valor: "))
    resultado = number_1 - number_2

    with open("operaciones.txt", "a") as archivo:
        archivo.write(str(number_1) + " - " + str(number_2) + " = " + str(resultado))
        archivo.write("\n")

    return print(f"{number_1} - {number_2} = {resultado}")

#multiplicacion replica la lista con una seleccion de valores seleccionada por el usuario
def multiplicacion ():
    numbers = int(input("Ingrese el rango de valores: "))
    resultado = 1
    lista = []
# dentro de la lista con append se ingresan el numero de valores necesarios
    for number in range(numbers):
        numero_ingresado = int(input("Ingrese un numero: "))
        lista.append(numero_ingresado)
        resultado = resultado * numero_ingresado

    operacion =generador_lexico(lista, "*")

    with open("operaciones.txt", "a") as archivo:
        archivo.write(operacion + " = " + str(resultado))
        archivo.write("\n")
# el print de todas las funciones sigue un mismo orden usando f para insertar el string  
    return print(f"{operacion} = {resultado}")

def division():
    dividendo = int(input("Valor del dividendo: "))
    divisor = int(input("Valor del divisor: "))
    #implementando el catch de try y except se elimina la posibilidad de dividir entre 0 ya que matematicamente este escenacio no es viable 

    try:
        resultado = dividendo/divisor
    except ZeroDivisionError:
        return print("El divisor no puede ser 0")

    with open("operaciones.txt", "a") as archivo:
        archivo.write(str(dividendo) + " / " + str(divisor) + " = " + str(resultado))
        archivo.write("\n")

    return print(f"{dividendo} / {divisor} = {resultado}")

def factorial():
    number = int(input("Numero que desea encontrar factorial: "))

    number_factorial = 1
#en la funcion factorial dentro de un rango del 1 al n+1 se multiplican todos los numero dentro de la lista creada
    for numbers in range(1, number+1):
        number_factorial = number_factorial * numbers

    with open("operaciones.txt", "a") as archivo:
        archivo.write(str(number)+"!" + " = " + str(number_factorial))
        archivo.write("\n")
    
    return print(f"{number}! = {number_factorial}")

def potencia():
    base = int(input("numero base: "))
    potencia = int(input("potencia: "))
    resultado = base ** potencia

    with open("operaciones.txt", "a") as archivo:
        archivo.write(str(base) + " ** " + str(potencia) + " = " + str(resultado))
        archivo.write("\n")
        
    return print(f"{base} ** {potencia} = {resultado}")
# implementando el generador lexico con el fin de representar los valores de la operacion no solo su reslutado
#con el operador se le asigna un valor especifico a un espacio por ejemplo  " " y + dentro de los items y strings de una lista 
def generador_lexico(lista, operador):
    resultado = ""
    for items in lista[:-1]:
        resultado += str(items) + " " + operador + " "

    resultado += str(lista[-1])

    return resultado

    #selecciona una opcion para iniciar el proceso o "AC" para salir de la calculadora, una vez iniciado un calculo debe ser finalizado 

def calculator(option):
    match option:
        case "AC":
            return False

        case "1":
            return suma()

        case "2":
            return resta()
        
        case "3":
            return multiplicacion()

        case "4":
            return division()

        case "5":
            return factorial()

        case "6":
            
            return potencia()


if __name__ == "__main__":
# con el while True: se habilita la funcion de un loop que mientras se cumpla un requerimiento de continua la funcion 

    while True:
        print("====================================")
        print("1.  SUMA")
        print("2.  RESTA")
        print("3.  MULTIPLICACION")
        print("4.  DIVISION")
        print("5.  FACTORIAL")
        print("6.  POTENCIA")
        print("AC. SALIR")
        option = input("Que opcion le gustaria selecionar?: ")
        
        if calculator(option) == False:
            break
# al ser un input false se da un break finalizando la calculadora (AC)