from collections import deque

def mostrar_pista(pista, ruta=None): #Funcion para mostrar la pista
    for i in range(len(pista)): #recorrer sobre cada celda de la pista
        for j in range(len(pista[0])):
            if pista[i][j] == 1: # edificio u obstaculo (pit stop)
                print("x", end=" ") 
            elif pista[i][j] == 2: # agua 
                print("~", end=" ") 
            elif pista[i][j] == 3: # areas bloqueadas temporalmente (yellow flag)
                print("#", end=" ")
            elif ruta and (i, j) in ruta: #si la celda forma parte de la ruta (racing line)
                print("*", end=" ")
            else: # simboliza la carretera o el camino transitable
                print(".", end=" ")     
        print()

def agregar_obstaculos(pista): #Funcion para agregar obstaculos a lapista
    print("\nIngresar las coordenadas y tipo de obstáculos (0: carretera, 1: edificio, 2: agua, 3: area bloqueada, 'fin' para terminar):")
    while True: #se agregan obstaculos hasta que el usuario decida finalizar
        entrada = input("x,y,tipo de obstaculo: ")
        if entrada.lower() == 'fin':
            break

        coordenadas = entrada.split(',')
        if len(coordenadas) != 3: #verificamos si las coordenadas son validas
            print('Formato incorrecto. Debes ingresar dos numeros separados por coma')
            continue

        x = int(coordenadas[0])
        y = int(coordenadas[1])
        tipo_obstaculo = int(coordenadas[2])

        if 0 <= x < len(pista) and 0 <= y < len(pista[0]): #verificamos si estan en el rango y actualizamos los valores en la pista
            pista[x][y] = tipo_obstaculo #el valor simboliza el obstaculo
        else:
            print('Coordenadas fuera de rango.')

def obtener_puntos_pit_stop(pista): # Funcion para obtener los puntos de inicio y fin de la ruta seleccionada por el usuario
    filas = len(pista)
    columnas = len(pista[0])

    while True:
        fila = int(input("x: "))
        columna = int(input("y: "))

        if 0 <= fila < filas and 0 <= columna < columnas:
            return fila, columna
        else:
            print("Coordenadas invalidas!. Estan fuera del rango.")

def calcular_ruta(pista, inicio, final):
    filas = len(pista) # Obtener el número de filas y columnas en la pista
    columnas = len(pista[0])
    fila_busqueda = deque([(inicio, [inicio])]) # Crear una fila de prioridad para explorar todos los puntos
    explorados = set([inicio]) # Registrar las celdas que ya han sido exploradas
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Direcciones posibles de movimiento

    while fila_busqueda:
        (actual, ruta) = fila_busqueda.popleft() # Sacar de la fila el proximo punto para explorar

        if actual == final: # Si nos encontramos en el punto final, retornar la ruta
            return ruta

        for direccion in direcciones: # Explorar todas las direcciones posibles desde el punto actual
            vecino_fila = actual[0] + direccion[0]
            vecino_columna = actual[1] + direccion[1]

            # Verificar si el punto vecino está dentro de los límites del pista
            fila_valida = vecino_fila >= 0 and vecino_fila < filas
            columna_valida = vecino_columna >= 0 and vecino_columna < columnas
            dentro_limites = fila_valida and columna_valida

            # Si el punto vecino está dentro de los límites y no ha sido explorado
            if dentro_limites:
                no_explorados = (vecino_fila, vecino_columna) not in explorados
                tipo_obstaculo = pista[vecino_fila][vecino_columna]

                if tipo_obstaculo == 0:  # Carretera o ruta transitable
                    es_transitable = True
                elif tipo_obstaculo == 1:  # Edificio u obstáculo que no se puede atravesar
                    es_transitable = False
                elif tipo_obstaculo == 2:  # Agua u otros obstáculos
                    es_transitable = True 
                elif tipo_obstaculo == 3:  # Áreas bloqueadas temporalmente
                    es_transitable = False

                # Si el punto vecino es transitable y no ha sido explorado
                if no_explorados and es_transitable:
                    # Marcarlo como explorado y agregarlo a la cola de prioridad
                    explorados.add((vecino_fila, vecino_columna))
                    fila_busqueda.append(((vecino_fila, vecino_columna), ruta + [(vecino_fila, vecino_columna)]))
    return None # Si no se encuentra ninguna ruta

# Parte principal 
# Inicializar el mapa de la pista
pista = [[0, 0, 0, 1, 0], 
        [0, 1, 0, 1, 0], 
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0]]

# Mostrar pista inicial
print("\nMapa de la pista:")
mostrar_pista(pista)

# Agregar obstaculos al pista
agregar_obstaculos(pista)

# Mostrar pista actualizado
print("\nPista actualizada:")
mostrar_pista(pista)

# Obtener puntos de inicio y final de la ruta
print("\nIngrese las coordenadas de inicio del pit stop:")
inicio = obtener_puntos_pit_stop(pista)
print("\nIngrese las coordenadas del final:")
final = obtener_puntos_pit_stop(pista)

# Calcular la ruta mas corta
ruta = calcular_ruta(pista, inicio, final)

# Mostrar la ruta obtenida en la pista
if ruta:
    print(f"\nRuta más corta encontrada desde {inicio} hasta {final}")
    mostrar_pista(pista, ruta)
else:
    print("\nNo existe una ruta disponible.")
