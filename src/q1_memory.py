from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter, defaultdict
from memory_profiler import profile

@profile
def q1_memory(file_path: str,top_n: int = 10) -> List[Tuple[datetime.date, str]]:
    # Optimizar memoria utilizando Counter como estructura de dato y almacenando solo elementos necesarios
    tweets_por_fecha = Counter()

    # Diccionario para almacenar el recuento de publicaciones por usuario por fecha
    publicaciones_por_usuario_por_fecha = defaultdict(lambda: Counter())
    try:
        with open(file_path, 'rb') as file:
            #Ejecutar la lectura linea por linea para optimizar la memoria utilizada
            for line in file:
                tweet = json.loads(line)
                # Tomar solo la parte de la fecha (sin la hora)
                fecha = tweet['date'][:10]  
                usuario = tweet['user']['username']            
                # Incrementar el recuento de tweets por fecha
                tweets_por_fecha.update([fecha])
                # Incrementar el recuento de publicaciones por usuario por fecha
                publicaciones_por_usuario_por_fecha[fecha].update({usuario: 1})
    # Manejo de errores y excepciones
    except KeyError as e:
        print(f"Error al leer el contenido del tweet: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
    except FileNotFoundError:
        print(f"Error: El archivo no se encuentra: {file_path}")
    except Exception as e:
        print(f"Error desconocido: {e}")

    try:
        # Encontrar las top N fechas con más tweets
        top_fechas = tweets_por_fecha.most_common(top_n)
    except Exception as e:
        print(f"Error al encontrar las fechas con mas tweets: {e}")
   
    # result = [
    #     tuple([datetime.strptime(fecha, '%Y-%m-%d').date(), publicaciones_por_usuario_por_fecha[fecha].most_common(1)[0][0]]) 
    #     for fecha, cantidad in top_fechas
        # ]
    
    return [
        tuple([datetime.strptime(fecha, '%Y-%m-%d').date(), publicaciones_por_usuario_por_fecha[fecha].most_common(1)[0][0]]) 
        for fecha, _ in top_fechas
        ]