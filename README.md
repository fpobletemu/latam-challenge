# Data Engineer Challenge - Fernando Poblete
​
## Descripción General
Este repositorio contiene el código para el latam-challenge, realizado por Fernando Poblete. A continuación se describen los problemas resueltos, instrucciones para utilizar el código y como interpretar los perfiladores utilizados para medir las estadísticas de cada función. El código fue desarrollado con `Python 3.10`.

## Enunciados

1. Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días. Debe incluir las siguientes funciones:
```python
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
```
```python
Returns: 
[(datetime.date(1999, 11, 15), "LATAM321"), (datetime.date(1999, 7, 15), "LATAM_CHI"), ...]
```
​
2. Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:
```python
def q2_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("✈️", 6856), ("❤️", 5876), ...]
```
3. El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos. Debe incluir las siguientes funciones:
```python
def q3_time(file_path: str) -> List[Tuple[str, int]]:
```
```python
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
```
```python
Returns: 
[("LATAM321", 387), ("LATAM_CHI", 129), ...]
```
​
## Instrucciones
1. Para este challenge se utiliza como dataset la información contenida en el [siguiente archivo](https://drive.google.com/file/d/1ig2ngoXFTxP5Pa8muXo02mDTFexZzsis/view?usp=sharing).
2. El archivo principal utilizado para analizar las estadísticas del código es un jupyter notebook (.ipynb).
3. Para ejecutar las funciones se deben definir las variables de entorno en un documento .env, usa la siguiente estructura como ejemplo:

```
└─────/src
   ├  ├── q1_memory.py
   ├  └── challenge.ipynb
   ├── *.env*
   ├── requirements.txt
   └── README.md
```

```bash
# Variables de entrega
postUrl="https://url.com/url-entrega"
autorName="Fernando Poblete"
autorEmail="f.pobletemu@gmail.com"
repoUrl="https://github.com/fpobletemu/latam-challenge.git"
#Variables para codigo
dataFilePath=C:\Users\fipob\Desktop\challenge_DE\src\farmers-protest-tweets-2021-2-4.json
```

4. Para ejecutar correctamente todas las funciones se debe levantar un entorno virtual `python -m venv challenge_env`.
5. Para instalar todas las dependencias necesarias, ejecutar `python -m pip install -r requirements`.
6. Una vez asignada la ruta del archivo, levantado el ambiente y dependencias instaladas, es posible ejecutar todas las celdas del archivo `challenge.ipynb` o una por una según prefiera.
7. Para analizar resultados 


## Supuestos
1. El encoding por defecto será `utf-8`
2. Para el tercer enunciado se entiende que las menciones corresponden al campo `'quoteCount'`
3. Se consideran solo los tweets principales, es decir, no se cuentan los tweets que está dentro de otro tweet (quotedTweet)

​
