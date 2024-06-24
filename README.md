# Game project

Para correr el juego primero entramos a la carpeta game en terminal con el comando:
```sh
cd game
```
Luego ejecutamos el archivo main.py con el siguiente comando:
```sh
python3 main.py
```
# App project

Primero hacemos un git clone en HTTPS:
```sh
git clone https://github.com/RenatoTato/python-py.git
```
o en SSH:
```sh
git clone git@github.com:RenatoTato/python-py.git
```
Luego entramos a la carpeta app en terminal con el comando:
```sh
cd app
```
Si no tiene la carpeta env, podemos crear con el comando:
```sh
python3 -m venv env
```
Activamos el entorno virtual con:
```sh
source env/bin/activate 
```
una vez ali instalamos las dependencias:
```sh
pip3 install -r requirements.txt
```
Por último, ejecutamos el archivo main.py con el siguiente comando:
```sh
python3 main.py
```