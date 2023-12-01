from typing import List, Tuple
import json
from collections import defaultdict


def q3_time(file_path: str, top_n: int = 10) -> List[Tuple[str, int]]:

    # Optimizar tiempo de ejecución utilizando diccionario, eficiente para buscar por llave (usuario)
    menciones_por_usuario = defaultdict(int)

    # Leer el archivo JSON y procesar los tweets
    try:
        #Lectura en binario para priorizar tiempo de ejecucion
        with open(file_path, 'rb') as file:

            for line in file:
                    tweet = json.loads(line)
                    # Asegurar que existe el usuario antes se consultar el username
                    usuario = tweet.get('user',{}).get('username')
                    # Validar si existe el campo en la data, si no, rellenar con 0
                    menciones = tweet.get('quoteCount', 0)
                    # Incrementar la cantidad de menciones por usuario
                    menciones_por_usuario[usuario] += menciones



    except FileNotFoundError: #Manejo de error en caso de no encontrar el archivo
        print(f"Error: El archivo {file_path} no fue encontrado.")

    # Transformar diccionario en lista y ordenar de manera descendente.
    lista_menciones_por_usuario = list(menciones_por_usuario.items())
    lista_menciones_por_usuario.sort(key=lambda x: x[1], reverse=True)
    # Encontrar el top 10 de usuarios más influyentes
    top_usuarios_influyentes = lista_menciones_por_usuario[:top_n]
    
    result = [
         tuple([usuario, menciones]) 
         for usuario, menciones in top_usuarios_influyentes
         ]

    return result
