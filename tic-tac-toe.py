from pdb import Restart
from tkinter import N

gameBoard = {'1': ' ', '2': ' ', '3': ' ','4': ' ','5':' ','6':' ','7':' ','8':' ','9':' '}    
    
def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+--+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+--+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(gameBoard)
        print("It's " + turn + "'s turn. Which number would you like to claim?")
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
        
        if count == 9:
            print("Game Over")
            print("Cat's Eye! It's a tie!!!")
            
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
        

if __name__ == "__main__":
    game()