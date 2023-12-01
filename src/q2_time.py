from typing import List, Tuple
import json
from collections import Counter
# from operator import itemgetter
import emoji
# from memory_profiler import profile

# @profile
def q2_time(file_path: str, top_n: int = 10) -> List[Tuple[str, int]]:
    
    # Optimizar tiempo usando Listas
    emojis = []
    try:
        # Leer el archivo JSON y procesar los tweets
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:                
                tweet = json.loads(line)
                contenido = tweet['content']
                emojis.extend(emoji['emoji'] for emoji in emoji.emoji_list(contenido))

    except KeyError as e:
        print(f"Error al leer el contenido del tweet: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")

    except FileNotFoundError:
        print(f"Error: El archivo no se encuentra: {file_path}")
    except Exception as e:
        print(f"Error desconocido: {e}")

    # Contador para el recuento de emojis en los comentarios
    recuento_emojis = Counter(emojis)

    # Encontrar el top 10 (por defecto) de emojis usados
    try:
        top_emojis = recuento_emojis.most_common(top_n)
    except Exception as e:
        print(f"Error al encontrar top emojis: {e}")

    
    # Retorna el top 10 historico de emojis y sus conteos respectivos
    result = [tuple([str(emoji_),int(conteo)]) for emoji_, conteo in top_emojis ]
    
    return list(result)