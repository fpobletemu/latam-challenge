from typing import List, Tuple
import json
from collections import Counter
from memory_profiler import profile

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    # Optimizar memoria utilizando Counter() para los conteos
    menciones_por_usuario = Counter()

    # Leer el archivo JSON y procesar los tweets
    try:
        # Leer en binario para optimizar memoria
        with open(file_path, 'rb') as file:

            # Leer linea por linea
            for line in file:
                    tweet = json.loads(line)
                    # Asegurar que existe el usuario antes se consultar el username
                    usuario = tweet.get('user',{}).get('username')
                    #Si no existe la llave 'quoteCount' se deja en 0 para evitar validar previamente.
                    menciones = tweet.get('quoteCount', 0)
                    # Incrementar el conteo de quoteCount por usuario usando metodo update() de Counter()
                    menciones_por_usuario.update({usuario: menciones})


    except FileNotFoundError: #Manejo de error en caso de no encontrar el archivo
        print(f"Error: El archivo {file_path} no fue encontrado.")

    # Encontrar el top 10 de usuarios más influyentes.
    top_usuarios_influyentes = menciones_por_usuario.most_common(10)

    # Retornar lista sin almacenarla
    return [
            tuple([usuario,menciones]) 
            for usuario, menciones in top_usuarios_influyentes
           ]
