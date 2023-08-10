#este codigo permite recibir un numero y el codigo generara 4 columnas con la tabla de numeros en decimal, octal, hexadecimal, binario
#comenzamos definienndo el input del usuario
numero = int(input("Introduzca su numero porfavor"))
#Antes de definir la funcion hacemos que la tabla se vea bien con width, para ello definimos cuanto queremos de anchura
width = len("{0:b}".format(numero))
#definimos la funcion
def funcion(numero):
    for i in range(1,numero+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))
funcion(numero)


"""
D= nos permite convertir cualquier numero en tring formating en decimal
o= nos permite escribir cualquier numero en string formating en octadecimal
X= nos permite escribir cualqiuer numero en string formating en hexadecimal
 y finalmente b nos permite escribir cualquier entero en string formating en binario
"""