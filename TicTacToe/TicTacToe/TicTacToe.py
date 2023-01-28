
player1 = ""
player2 = ""
play_again = ""
no_ones_turn = True
player1_turn = True
choice = True
winner = False
chosen = True

boxes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def startgame():
    global player1_turn
    global choice
    global player1, player2
    print("Welcome to Tic Tac Toe!")
    while choice == True:
        player1_choice = str(input("Player 1, Do you want to be X or O? "))
        # player1_turn_choice = str(input("Would you like to go first (yes or no): "))
        if player1_choice.upper() == "X":
            player1 = "X"
            player2 = "O"
            choice = False
            return player1
        elif player1_choice.upper() == "O":
            player1 = "O"
            player2 = "X"
            choice = False
            return player1
        else:
            print("Please pick either X or O.")
startgame()

def game_board():
    playing = True
    whitespace = "     |     |     "
    line = "-------------------"
    global boxes
    print("\t" + whitespace)
    print("\t  {}  |  {}  |  {}  ".format(boxes[6], boxes[7], boxes[8]))
    print("\t" + whitespace)
    print("\t" + line)
    print("\t" + whitespace)
    print("\t  {}  |  {}  |  {}  ".format(boxes[3], boxes[4], boxes[5]))
    print("\t" + whitespace)
    print("\t" + line)
    print("\t" + whitespace)
    print("\t  {}  |  {}  |  {}  ".format(boxes[0], boxes[1], boxes[2]))
    print("\t" + whitespace)
game_board()

def first_player():
    global no_ones_turn, player1_turn
    while no_ones_turn == True:
        player1_turn_choice = str(input("Player1, would you like to go first (yes or no): "))
        if player1_turn_choice.lower() == "yes" or player1_turn_choice.lower() == "no":
            if player1_turn_choice.lower() == "no":
                player1_turn = False
                no_ones_turn = False
                return player1_turn
            else:
                no_ones_turn = False
                return player1_turn
        else:
            print("Please pick either yes or no.")
first_player()

def play_game():
    global player1_turn, boxes
    while player1_turn == True:
        print("Player1's turn")
        turn = input("Please pick a square (1-9): ")
        if turn.isdigit() == True and int(turn) in range(1, 10):          
            if type(boxes[int(turn)-1]) == int:
                player1_turn = False
                boxes[int(turn)-1] = player1
                return boxes
            else:
                print("Sorry, this spot is already taken")
        else:
            print("Please pick and integer between 1 and 9.")
    while player1_turn == False:
        print("Player2's turn")
        turn = input("Please pick a square (1-9): ")
        if turn.isdigit() == True and int(turn) in range(1, 10):
            if type(boxes[int(turn)-1]) == int:
                boxes[int(turn)-1] = player2                      
                player1_turn = True
                return boxes
            else:
                print("Sorry, this spot is already taken")
        else:
            print("Please pick and integer between 1 and 9.")


def is_winner():
    global boxes, winner, player1
    if (boxes[0] == player1 and boxes[1] == player1 and boxes[2] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
    elif (boxes[3] == player1 and boxes[4] == player1 and boxes[5] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
    elif (boxes[6] == player1 and boxes[7] == player1 and boxes[8] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
    elif (boxes[0] == player1 and boxes[3] == player1 and boxes[6] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
    elif (boxes[1] == player1 and boxes[4] == player1 and boxes[7] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
    elif (boxes[2] == player1 and boxes[5] == player1 and boxes[8] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
    elif (boxes[0] == player1 and boxes[4] == player1 and boxes[8] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
    elif (boxes[2] == player1 and boxes[4] == player1 and boxes[6] == player1):
        game_board()
        print("Player1 Wins!!!")
        winner = True
        return winner
        #####stop
    if (boxes[0] == player2 and boxes[1] == player2 and boxes[2] == player2):
        game_board()
        print("Player2 Wins!!!")
        winner = True
        return winner
    elif (boxes[3] == player2 and boxes[4] == player2 and boxes[5] == player2):
        game_board()
        print("Player2 Wins!!!")
        winner = True
        return winner
    elif (boxes[6] == player2 and boxes[7] == player2 and boxes[8] == player2):
        game_board()
        print("Player2 Wins!!!")
        winner = True
        return winner
    elif (boxes[0] == player2 and boxes[3] == player2 and boxes[6] == player2):
        game_board()
        print("Player2H Wins!!!")
        winner = True
        return winner
    elif (boxes[1] == player2 and boxes[4] == player2 and boxes[7] == player2):
        game_board()
        print("player2 Wins!!!")
        winner = True
        return winner
    elif (boxes[2] == player2 and boxes[5] == player2 and boxes[8] == player2):
        game_board()
        print("player2 Wins!!!")
        winner = True
        return winner
    elif (boxes[0] == player2 and boxes[4] == player2 and boxes[8] == player2):
        game_board()
        print("player2 Wins!!!")
        winner = True
        return winner
    elif (boxes[2] == player2 and boxes[4] == player2 and boxes[6] == player2):
        game_board()
        print("player2 Wins!!!")
        winner = True
        return winner
    else:
        winner = False
        return winner
    
