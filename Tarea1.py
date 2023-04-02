#prob.1
# El programa recibe una frase la cual tiene que analizar su composicion gramatica
# al determinar si esta se lee de igual forma en cualquier sentido 
# la frase debe poseer la misma letra al inicio y al final
# la frase debe poseer un centro absoluto del cual parten dos frases simetricas 
# una vez que se comprueban estos parametros el sistema notifica una alerta "palin" 

# Pedir una frase al usuario 
# A partir de la primera letra contar el numero de caracteres de la frase 
# Si el numero de caracteres de una frase es par o divisible entre 2 se descarta con "palin"
 # "Ana trae pan" 10 caract (desc.)
 # "Vive en Croacia" 13 caract (appr.)
# Si la frase es un numero impar se analiza la primera y ultima letra, si son distintas se descarta "palin"
 # 'Vive en Croacia" carac impar, primer letra V ultima letra A (desc.)
 # "Raquel fue a tomar" carac impar, primer letra R ultima letra R 
# Si los caracteres al lado de la letra central de la frase son iguales se establece como "palin" 
  # "Sometamos o matemos" (impar 17 carac.) (prim. letr S, ult. letr S) (cent. S, lados de "o"y "o")
# Report "palin"

#sub prob
# impar no consecuente de "palin"
 # una frase puede ser impar no obstante esta no es palindroma debido a esto se tiene que anailzar a un segundo plano
# impar, primer y ultima letra igual no consecuente de de "palin" 
  # al no cumplir con el requisito de ser impar se descarta la palabra, si se cumple se conserva y se analiza la ultima y primer letra de la frase 
  # aunque ambos caracteres sean iguales no es consecuente de "palin" ya que el resto de la frase puede diferir
# impar, primer - ultima letra igual y letras al lado 
 # si los dos caracteres al lado del caracter central son simetricos 
#al cumplirse estos tres parametros el sistema refleja "palin"

#Prob 2 

# el programa lleva un registro de acciones individuales las cuales va a determinar como logs 
# una vez que se representa la accion como log se lleva una cuenta de 24 horas
# una vez transcurridas las 24 horas se va a borrar este log per request del administrador 
# solo se conservan mas alla de las 24 horas los logs que contengan "error" en su data
# en el caso de este poseer un "error" se debe dirigir a un directorio por separado llamado "Errores"
# Al redirigirse, un mensaje automatizado debe enviarse al correo del administrador 

# se recibe actividad la cual se cataloga como "logs" 
# a cada "logs" se le asigna un conteo "T-minus 86400s"
# durante el conteo se analiza la composicion de las palabras en busca "err"
 # Al leer "err" se elimina el conteo
  # asigna el "err" al direc. Errores al hacer match "err" con "Err"
# Se crea un mensaje predeterminado que se envia a un destinatario standard que se automatiza su activacion al existir la presencia de "err" en un log 
 # Al no haber "err" el conteo continua hasta "T minus 0s y se elimina"

# al iniciar el analisis de cada frase se toma en cuenta el conteo de palabras y sus iniciales, se compara todo el alfabeto y se detiene en e, se detiene en la palabra con este caracter 
#se repite el proceso y se detiene en r, si no se presenta esta caracteristica se procede con la siguiente palabra 
 # al tener "e", "r" y "r" se asume que el log posee error 
#al tener error se elimina el conteo, sin embargo el mensaje automatizado necesita cuerpo y destinatario 
 # se predetrminan ambos ya que la accion de envio es desencadenada al presentarse "err" 

#prob 3

#el programa debe notificart si un numero entero es multiplo de 5 
 # el numero presente no es estrictamente el inicial ya que el orden de este puede ser re acomodado de forma que se consiga un  multiplo 
# el orden de los numeros se analiza con la tabla de division del 5 con el proposito de determinar si alguna de las potenciales combinaciones numericas dan un dividendo entero 

# El interfaz de la plataforma permite el ingreso de un numero entero 
 # si el num. ingresado posee (.) se presenta (num invalid)
# SI Al ingresar un numero valido el sistema analiza las posibles combinaciones numericas del numero entero 
 # (num 1437) possible (1473) (1347)(1374)(1743)(1734)(...)
# SI Al determinar todo el campo muestral el sistema corre la ecuacion 
 # x/5= y 
  # en el cual ambos "X" y "Y" deben ser numeros enteros 
# Si ambos numeros son enteros la combinacion de numeros (X) es multiplo de 5 
# SI se  presenta un multiplo de 5 el sistema notifica (Y mult 5 igual X)

# no todos los numeros ingresados son numeros enteros ya que existen decimales y fracciones que mientras pueden traducirse a numeros enteros no pueden ser re ordenados 
# Al ingresar un numero entero las posibles combinaciones se elevan a mayor numero de digitos 2 digitos = 2 combinaciones, 3 digitos = 6, 4 digitos = 24 combinaciones 
  # el aumento de la variable de combinaciones es num de posibles combinaciones anterior a partir de multiplicado por si mismo  +1
   # un numero de 2 digitos tiene 2 combinaciones osea 3 digitos posee 2*(2+1) = 6 combinaciones 
# una vez las posibles combinaciones se presentan se divide /5 y se toman las muestras. 


