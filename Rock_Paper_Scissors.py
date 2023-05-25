import random as rd
options=('rock','paper','scissors')


running =True

while running:

    player=None
    computer=rd.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors)")


    print(f'Player:  {player}')
    print(f'computer: {computer}')

    if player == computer:
        print("It's a Tie")
    elif player=='rock' and computer=='scissors':
        print('congrats! you win.')
    elif player=='paper' and computer=='rock':
        print('congrats! you win.')
    elif player=='scissors' and computer=='paper':
        print('congrats! you win.')
    else:
        print('Better Luck Next Time!')
    
    playAgain=input('Want to play again? (y/n)').lower()
    if not playAgain=='y':
        running=False

print('Thanks for playing :)')