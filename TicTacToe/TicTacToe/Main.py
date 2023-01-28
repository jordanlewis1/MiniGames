import TicTacToe

if __name__ == "__main__":
    TicTacToe.startgame()
    while TicTacToe.winner== False:
        TicTacToe.is_winner()
        if TicTacToe.winner == True:
            print("Thank you for playing.")
        else:
            TicTacToe.game_board()
            TicTacToe.first_player()
            TicTacToe.play_game()