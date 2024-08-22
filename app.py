# importar liberia Flask y liberia jsonify
from flask import Flask, jsonify

# instancia de la liberia Flask
app = Flask(__name__)

# ruta para el endpoint '/personas'
@app.route('/personas', methods = ['GET'])

# creacion del metodo obtener_personas
def obtener_personas():
    # funcion de lista estatica de nombres 
    names = ["Ramon",
            "Manuel",
            "Camilo",
            "Oscar",
            "Raul",
            "Marcos"]
    
    # convertir la lista names en formato JSON
    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True)

