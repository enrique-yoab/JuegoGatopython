from components.cli import *
from components.board_logic import *
from components.user import *
from components.IA_machine import *

def TikTakToe(shoter, symbolU, symbolM, functionMachine, *argsFunctionMachine):
    """Inicia el juego del gato."""
    row = 4      #renglon
    col = 3      #columa
    winner = 0   #ganador (usuario, maquina o empate)
    counter = 0  #contador de los tiros realizados durante el juego
    
    if check_board(row, col):
        board = create_board(row,col)  # Crear tablero vacío ' '
        print(f"El juego iniciará con {'el jugador' if shoter == 1 else 'la máquina'} primero")
        show_board(board)

        while winner == 0:  # bucle para que tire repetidamente
            #si es 1 tira el jugador, si es diferente tira la maquina
            if shoter == 1:
                board = throw_the_user(board, symbolU)
            else:
                board = functionMachine(board,*argsFunctionMachine, symbolU)

            counter += 1
            show_board(board)
            #se debe considerar que el gato sera de diferente tamaño y mantendra la jugabilidad como el de 3 x 3 = numero tiros
            winner = check_winner(board, symbolU, symbolM, counter)  # Se envía contadorTiros por si ya no hay espacio en el tablero

            if winner == 1:
                clean_screen()
                print("¡El usuario ganó! 🎉")
                show_board(board)
                print(f"Se realizaron {counter} tiros totales")
                break
            elif winner == 2:
                clean_screen()
                print("¡La máquina ganó! 🤖")
                show_board(board)
                print(f"Se realizaron {counter} tiros totales")
                break
            elif winner == 3:  # Si verificaGanador detecta empate
                clean_screen()
                print("¡Empate! No hubo ningún ganador. 😐")
                show_board(board)
                print(f"Se realizaron {counter} tiros totales")
                break
            #tirador es 2 si tirador es igual a 1, si no tirador es 1 si tirador es igual a 2
            #por lo que me alterna el turno
            shoter = 2 if shoter == 1 else 1  # Cambia de turno

    else:
        print("El tablero no se puede iniciar. Dimensiones inválidas.")

# ------------------BLOQUE QUE INICIARÁ EL GATO-------------------
if __name__ == "__main__":
   try:
       eleccion = selection()
       marcaUsuario, marcaMaquina = symbol()
       TikTakToe(eleccion,marcaUsuario,marcaMaquina, Block_Position, marcaMaquina)
   except:
       print("Error al iniciar el juego")
