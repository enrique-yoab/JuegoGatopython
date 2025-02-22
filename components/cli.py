import os

def clean_screen():
    """Limpia la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def symbol():
    print("¿Qué marca escoges? 'X' o 'O'")
    while True:
        usuario = input().strip().upper()  # Elimina espacios y convierte a mayúsculass
        if usuario == 'X':
            clean_screen()
            maquina = 'O'
            print(f"La maquina sera: {maquina}\nEl usuario sera: {usuario}")
            return usuario, maquina  # Retorna ambas marcas
        elif usuario == 'O':
            clean_screen()
            maquina = 'X'
            print(f"La maquina sera: {maquina}\nEl usuario sera: {usuario}")
            return usuario, maquina
        else:
            clean_screen()
            print("Ingresa una letra válida: X o O")
            
def selection():
    """Inicia el juego del gato."""
    print("\tESTE ES EL JUEGO DEL GATO. ¿QUIERES TIRAR PRIMERO O LA MÁQUINA?")
    tirador = 0
    while tirador == 0:
        try:
            tirador = int(input("1) Usuario tira primero\n2) Máquina tira primero\n"))
            if tirador == 1:
                clean_screen()
                return 1 # Devuelve la elección del jugador
            elif tirador == 2:
                clean_screen()
                return 2 # Devuelve la elección de la máquina
            else:
                clean_screen()
                print("Ingrese un valor válido (1 o 2).")
                tirador = 0  # Reinicia tirador para repetir el bucle
        except ValueError:
            clean_screen()
            print("Entrada inválida. Ingrese un número entero.")