""""
Este programa nos permite cambiar, la letra deacuerdo a su posicion, por ejemplo, n la palabra LaZY DoOG la primera letra de la palabra se mantiene igual 

"""
frase = input("introduzca su palabra porfavor")
def palabraCambiadora(frase):
    string =""
    palabras = frase.split()
    for palabra in palabras:
        string+=palabra[0]
        for letra in range(1,len(palabra)):
            if palabra[letra].lower()<palabra[letra-1]:
                string+=palabra[letra].upper()
            elif palabra[letra].lower()>palabra[letra-1]:
                string+=palabra[letra].lower()
            elif palabra[letra].lower()==palabra[letra-1]:
                string+=palabra[letra]
        string+= " "
    print(string)
palabraCambiadora(frase)

    