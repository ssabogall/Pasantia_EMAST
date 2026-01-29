"""Dado un arreglo de números donde cada elemento se repite exactamente dos veces, 
excepto uno que aparece solo una vez, implemente una funcion que solo deja los numero duplicados, asi sea que 
halla mas de un numero duplicadolos números duplicados
"""

def filtrar_y_multiplicar(Entrada):
    # Tu código aquí
    EntradaN = []
    for entradax in Entrada:
        print (entradax)
        if Entrada.count(entradax) > 1: #aqui pregunto si el numero se repite mas de una vez en la lista
            EntradaN.append(entradax) #si se repite lo agrego a la nueva lista
    return EntradaN
         

Entrada = [4,1,2,1,2]
resultado = filtrar_y_multiplicar(Entrada)
print(resultado)





