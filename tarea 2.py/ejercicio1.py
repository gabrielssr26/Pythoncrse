while True:  
    num = int(input("Ingrese un Numero entero "))
    
    if num>= 0: 
        break
    else: 
        print("Numero invalido, ingrese un numero entero ")
fact = 1
for i in range (1, num+1):
    fact*=i 
print(fact)

