#rock paper scissors game

play = 'yes'

print ("Welcome to simple rock paper scissors game!\n")
while play[0] != 'n':
    print ("1. You vs Computer!\n2. You vs Friend!\n\n")

    option = int(input("Enter (1 or 2): "))

    if option == 1:
        import random
        rando = random.randint(0, 2)

        computer = None

        if rando == 0:
            computer = "rock"
        elif rando == 1:
            computer = "paper"
        else:
            computer = "scissor"

        player1 = input('Enter your Move: ')

        if str(player1) != 'rock' and str(player1) != 'paper' and str(player1) != 'scissor':
            print ("You entered invalid input!")
        
        print(f"Computer's Move: {computer}")

        if str(computer) == 'rock':
            if str(player1) == 'rock':
                print("Tie!")
            if str(player1) == 'paper':
                print("You Win!")
            if str(player1) == 'scissor':
                print("Computer Wins")

        if str(computer) == 'paper':
            if str(player1) == 'rock':
                print("Computer wins!")
            if str(player1) == 'paper':
                print("Tie!")
            if str(player1) == 'scissor':
                print("You Win")

        if str(computer) == 'scissor':
            if str(player1) == 'rock':
                print("You Win!")
            if str(player1) == 'paper':
                print("Computer Wins!")
            if str(player1) == 'scissor':
                print("Tie!")
        

    elif option == 2:

        player1 = input("Player 1: ")

        print('NO CHEATING!\n' * 20)

        player2 = input("Player 2: ")

        if str(player1) != 'rock' and str(player1) != 'paper' and str(player1) != 'scissor':
            print ("Player 1 entered invalid input!")
        if str(player2) != 'rock' and str(player2) != 'paper' and str(player2) != 'scissor':
            print ("Player 2 entered invalid input!")


        if str(player2) == 'rock':
            if str(player1) == 'rock':
                print("Tie!")
            if str(player1) == 'paper':
                print("Player 1 Wins!")
            if str(player1) == 'scissor':
                print("Player 2 Wins")

        if str(player2) == 'paper':
            if str(player1) == 'rock':
                print("Player 2 wins!")
            if str(player1) == 'paper':
                print("Tie!")
            if str(player1) == 'scissor':
                print("Player 1 Wins")

        if str(player2) == 'scissor':
            if str(player1) == 'rock':
                print("Player 1 Wins!")
            if str(player1) == 'paper':
                print("Player 2 Wins!")
            if str(player1) == 'scissor':
                print("Tie!")
    
    play = input('Do you wanna play again? [yes/no]: ')