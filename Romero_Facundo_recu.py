# Defino la función

def temperatura_media_alta(temperaturas:list, umbral:int) -> bool:
    """
    Función que calcula el promedio de una lista de temperaturas en grados y 
    compara si es mayor o menor al umbral dado.

    Args:

        temperaturas (List): Lista de integers que representan las distintas temperaturas en grados a calcular su promedio
        umbral (int): Temperatura la cual se compara con el promedio de temperaturas
    
    Return:

        Res (Bool): Valor booleano de la comparación de promedio y umbral, True si el promedio es mayor al umbral y False si es menor.
    """
    promedio_temp = sum(temperaturas) / len(temperaturas) # Calcula promedio
    
    # Uso if-statements para el caso que sea True o False
    if promedio_temp > umbral:
        res = True
    else:
        res = False
    
    # Retorno el resultado final
    return res


# Declaro las variables que se usaran en la invocación de la función
temperaturas = [18,22,25,20,21]
umbral = 20

# Invoco a la función.
print(temperatura_media_ubral(temperaturas,umbral))
