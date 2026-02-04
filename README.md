PamPan: Un olor delicioso a la vuelta de la esquina.
PamPan es una aplicación de mapas interactiva diseñada para ayudar a los amantes del pan dulce a guardar sus
panadería preferidas en Tijuana.

Cómo correr el proyecto: 
  
  Paso 1: Crear el entorno virtual
   
    python -m venv nombre_del_entorno
    cd nombre_del_entorno
    Para Windows:
      Scripts\activate
    Para Linux
      Source bin\activate
  
  Paso 2: Clonar el repositorio
    
    git clone + URL_del_repositorio
    cd mapaPamPan
  
  Paso 3: Instalar dependencias
   
    pip install -r requirements.txt
  
  Paso 4: Ejecutar aplicación
    
    flask --app main run
    Abrir en el navegador en: http://127.0.0.1:5000/


Stack Tecnológico:

-Backend: pyhton, Flask

-Frontend: HTML5, Tailwind CSS

-Mapa: Leaflet.js, OpenSrtreetMap

-Iconografía: Lucid Icons

Justificación de Diseño:

Para la creación de este protecto se utilizaron algunos principios clave de UX:

1.- Psicología del color y Heurísticas de Nielsen:

- Paleta de colores cálida: Se usaron tonos de color crema, ámbar y café. Estos tonos estimulan
el apetito y dan una sensación de calidez de un horno de panadería.

- El uso de iconos y terminologías cumple con la heuritíca de Nielsen de "Correspondencia entre el sistema y el mundo real."


2.- Ley de Fitts:

- Los controles de Zoom del mapa se encuentran en la eaquina inferior derecha para reducir la distancia que se debe de recorrer para llegar a ellos. También se aumentó el tamaño para que su área tactil sea más amplia reduciendo el posible fallo de hacer click.

3.- Feedback:
-Al hacer clic en el mapa, no se guarda de manera inmediata el pin, sino que sale un popup para confirmar o no si se desea realizar tal acción.
- Para evitar la incertidumbre del usario al intercatuar se agregaron "toasts" para informarle al usuario del estado del sistema en todo momento.

4.- Accesbilidad
- Se implementó un sistema de Pestañas para pantallas más pequeñas (móvil) y columnas para las más grandes.
- Se incluyeron etiquetas "aria-label" en los botones para soporte de lectura de pantallas.
- Es posible navegar por la lista usando las tecas Tab y Enter.

Creditos a la IA

Este código fue co-creado utilizando Gemini Canvas como asistente de programación.

-Prompt para el diseño: PamPan. Debe tener un 'Hero' con una imagen de fondo de una panadería con tonos neutros, un título grande que diga "Un olor delicioso a la vuelta de la esquina", y un botón CTA prominente y fácil de localizar que diga 'Explorar Mapa'. Usa
Tailwind CSS. El diseño debe inspirar el deseo por comer un delicioso pan dulce mexicano y debe usar colores cálidos como el café, beige, amarillo o naranja.

-Prompt para el mapa: Genera un archivo HTML que incluya la librería Leaflet.js (vía CDN) y
Tailwind CSS. Crea un contenedor div 'map' que ocupe el 100% del ancho y 500px de
alto (o 'h-screen'). Inicializa el mapa centrado en Tijuana, Baja California con un tilelayer de
OpenStreetMap. Asegúrate de que los botones de zoom estén en una posición fácil de
alcanzar.

-Prompt para feedback: Escribe un script en JS para Leaflet. Cuando el usuario haga clic en
el mapa: 1. Ponga un marcador temporal inmediatamente. 2. Abra un popup que
pregunte '¿Guardar este punto?'. 3. Al confirmar, envíe las coordenadas (lat, long) a un
endpoint Flask /guardar_punto usando fetch. Muestra un 'toast' o notificación de
'Guardando...' mientras se procesa.

-Prompt para la accesibilidad: Modifica la interfaz para tener dos columnas (o pestañas en móvil):
'Mapa' y 'Lista de Lugares'. Cuando se agregue un marcador en el mapa, debe aparecer
también como un texto descriptivo en la sección de Lista (ej. 'Punto en Lat: X, Long: Y' o la dirección del marcador).
Asegúrate de que todos los botones del mapa/pagina tengan atributos 'aria-label' como 'Acercar
mapa' o 'Alejar mapa'. También los pines deben de contrastar con el mapa.
