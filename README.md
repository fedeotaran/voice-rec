# voice-rec

Este es un pequeño programa de reconocimiento de voz.
En este ejemplo, al ejecutar el programa podrán grabar por unos segundos
sus voces y obtendrán como resultado el texto identificado de lo que
hablaron.

## Dependencias del sistema

### Windows

En windows no se necesitan dependencias del sistema.

### Linux

```bash
sudo apt-get install python-pyaudio python3-pyaudio
````

### Mac

```bash
brew install portaudio
```

## Instalación de librerías

Primero debes crear un entorno virtual y activarlo:

```bash
virtualenv venv
```
```bash
source venv/bin/activate
```

Ahora instalar las dependencias dentro del `requirements.txt`:

```bash
pip install requirements.txt
```

Luego ejecuta el programa y graba lo que quieras:
```bash
python voice_to_text.py
````