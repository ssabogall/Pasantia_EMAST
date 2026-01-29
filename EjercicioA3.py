"""
Implemente un metodo que cuando haya dos caracteres juntos se debe de volver digamos si hay 2 a entonces necesitare poner a2,si hay 3 "b" 
seguidas entonces poner en texto 3b y asi susesivamente y si solo es una b entonces 1b.
ejemplo de entrada: ["a","a","b","c","c","c","c","c","a","a","a"]
ejemplo de salida: ["a2","b1","c5","a3"]
"""

def comprimir_cadena(Entrada):
    contador= 0
    ContardorLL = []
    for caracter in Entrada: # Primero leo todo lo que hay en mi variable palabras y lo guardo en una variable temporal en caracter
        print(caracter)
        if Entrada.count(caracter) > 1: #aqui pregunto si el caracter se repite mas de una vez en la lista
            contador +=1 #si se repite aumento el contador en 1
            if caracter not in ContardorLL: #pregunto si el caracter ya esta en la lista de salida
                ContardorLL.append(caracter) #si no esta lo agrego
                ContardorLL.append(str(contador)) #agrego el contador convertido a string para que no haya problemas al momento de imprimir
    return print(ContardorLL)


Entrada = ["a","a","b","c","c","c","c","c","a","a","a"]
resultado = comprimir_cadena(Entrada)
print(resultado)

#No me dio y necesitaba hacer otras cosas