"""Dada un arreglo de números, mueva todos los ceros al final del arreglo. 
"""
def mover_ceros_al_final(Entrada):
    # Tu código aquí
    EntradaN = []
    for entradaAUX in Entrada:
        print (entradaAUX)
        if entradaAUX != 0: #aqui pregunto si el numero es diferente de cero
            EntradaN.append(entradaAUX) #si es diferente de cero lo agrego a la nueva lista
    for entradaAUX in Entrada:
        if entradaAUX == 0: #aqui pregunto si el numero es igual a cero
            EntradaN.append(entradaAUX) #si es igual a cero lo agrego a la nueva lista            
    return print(EntradaN)

Entrada = [0, 1, 0, 3, 12]
resultado = mover_ceros_al_final(Entrada)
print(resultado)
# porque lo hago asi, porque lo pense como un un lifo pues los primero en entrar son los primeros en salir
# asi que primero agrego los numeros diferentes de cero y luego agrego los ceros al final