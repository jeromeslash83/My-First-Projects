start_game = True


def tic_board(board):
    print(f"| {board['1']} | {board['2']} | {board['3']} |")    
    print(f"----+---+----")
    print(f"| {board['4']} | {board['5']} | {board['6']} |")
    print(f"----+---+----")
    print(f"| {board['7']} | {board['8']} | {board['9']} |")


def check_winner(count, board):
    """Checks the count number of the game and checks if there is a horizontal, vertical, or diagonal line
    of thee of 'X' or 'O' in the board and returns True if the user has won or is a tie; else it returns False."""
    patterns = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['1','4','7'], ['2','5','8'], ['3','6','9'],['1','5','9'],['3','5','7']]
    if count < 5:
        pass
    elif count == 9:
        print("It's a tie!")
        return True
    else:
        for lists in patterns:
            if set(lists) <= set([k for k,v in board.items() if v == 'X']):
                print("Player 1 wins!")
                return True
            elif set(lists) <= set([k for k,v in board.items() if v == 'O']):
                print("Player 2 wins!")
                return True
            else:
                pass


def new_game():
    """Restarts or closes the game depending on the user's input"""
    restart = input("Do you want to play another game? 'y' or 'n'\n").lower()
    if restart == 'y':
        tic_tac_toe()
    else:
        pass


def tic_tac_toe():
    """Starts the game"""
    board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ',
    '6': ' ', '7': ' ', '8': ' ', '9': ' '
    }
    tile_count = 0
    while start_game:

        tic_board(board)
        #Puts X and O in the squares in the board
        player_1 = input("Player 1 pick a tile number from 1 to 9: ")
        while board[player_1] != ' ':
            print('That space is already taken. Try again.')
            player_1 = input("Player 1 pick a tile number from 1 to 9: ")

        if int(player_1) in range (1,9):
            board[player_1] = 'X'
            tile_count += 1
        else:
            print("Wrong input try again.")
        tic_board(board)
        if check_winner(tile_count, board):
            new_game()
            break
        else:
            pass
        
        player_2 = input("Player 2 pick a tile number from 1 to 9: ")
        while board[player_2] != ' ':
            print('That space is already taker. Try again.')
            player_2 = input("Player 2 pick a tile number from 1 to 9: ")
            
        if int(player_2) in range (1,9):
            board[player_2] = 'O'
            tile_count += 1
        else:
            print("Wrong input try again.")
        if check_winner(tile_count, board):
            new_game()
            break
        else:
            pass

print("Welcome to Tic Tac Toe!")

game = input("Would you like to play a game? 'y' or 'n'\n").lower()
if game == 'y':
    tic_tac_toe()
else:
    start_game = False
