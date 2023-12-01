from typing import List, Tuple
import json
from collections import Counter
# from operator import itemgetter
import emoji
from memory_profiler import profile

@profile
def q2_memory(file_path: str, top_n: int = 10) -> List[Tuple[str, int]]:
    
    # Optimizar en memoria usando solo estructuras de dato como Counter y no guardando nada mas, solo lo necesario (Emojis).
    recuento_emojis = Counter()
    try:
        # Leer el archivo JSON y procesar los tweets
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Cargar la cadena como un objeto json                
                tweet = json.loads(line)
                # Extraer contenido del tweet
                contenido = tweet['content']
                # Contar emojis dentro del contenido del tweet y sumarlos a los totales
                recuento_emojis.update(emoji['emoji'] for emoji in emoji.emoji_list(contenido))

    # Manejo de errores y excepciones
    except KeyError as e:
        print(f"Error al leer el contenido del tweet: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
    except FileNotFoundError:
        print(f"Error: El archivo no se encuentra: {file_path}")
    except Exception as e:
        print(f"Error desconocido: {e}")            

    # Encontrar el top 10 (por defecto) de emojis usados
    try:
        top_emojis = recuento_emojis.most_common(top_n)
    except Exception as e:
        print(f"Error al encontrar top emojis: {e}")

    
    # Retorna el top 10 historico de emojis y sus conteos respectivos sin almacenar el resultado en ninguna variable dentro de la funcion
    return [tuple([str(emoji_),conteo]) for emoji_, conteo in top_emojis ]