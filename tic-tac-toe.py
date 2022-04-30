from pdb import Restart
from tkinter import N

#Tic-Tac-Toe
#By: Mandy Beck

gameBoard = {'1': ' ', '2': ' ', '3': ' ','4': ' ','5':' ','6':' ','7':' ','8':' ','9':' '}   

board_keys = []

for key in gameBoard:
    board_keys.append(key) 
    
def printBoard(board):
    print("")
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print("")
    
def main():
    turn = 'X'
    count = 0
    for i in range(9):
        printBoard(gameBoard)
        print("It's " + turn + "'s turn to choose a square. (1-9): ")
        move = input()
        
        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("That number is already taken. \nPick another number")
            continue
        if count >= 5:
            if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
            elif gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
            elif gameBoard['3'] == gameBoard['5'] == gameBoard['7'] != ' ':
                printBoard(gameBoard)
                print('Game Over')
                print(turn + "'s won!")
                break
        
        while count == 9:
            print("Game Over")
            print("Cat's Eye! It's a tie!!!")
            break
            
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
            
    playAgain()
        
def playAgain():
    restart = input("Do you want to play again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            gameBoard[key] = ' '
        main()
       
if __name__ == "__main__":
    main()