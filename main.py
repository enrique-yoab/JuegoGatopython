from components.cli import *
from components.board_logic import *
from components.ai_random import *

def playPlayer(board,symbol):
    size=len(board)
    while True:
        try:
            #se pide al usuario posicion para su marca, se maneja como matriz 
            row=int(input(f"Ingresa el renglon (1-{size}): "))
            column=int(input(f"Ingresa la columna (1-{size}): "))
            if 1 <= row <= len(board) and 1 <= column <= len(board[0]):
                if board[row-1][column-1] == ' ':
                    board[row-1][column-1] = symbol
                    clean_screen()
                    print(f"Tiro el jugador [{row}][{column}]")
                    return
                else:
                    clean_screen()
                    print("Casilla ocupada. Intente de nuevo.")
                    print_board(board)
            else:
                clean_screen()
                print("Valor fuera de rango. Intente de nuevo.")
        except ValueError:
            clean_screen()
            print("Ingresa numeros enteros. Intentalo de nuevo")

def TicTacToe(board,tirador,symbol_player,symbol_machine):
    counter=0
    print(f"El juego iniciará con {'el jugador' if tirador == 1 else 'la máquina'} primero")
    print_board(board)
    winner = None

    while winner==None and not check_full(board):
        if tirador==1:
            playPlayer(board,symbol_player)
        else:
            playAIRandom(board,symbol_machine)
        counter+=1
        print_board(board)
        winner=check_winner(board)
        if winner==symbol_player:
            clean_screen()
            print("¡El usuario ganó! 🎉")
            print_board(board)
            print(f"Se realizaron {counter} tiros totales")
            return
        elif winner==symbol_machine:
            clean_screen()
            print("¡La máquina ganó! 🤖")
            print_board(board)
            print(f"Se realizaron {counter} tiros totales")
            return
        tirador=(2 if tirador == 1 else 1)#Cambio de turno
    clean_screen()
    print("¡Empate! No hubo ningún ganador. 😐")
    print_board(board)
    print(f"Se realizaron {counter} tiros totales")

def main():
    #Comienza con la inicialización del tablero
    main_board=create_board(4)
    #Selección de simbolos tanto del Jugador y Maquina
    symbols=symbol()
    #Selección de quien comienza
    option=selection()
    TicTacToe(main_board,option,symbols[0],symbols[1])

main()