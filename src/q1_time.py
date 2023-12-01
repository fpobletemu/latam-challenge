from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter


def q1_time(file_path: str, top_n: int = 10) -> List[Tuple[datetime.date, str]]:
    
    # Optimizar en tiempo usando Listas como estructura de datos.
    fechas = []
    usuarios = []
    try:
        with open(file_path, 'rb') as file:
            for line in file:
                tweet = json.loads(line)
                fecha = tweet['date'][:10] #Solo se captura la parte de la fecha
                fechas.append(fecha)

                usuario = tweet['user']['username'] #nombre de usuario
                usuarios.append(usuario)
    # Manejo de errores y excepciones, no se realizan dentro del ciclo for para no perjudicar el tiempo de ejecucion
    except FileNotFoundError:
        print(f"Error: El archivo no se encuentra: {file_path}")
    except Exception as e:
        print(f"Error desconocido: {e}") 

    # Optimizar tiempo utilizando Counter() para los conteos.
    counter_fechas = Counter(fechas)

    # Encontrar las 10 fechas con más tweets, ordeno por el valor de la llave (conteo de tweets)

    try:
        top_fechas = [dia for dia, _ in counter_fechas.most_common(top_n)]
    except Exception as e:
        print(f"Error al buscar top de fechas: {e}") 
    
        
    resultado = []
    for dia in top_fechas:
        # Encontrar los indices de los registros que corresponden al dia actual
        indices_dia = [i for i,fecha in enumerate(fechas) if fecha == dia]

        # Contar la frecuencia de usuarios en el dia actual (cantidad de tweets por usuario)
        tweets_por_usuario = Counter(usuarios[i] for i in indices_dia)

        usuario_con_mas_tweets, tweets_usuario = tweets_por_usuario.most_common(1)[0]
        resultado.append(tuple([datetime.strptime(dia, '%Y-%m-%d').date(),usuario_con_mas_tweets]))


    #Retornar el resultado asegurando que sea una lista
    return list(resultado)