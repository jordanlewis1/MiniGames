import RPS as r

if __name__ == '__main__':    
    game = r.StartGame()
    game.game_start()
    game.round_choie()
    while True:
        if game.round_counter < int(game.total_rounds):
            in_game = r.PlayGame()
            in_game.round_num()
            result = r.Winner(in_game.player_choice(), in_game.computer_choice)
            result.check()
        else:
            print('[Game Summary]')
            print(f'Your points {r.user_score} | Computer points: {r.computer_score}')
            if r.user_score > r.computer_score:
                print('You Won.')

            elif r.computer_score > r.user_score:
                print('Computer Won.')
            else:
                print('It was a tie.')
            print("Thanks for playing")
            break