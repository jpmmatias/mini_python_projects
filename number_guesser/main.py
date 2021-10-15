import random


play = input('Hello, do you want to play? ')

if play.lower() != 'yes':
  quit()


while True:
  top_of_range = input('Type a number: ')
  if top_of_range.isdigit():
   top_of_range = int(top_of_range)
   if top_of_range <= 0:
     print('Please type a number larger than zero next time!')
     continue
   else:
     break
  else:
   print('Please type a number next time!')
   continue


r = random.randint(0,top_of_range)
guesses = 0

while True:
  guesses += 1
  user_guess = input('Try to guess the random number between 0 and ' + str(top_of_range)+ ': ')
  if user_guess.isdigit():
   user_guess = int(user_guess)
  else:
    print('Please type a number next time!')
    continue
  if user_guess == r:
    print('You are correct!',r,'is the number, guesses:', guesses)
    break
  else:
    print('You are wrong, please try again, your guess is above the number') if user_guess > r else print('You are wrong, please try again, your guess is under the number')
    continue

