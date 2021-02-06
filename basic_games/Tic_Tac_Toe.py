# TIC TAC TOE GAME

board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ',
'6': ' ', '7': ' ', '8': ' ', '9': ' '
}

def tic_board():
    print(f"| {board['1']} | {board['2']} | {board['3']} |")    
    print(f"----+---+----")
    print(f"| {board['4']} | {board['5']} | {board['6']} |")
    print(f"----+---+----")
    print(f"| {board['7']} | {board['8']} | {board['9']} |")

def check_winner():
    if board['1'] and board['2'] and board['3'] == 'X' or board['1'] and board['2'] and board['3'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif board['4'] and board['5'] and board['6'] == 'X' or board['4'] and board['5'] and board['6'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif board['7'] and board['8'] and board['9'] == 'X' or board['7'] and board['8'] and board['9'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif board['1'] and board['4'] and board['7'] == 'X' or board['1'] and board['4'] and board['7'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif board['2'] and board['5'] and board['8'] == 'X' or board['2'] and board['5'] and board['8'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif board['3'] and board['6'] and board['9'] == 'X' or board['3'] and board['6'] and board['9'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif board['1'] and board['5'] and board['9'] == 'X' or board['1'] and board['5'] and board['9'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif board['3'] and board['5'] and board['7'] == 'X' or board['3'] and board['5'] and board['7'] == 'O':
        if board['1'] == 'X':
            print ("Player 1 wins!")
        else:
            print ("Player 2 wins!")
    elif tile_count == 9:
        print("No more spaces to be filled. It's a tie.")


print("Welcome to Tic Tac Toe!")
tile_count = 0
start_game = True
game = input("Would you like to play a game? 'y' or 'n'\n").lower()
if game == 'y':
    start_game = True
else:
    start_game = False

while start_game:
    tic_board()
    #Puts X and O in the squares in the board
    player_1 = input("Player 1 pick a tile number from 1 to 9: ")
    while board[player_1] != ' ':
        print('That space is already taker. Try again.')
        player_1 = input("Player 1 pick a tile number from 1 to 9: ")

    if int(player_1) in range (1,9):
        board[player_1] = 'X'
        tile_count += 1
    else:
        print("Wrong input try again.")
    tic_board()
    check_winner()

    player_2 = input("Player 2 pick a tile number from 1 to 9: ")
    while board[player_2] != ' ':
        print('That space is already taker. Try again.')
        player_2 = input("Player 2 pick a tile number from 1 to 9: ")
        
    if int(player_2) in range (1,9):
        board[player_2] = 'O'
        tile_count += 1
    else:
        print("Wrong input try again.")
    check_winner()


