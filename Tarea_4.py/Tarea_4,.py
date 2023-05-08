# Ejercicio 1 
#Ejecutar un programa que realice la cuenta de items, letras y caracteres especiales dentro de un string 
# El ususario ingresa un string de diferentes caracteres y el programa los va a separar en grupos unitarios 

def ejercicio1 (inputString):

    count_num = 0
    count_letters = 0
    count_special = 0
    for i in inputString:
        if i.isalpha():
#alpha realiza un conteo de las letras a partir de cero, con letters, num y special, se le agrega un +1 a la cuenta cada vez que un cararcter designado aparece
            count_letters+=1
        elif i.isnumeric():
            count_num+=1
        else:
            count_special+=1
    return print("Letras en: " +inputString +": " +str(count_letters) +"\nNumeros en " +inputString +": " +str(count_num) +"\nCaracteres especiales en " +inputString +": " +str(count_special))
    


#=============================================================================================

# Ejercicio 2, 
# Cree una funcion que realice una cuente de las apariciones repetidas de un caracter dentro de una stirng
def ejercicio2 (inputString):
    outputDictionary = dict()
    for char in inputString:
        if char not in outputDictionary:
            outputDictionary[char]=1
        else:
            outputDictionary[char]= outputDictionary.get(char)+1
    return print(outputDictionary)

#===========================================================================
#Ejercicio3 
# cree una funcion la cual elimine los elementos repetidos dentre de una combinacion 
def ejercicio3(inputList, removeElement):
    for elements in inputList:
        if elements == removeElement:
            inputList.remove(removeElement)
    return print(inputList)

#============================================================================
# Ejercicio4 
# con el uso de un string, cree una lista y una tupla la cual contenga el mismo orden y puntuacion que el input 
def ejercicio4(inputString):
    #la funcion split pasa de un string a una lista
    my_list = inputString.split(',')
    tupla=tuple(my_list)
    #tuple convierte la lista en una tupla 
    print(my_list)
    print(tupla)
    return(inputString)


#=============================================================================
if __name__=='__main__':


#los inputs fueron predeterminados con el fin de probar que el programa corre los 4 ejemplos por cada uno y asi evitar multiples documentos. 
    print('========Casos de Prueba ejercicio 1=========\n')
print('baba')
ejercicio1('baba')
print(" ")
print('(e)xpresoas22562222 ')
ejercicio1("(e)xpresoas22562222")
print(" ")
print('E$trella24 ')
ejercicio1('E$trella24')
print(" ")
print(' a3rchiv@l2')
ejercicio1('a3rchiv@l2')


print('==========CASOS DE PRUEBA EJERCICIO 2==========\n')
print('Primer string: Esdrujula')
ejercicio2('esdrujula')
print(" ")
print('Segundo string: Papa')
ejercicio2("papa")
print(" ")
print("Tercer string:Pauperrimo")
ejercicio2('pauperrimo')
print(" ")
print('Cuarto String:testosterona')
ejercicio2('testosterona')
print(" ")

print('==========CASOS DE PRUEBA EJERCICIO 3==========\n')
print('Primer lista [20,3,20,40,5,20,80],eliminar 20')
ejercicio3([20,3,20,40,5,20,80],20)
print(" ")
print("Segunda lista: [1,0,1,1,1,1,0,0,1,0,1], eliminar 1")
ejercicio3([1,0,1,1,1,1,0,0,1,0,1],1)
print(" ")
print('Tercer lista:[11,22,33,33,44,55,66,44,22,11,33,11,44,11], elliminar 11')
ejercicio3([11,22,33,33,44,55,66,44,22,11,33,11,44,11],11)
print(" ")
print('Cuarta lista[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9], eliminar 9')
ejercicio3([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9],9) 
print(" ")

print('==========CASOS DE PRUEBA EJERCICIO 4==========\n')
print("Casos ejemplificados de lista y tupla ")
print('Primer lista: 1,2,3,4,5,6,7')
ejercicio4('1,2,3,4,5,6,7')
print(" ")
print('Segunda lista: A,z,u,l,e,j,o')
ejercicio4('A,z,u,l,e,j,o')
print(" ")
print("Tercera lista:Az,1,Rj,2,Vd,3,Gr,4")
ejercicio4('Az,1,Rj,2,Vd,3,Gr,4')
print(" ")
print('Cuarta Lista:P,1,E,2,R,3,R,4,O,5')
ejercicio4('P,1,E,2,R,3,R,4,O,5')


