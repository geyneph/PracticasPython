"""
Este programa consiste en capitalaziar los nombres de las personas
"""
#utilizamos input para registrar el nombre de la persona
name = input("introduzca su nombre porfavor")
#procedemos a definir la funcion que nos permititira capitalziar las iniciales
def funcion_capitalizadora(name):
    #hacemos una lista con los nombres
    lista = name.split()
    for palabra in lista:
        lista[lista.index(palabra)] = palabra[0].upper() + palabra[1:]
    resultado = " ".join(lista)
    return resultado
print(funcion_capitalizadora(name))