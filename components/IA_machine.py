import random

def throw_the_machine(board,symbolM):
        while True:
            #la maquina escoge una posicion aleatorio
            renglon = random.randint(1,len(board))
            columna = random.randint(1,len(board[0]))
            #compara la posicion que ingreso si esta vacia
            if board[renglon-1][columna-1] == ' ':
                board[renglon-1][columna-1] = symbolM
                print(f"La maquina tiro [{renglon}][{columna}]")
                return board
            #si la posicion esta ocupada el bucle while se repite