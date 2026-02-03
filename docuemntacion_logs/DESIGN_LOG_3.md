Explica cómo manejaste los estados de "Carga" y "Error" en la UI.
Para que el usuario pudiera tener un feedback del estado de guardado se implementó un "Toast de notificación", en la parte inferior para que no obtruyera la visualización del mapa. Se manejaron tres tipos de estado: 

Cargando: Muestra un icono de spinner y el mensaje "Guardando aroma...". Esto indicándole al usuario que está procesando la petición de guardar y que debe esperar.

Éxito: Si se logró guardar, el estado muestra a un check verde y el mensaje "¡Panadería Guardada!". Esto indicándole al usuario que el proceso se completó correctamente.

"Error" Si no se logró guardar, el estado muestra un símbolo de alerta y el mensaje "Error al conectar". Esto indicándole al usuario que el proceso no pudo completarse debido a un error.