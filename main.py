from flask import Flask, render_template,request, jsonify
import time

app = Flask(__name__)


# Ruta Landing Page
@app.route("/")
def home():
    return render_template("index.html")

# Ruta Mapa
@app.route('/mapa')
def mapa():
    return render_template('map.html')
# Endpoint para recibir datos ---
@app.route('/guardar_punto', methods=['POST'])
def guardar_punto():
    # Recibe los datos enviados por el mapa (latitud, longitud)
    data = request.get_json()
    lat = data.get('lat')
    lng = data.get('lng')
    
    # Simulación que guarda en una base de datos
    print(f"Nueva Panadería detectada en: {lat}, {lng}")
    
    # Simulación de un pequeño retraso de red para ver el efecto de "Cargando..." en el frontend
    time.sleep(1) 
    
    # Respondemos al frontend que todo salió bien
    return jsonify({"status": "success", "mensaje": "Panadería guardada correctamente"})