from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict,Counter
from operator import itemgetter
from memory_profiler import profile

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    # Contador de Tweets por fecha
    tweets_por_fecha = Counter()

    # Diccionario para almacenar el recuento de publicaciones por usuario por fecha
    publicaciones_por_usuario_por_fecha = defaultdict(lambda: defaultdict(int)) # (key: value)

    archivo_tweets = file_path

    with open(archivo_tweets, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            fecha = tweet['date'][:10] # Tomar solo la parte de la fecha (sin la hora)
            usuario = tweet['user']['username']

            # Incrementar el recuento de tweets por fecha
            tweets_por_fecha[fecha] += 1

            # Incrementar el recuento de publicaciones por usuario por fecha
            publicaciones_por_usuario_por_fecha[fecha][usuario] += 1

    # Encontrar las 10 fechas con más tweets, ordeno por el valor de la llave (conteo de tweets)
    top_fechas = sorted(tweets_por_fecha.items(), key=lambda x: x[1], reverse=True)[:10]
    
    result = []
    # Imprimir las 10 fechas con más tweets y el usuario con más publicaciones en cada fecha
    for fecha,cantidad in top_fechas:
        usuario_mas_publicaciones = max(publicaciones_por_usuario_por_fecha[fecha].items(), key=itemgetter(1))[0]
        #Se convierte la fecha de str a datetime
        dt_fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        result.append(tuple([dt_fecha,usuario_mas_publicaciones]))

    #Retornar el resultado asegurando que sea una lista
    return list(result)