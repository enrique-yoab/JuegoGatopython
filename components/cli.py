import os
from components.IA_machine import *
#Necesario para retornar las funciones de comportamiento de IA

def clean_screen():
    """Limpia la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def symbol():
    print("¿Qué marca escoges? 'X' o 'O'")
    while True:
        user = input().strip().upper()  # Elimina espacios y convierte a mayúsculass
        if user == 'X':
            clean_screen()
            machine = 'O'
            print(f"La maquina sera: {machine}\nEl usuario sera: {user}")
            return user, machine  # Retorna ambas marcas
        elif user == 'O':
            clean_screen()
            machine = 'X'
            print(f"La maquina sera: {machine}\nEl usuario sera: {user}")
            return user, machine
        else:
            clean_screen()
            print("Ingresa una letra válida: X o O")
            
def selection():
    """Inicia el juego del gato."""
    print("\tESTE ES EL JUEGO DEL GATO. ¿QUIERES TIRAR PRIMERO O LA MÁQUINA?")
    shoter = 0
    while shoter == 0:
        try:
            shoter = int(input("1) Usuario tira primero\n2) Máquina tira primero\n"))
            if shoter == 1:
                clean_screen()
                return 1 # Devuelve la elección del jugador
            elif shoter == 2:
                clean_screen()
                return 2 # Devuelve la elección de la máquina
            else:
                clean_screen()
                print("Ingrese un valor válido (1 o 2).")
                shoter = 0  # Reinicia tirador para repetir el bucle
        except ValueError:
            clean_screen()
            print("Entrada inválida. Ingrese un número entero.")

def confront():
    print("¿Con que IA te quieres enfrentar?")
    option = 0
    while option == 0:
        try:
            option = int(input("1)IA Random\n2)IA Defensiva\n3)IA Bloqueadora\n"))
            if option == 1:
                clean_screen()
                return throw_random_machine
            elif option == 2:
                clean_screen()
                return None
            elif option == 3:
                clean_screen()
                return Block_Position
            else:
                clean_screen()
                print("Por favor escoga una opción valida.")
                option=0
        except ValueError:
            option=0
            clean_screen()
            print("Entrada inválida. Ingrese un número entero")