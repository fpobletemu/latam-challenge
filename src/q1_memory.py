from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter, defaultdict
from memory_profiler import profile

@profile
def q1_memory(file_path: str,top_n: int = 10) -> List[Tuple[datetime.date, str]]:
    # Contador de Tweets por fecha
    tweets_por_fecha = Counter()

    # Diccionario para almacenar el recuento de publicaciones por usuario por fecha
    publicaciones_por_usuario_por_fecha = defaultdict(lambda: Counter())

    with open(file_path, 'r', encoding='utf-8') as file:
        #Se ejecuta la lectura linea por linea para optimizar la memoria utilizada
        for line in file:
            tweet = json.loads(line)
            fecha = tweet['date'][:10]  # Tomar solo la parte de la fecha (sin la hora)
            usuario = tweet['user']['username']

            # Incrementar el recuento de tweets por fecha
            tweets_por_fecha[fecha] += 1

            # Incrementar el recuento de publicaciones por usuario por fecha
            publicaciones_por_usuario_por_fecha[fecha][usuario] += 1

    # Encontrar las top N fechas con más tweets
    top_fechas = Counter(tweets_por_fecha.most_common(top_n))

    # Imprimir las top N fechas con más tweets y el usuario con más publicaciones en cada fecha
    # for fecha, cantidad in top_fechas.items():
    #     usuario_mas_publicaciones = next(iter(publicaciones_por_usuario_por_fecha[fecha].most_common(1)), (None, None))[0]
    #     dt_fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
    #     print(f"Fecha: {dt_fecha}, Tweets: {cantidad}, Usuario con más publicaciones: {usuario_mas_publicaciones}")

    result = [tuple([datetime.strptime(fecha[0], '%Y-%m-%d').date(),next(iter(publicaciones_por_usuario_por_fecha[fecha].most_common(1)), (None, None))[0]]) for fecha, cantidad in top_fechas.items()]
    
    return list(result)