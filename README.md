# raceroutefinder

Esta implementación de Python simula una pista de carreras con obstáculos y un buscador de rutas de paradas en boxes. El objetivo es encontrar la ruta más corta desde un punto de partida hasta un punto de llegada, evitando obstáculos y áreas bloqueadas utilizando el algoritmo Breadth-First Search (BFS). La pista está representada por un mapa bidimensional, donde cada celda representa una ubicación específica en la pista. 

### Caracteristicas:

- Simula una pista de carreras con varios obstáculos (edificios, agua y áreas bloqueadas) en un mapa bidimensional (2D).
- Permite a los usuarios agregar obstáculos a la pista modificando el mapa.
- Encuentra la ruta más corta desde un punto inicial hasta un punto final utilizando el algoritmo BFS.
- Muestra el mapa y la ruta calculada.

### Inicializacion de la pista:
La pista se inicializa con un mapa predefinido que se puede ser modificado por el usuario agregando diferentes tipos de obstaculos. La pista se representa como una matriz bidimensional donde:
- 0 representa una carretera transitable.
- 1 representa un edificio u obstáculo no transitable.
- 2 representa agua, que es transitable.
- 3 representa áreas bloqueadas temporalmente que no son transitables.

### Mostrar la pista
La funcion ```mostrar_pista``` permite visualizar la pista en la consola.

### Agregar obstaculos
Se pueden agregar obstáculos a la pista utilizando la función ```agregar_obstaculos```. El usuario puede ingresar las coordenadas y el tipo de obstáculo.

### Obtener puntos de inicio y final
El usuario debe ingresar las coordenadas del punto de inicio y del punto final para la ruta mediante ```obtener_puntos_pit_stop```.

### Calcula la ruta
La función ```calcular_ruta``` calcula la ruta más corta desde el punto de inicio hasta el punto final utilizando BFS. Si se encuentra una ruta, se muestra en la pista.

### Requisitos
- Python 3.x
