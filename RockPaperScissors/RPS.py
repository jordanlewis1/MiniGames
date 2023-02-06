import random

computer_score = 0
user_score = 0

class StartGame:
    round_counter = 0
    total_rounds = 1

    def __init__(self):
        pass

    def game_start(self):
        print('--- Rock Paper Scissors Game ---')
    
    def round_choie(self): 
        while True:
            num_of_rounds = str(input('How many rounds would you like to play? '))
            if num_of_rounds.isdigit() == True:
                StartGame.total_rounds = num_of_rounds
                return StartGame.total_rounds
            else:
                print('Invalid Input')
    
    def round_num(self):
        StartGame.round_counter += 1
        print(f'Round #{StartGame.round_counter}')
    
    def get_round(self):
        return StartGame.round_counter


class PlayGame(StartGame):
    cpu_choice = ['Rock', 'Paper', 'Scissors']
    
    def __init__(self):
        self.computer_choice = random.choice(PlayGame.cpu_choice)

    
    def player_choice(self):
        while True:
            user_choice = str(input('Rock, Paper or Scissors: '))
            if user_choice.lower() == 'rock':
                return user_choice
            elif user_choice.lower() == 'paper':
                return user_choice
            elif user_choice.lower() == 'scissors':
                return user_choice
            else:
                print('Not an option')

class Winner():
    def __init__(self, player, computer):
        self.player = player.title()
        self.computer = computer
    
    def check(self):
        global computer_score, user_score
        print(f'You: {self.player}     |     Computer: {self.computer}')
        if self.player == self.computer:
            print('This rounded ended in a tie!')
        elif self.player == 'Rock':
            if self.computer == 'Paper':
                print('You lost this round!')
                computer_score += 1
            else:
                print('You won this round!')
                user_score += 1

        elif self.player == 'Scissors':
            if self.computer == 'Rock':
                print('You lost this round!')
                computer_score += 1
            else:
                print('You won this round!')
                user_score += 1

        else:
            if self.computer == 'Rock':
                print('You won this round!')
                user_score += 1
            else:
                print('You lost this round!')
                computer_score += 1

