import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

def get_computer_pick():
  random_number = random.randint(0,2)
  return options[random_number]

def was_game_started():
  return True if user_wins > 0 or computer_wins>0 else False

def did_the_user_logout(user_input):
  return True if user_input == 'q' else False


while True:
  if was_game_started():
    print('You won', user_wins, 'games untill now')
    print('The computer won', computer_wins, 'games untill now')

  user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()

  if did_the_user_logout(user_input):
   break

  if user_input not in options:
    print('This is not a option')
    continue

  computer_pick = get_computer_pick()

  if user_input == 'rock' and computer_pick=='scissors':
    print('You won! The computer choose', computer_pick)
    user_wins +=1
  elif user_input == 'scissors' and computer_pick=='paper':
    print('You won! The computer choose', computer_pick)
    user_wins +=1
  elif user_input == 'paper' and computer_pick=='rock':
    print('You won! The computer choose', computer_pick)
    user_wins +=1
  elif user_input == computer_pick:
   print('The computer choose too', user_input,', try again!')
  else:
    computer_wins+=1
    print('You lose! The computer choose', computer_pick)
  continue




