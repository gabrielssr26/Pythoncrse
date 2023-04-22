
string1 = input("Ingrese una palabra ")
string2 = input("Ingrese una segunda palabra de la misma longitud ")
if len(string1) != len(string2): 
    print("Las palabras son de diferente numero de caracteres")
else:
    frase = " "
    for i in range(0,len(string1)):
        frase += string1[i] + string2[i]
    print(frase)
