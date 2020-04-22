import random

while True:
    print("Let's play")
    choice = input("Do your choice:\n\trock\n\tpaper\n\tscissors\n\t")
    choice = choice.lower()
    
    print("My choice is", choice)

    choices = ['rock', 'paper', 'scissors']

    #computer_choice = choices[random.randint(0, len(choices)-1)]
    computer_choice = random.choice(choices)
    
    print("Compuer choice is", computer_choice)
    if choice in choices:
        if choice == computer_choice:
           print('It is a tie')
        if choice == 'rock':
            if computer_choice == 'paper':
                print('You lose, sorry dude :(')
            elif computer_choice == 'scissors': 
                print('You win!!!!!! Congrats!!! :)') 
        if choice == 'paper':
            if computer_choice == 'scissors':
                print('You lose, sorry dude :(')
            elif computer_choice == 'rock': 
                print('You win!!!!!! Congrats!!! :)')
        if choice == 'sciccosr':
            if computer_choice == 'rock':
                print('You lose, sorry dude :(')
            elif computer_choice == 'paper': 
                print('You win!!!!!! Congrats!!! :)')
    else:
        print("Invalid choice, try again")
    print()
