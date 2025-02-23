from components.cli import *
from components.board_logic import *

def throw_the_user(board, symbolU):
    r=len(board)
    c=len(board[0])
    while True:
        try:
            #se pide al usuario posicion para su marca, se maneja como matriz 
            row=int(input(f"Ingresa el renglon (1-{r}): "))
            col=int(input(f"Ingresa la columna (1-{c}): "))
            if 1 <= row <= r and 1 <= col <= c:
                if board[row-1][col-1] == ' ':
                    board[row-1][col-1] = symbolU
                    clean_screen()
                    print(f"Tiro el jugador [{row}][{col}]")
                    return board #se regresa el tablero modificado
                else:
                    clean_screen()
                    print("Casilla ocupada. Intente de nuevo.")
                    show_board(board)
            else:
                clean_screen()
                print("Valor fuera de rango. Intente de nuevo.")
        except ValueError:
            clean_screen()
            print("Ingresa numeros enteros. Intentalo de nuevo")
