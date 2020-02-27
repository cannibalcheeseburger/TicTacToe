import os
from random import randint
board = ["-","-","-",
        "-","-","-", 
        "-","-","-"]
still_going = True
player = False

def disp_board():
    print(board[0] + "|" + board[1] + "|" + board[2] )
    print(board[3] + "|" + board[4] + "|" + board[5] )
    print(board[6] + "|" + board[7] + "|" + board[8] )         

def game(still_going,player):
    while still_going:
        player = not player
        get_input(player)
        os.system('cls')
        disp_board()
        if check_win() or isTie():
            still_going = False    

def get_input(player):
    while True:
        
        if player:
            position = input("Enter value 1-9:") 
            symbol = "X"
        else :
            position = randint(0,8)
            symbol = "O"  
        if int(position)>0 and int(position)<10 and board[int(position)-1] == "-" :
            break

    board[int(position)-1] = symbol


def isTie(): 
    for i in board:
        if i == "-":
            return False
    print("Its a Tie")        
    return True    


def check_win():
    return rows() or diagonals()

def rows():
    for i in range(0,3):
        if board[i] == board[i+3] and board[i] == board[i+6] and board[i]!="-":
            return True
    for i in range(0,7,3):
        if board[i] == board[i+1] and board[i] == board [i+2] and board[i]!="-":
            return True
    return False                

def diagonals():
    if (board[0]==board[4] and board[0] == board[8] and board[8]!="-") or (board[2]== board[4] and board[2]== board[6] and board[6]!="-"):
        return True
    return False

game(still_going,player)

print("The End MOther Fokers")