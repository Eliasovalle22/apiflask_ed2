# API Flask para Obtener una lista de personas por medio de un endpoint con el metodo 'GET'

Esta API está desarrollada en Flask y devuelve una lista de nombres de personas.

## Instalación

1. Navega a la carpeta del proyecto:
    ```bash
    cd apiflask_taller1
    ```

2. Activa el entorno virtual e instalar las librerias:
    ```bash
    python -m venv 'nombre_del_entorno_virtual' NOTA: En este caso es apiflask_taller1
    apiflask_taller1\Scripts\activate  # Para Windows
    pip install Flask
    ```

3. Se ejecuta la aplicación para obtener la ruta de acceso del endpoint:
    ```bash
    python app.py
    ```

## Uso

Se ejecuta la ruta del endpoint (EJEMPLO: GET http://127.0.0.1:5000/personas) y nos deberia arrojar una respuestas como la siguiente:

    [
    "Ramon",
    "Manuel",
    "Camilo",
    "Oscar",
    "Raul",
    "Marcos"
    ]
