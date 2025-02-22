import random
import os

def limpiar_terminal():
    """Limpia la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrarTablero(tablero):
    """Muestra el tablero de juego."""
    for fila in tablero:
        print(" | ".join(fila)) # imprime la lista de fila, uniendo sus elementos con "|"
        print("-" * (len(fila)*4-1)) # crea una linea de "-" para separar las filas.
        
def comprobarTablero(filas, columnas):
    if filas < 3 or columnas < 3:
        print("El tablero no se creo")
        return False
    else :
        print("El tablero se creo")
        return True
    
def marca():
    print("¿Qué marca escoges? 'X' o 'O'")
    while True:
        usuario = input().strip().upper()  # Elimina espacios y convierte a mayúsculass
        if usuario == 'X':
            limpiar_terminal()
            maquina = 'O'
            print(f"La maquina sera: {maquina}\nEl usuario sera: {usuario}")
            return usuario, maquina  # Retorna ambas marcas
        elif usuario == 'O':
            limpiar_terminal()
            maquina = 'X'
            print(f"La maquina sera: {maquina}\nEl usuario sera: {usuario}")
            return usuario, maquina
        else:
            limpiar_terminal()
            print("Ingresa una letra válida: X o O")
            
def seleccion():
    """Inicia el juego del gato."""
    print("\tESTE ES EL JUEGO DEL GATO. ¿QUIERES TIRAR PRIMERO O LA MÁQUINA?")
    tirador = 0
    while tirador == 0:
        try:
            tirador = int(input("1) Usuario tira primero\n2) Máquina tira primero\n"))
            if tirador == 1:
                limpiar_terminal()
                return 1 # Devuelve la elección del jugador
            elif tirador == 2:
                limpiar_terminal()
                return 2 # Devuelve la elección de la máquina
            else:
                limpiar_terminal()
                print("Ingrese un valor válido (1 o 2).")
                tirador = 0  # Reinicia tirador para repetir el bucle
        except ValueError:
            limpiar_terminal()
            print("Entrada inválida. Ingrese un número entero.")
            
def tiraJugador(tablero, marcaU):
    while True:
        try:
            #se pide al usuario posicion para su marca, se maneja como matriz 
            renglon=int(input("Ingresa el renglon (1-3): "))
            columna=int(input("Ingresa la columna (1-3): "))
            if 1 <= renglon <= len(tablero) and 1 <= columna <= len(tablero[0]):
                if tablero[renglon-1][columna-1] == ' ':
                    tablero[renglon-1][columna-1] = marcaU
                    limpiar_terminal()
                    print(f"Tiro el jugador [{renglon}][{columna}]")
                    return tablero #se regresa el tablero modificado
                else:
                    limpiar_terminal()
                    print("Casilla ocupada. Intente de nuevo.")
                    mostrarTablero(tablero)
            else:
                limpiar_terminal()
                print("Valor fuera de rango. Intente de nuevo.")
        except ValueError:
            limpiar_terminal()
            print("Ingresa numeros enteros. Intentalo de nuevo")

def tiraMaquina(tablero,marcaM):
        while True:
            #la maquina escoge una posicion aleatorio
            renglon = random.randint(1,len(tablero))
            columna = random.randint(1,len(tablero[0]))
            #compara la posicion que ingreso si esta vacia
            if tablero[renglon-1][columna-1] == ' ':
                tablero[renglon-1][columna-1] = marcaM
                print(f"La maquina tiro [{renglon}][{columna}]")
                return tablero
            #si la posicion esta ocupada el bucle while se repite
            
def verificaGanador(tablero, marcaU, marcaM, contadorTiros):
    N = len(tablero)     #tamano del renglon
    M = len(tablero[0])  #tamano de la columna
    
    #verificamos los renglones, para identificar si hay 3 iguales
    for renglon in range(N):
        #este es el arreglo dinamico 3 x 3, si hay mas de 3 columnas se adelantara una a la derecha
        for columna in range(M-2):
            if all(tablero[renglon][columna+i] == marcaU for i in range(3)):
                return 1
            if all(tablero[renglon][columna+i] == marcaM for i in range(3)):
                return 2
            
    #verificamos las columnas, para identificar si hay 3 iguales
    for columna in range(M):
        #este es el arreglo dinamico 3 x 3, si hay mas de 3 renglones se adelantara una a la derecha
        for renglon in range(N-2):
            if all(tablero[renglon+i][columna] == marcaU for i in range(3)):
                return 1
            if all(tablero[renglon+i][columna] == marcaM for i in range(3)):
                return 2
            
    #Verificamos las diagonales, de arriba hacia abajo
    for renglon in range(N-2):
        for columna in range(M-2):
            if all(tablero[renglon+i][columna+i] == marcaU for i in range(3)):
                return 1
            if all(tablero[renglon+i][columna+i] == marcaM for i in range(3)):
                return 2
            
    #verificamos las diagonales, de abajo hacia arriba
    for renglon in range(2, N):
        for columna in range(M-2):
            if all(tablero[renglon-i][columna+i] == marcaU for i in range(3)):
                return 1
            if all(tablero[renglon-i][columna+i] == marcaM for i in range(3)):
                return 2
    
    #si el contador de tiros es igual a M x N entonces es un empate
    if contadorTiros == N*M:
        return 3
    #se retorna sero si aun no encuentra un ganador
    return 0
def posicionBloqueo(tablero,marcaU,marcaM):
    print()

def iniciarGato(tirador, marcaU, marcaM):
    """Inicia el juego del gato."""
    fila = 3
    columna = 3
    ganador = 0
    contadorTiros = 0
    
    if comprobarTablero(fila, columna):
        gato = [[' ' for _ in range(columna)] for _ in range(fila)]  # Crear tablero vacío
        print(f"El juego iniciará con {'el jugador' if tirador == 1 else 'la máquina'} primero")
        mostrarTablero(gato)

        while ganador == 0:  # bucle para que tire repetidamente
            #si es 1 tira el jugador, si es diferente tira la maquina
            if tirador == 1:
                gato = tiraJugador(gato, marcaU)
            else:
                gato = tiraMaquina(gato, marcaM)

            contadorTiros += 1
            mostrarTablero(gato)
            #se debe considerar que el gato sera de diferente tamaño y mantendra la jugabilidad como el de 3 x 3 = numero tiros
            ganador = verificaGanador(gato, marcaU, marcaM, contadorTiros)  # Se envía contadorTiros por si ya no hay espacio en el tablero

            if ganador == 1:
                limpiar_terminal()
                print("¡El usuario ganó! 🎉")
                mostrarTablero(gato)
                print(f"Se realizaron {contadorTiros} tiros totales")
                break
            elif ganador == 2:
                limpiar_terminal()
                print("¡La máquina ganó! 🤖")
                mostrarTablero(gato)
                print(f"Se realizaron {contadorTiros} tiros totales")
                break
            elif ganador == 3:  # Si verificaGanador detecta empate
                limpiar_terminal()
                print("¡Empate! No hubo ningún ganador. 😐")
                mostrarTablero(gato)
                print(f"Se realizaron {contadorTiros} tiros totales")
                break
            #tirador es 2 si tirador es igual a 1, si no tirador es 1 si tirador es igual a 2
            #por lo que me alterna el turno
            tirador = 2 if tirador == 1 else 1  # Cambia de turno

    else:
        print("El tablero no se puede iniciar. Dimensiones inválidas.")

# ------------------BLOQUE QUE INICIARÁ EL GATO-------------------
if __name__ == "__main__":
    eleccion = seleccion()
    marcaUsuario, marcaMaquina = marca()
    if eleccion == 1:
      iniciarGato(eleccion,marcaUsuario,marcaMaquina)
    elif eleccion == 2:
      iniciarGato(eleccion,marcaUsuario,marcaMaquina)
    else:
      print("Error al iniciar el juego")