import random

def playAIRandom(board,symbol):
    while True:
        #Definiendo posición
        row=random.randint(0,len(board)-1)
        column=random.randint(0,len(board)-1)
        if board[row][column] == ' ':
            board[row][column]=symbol
            print(f"La maquina tiro en {row},{column}")
            break