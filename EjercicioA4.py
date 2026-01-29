#si tengo una lista con numero del 2 al 10 pero en la lista faltan numero y neceisot la lista de completa 
#con los numero que faltan y tambien los que ya estaban de forma ordenada en una lista
"""
ejemplo:
lista [1, 2, 4, 5] -> Salida: 3
"""
def completar_lista(Entrada):
    # Generar la lista completa desde 1 hasta el máximo valor de la entrada
    maximo = max(Entrada) if Entrada else 0 # Manejar el caso de lista vacía
    lista_completa = list(range(1, maximo + 1)) # Crear lista completa
    faltantes = [num for num in lista_completa if num not in Entrada]# Encontrar los números faltantes    
    return faltantes


EntradaN = [1,2,4,5]   
resultado = completar_lista(EntradaN)
print(resultado)  # Salida esperada: [3]
