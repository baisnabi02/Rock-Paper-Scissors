import random

exit=False
user_points = 0
computer_points = 0
while exit==False:

    options=["rock","paper","scissors"]
    user_input=input("choose rock , paper,scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":


        print("Game Over")
        print("you won a total score of " + str(user_points) +" and the computer total score is "+ str(computer_points))
    
        exit=True
    
    if user_input == "rock":
        if computer_input == "rock":
            print("your input is rock")
            print("computer input is also rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer win!")
            computer_points +=1
        elif computer_input == "scissors":
            print("your input is rock")
            print("computer input is scissors")
            print("you win!")
            user_points +=1 

    elif user_input == "paper":
        if computer_input == "rock":
            print("your input is paper")
            print("computer input  rock")
            print("You win")
            user_points +=1
        elif computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("It is a tie!")

            
        elif computer_input == "scissors":
            print("your input is paper")
            print("computer input is scissors")
            print("computer win!")
            computer_points +=1 


    elif user_input == "scissors":
        if computer_input == "rock":
            print("your input is scissors")
            print("computer input  rock")
            print("computer win")
            computer_points +=1
        elif computer_input == "paper":
            print("your input is scissors")
            print("computer input is paper")
            print("you win!")
            user_points +=1

            
        elif computer_input == "scissors":
            print("your input is scissors")
            print("computer input is scissors")
            print("Its a tie!")
                     


    elif user_input !="rock" or user_input !="paper" or user_input!= "scissors":
        print("Invalid input")

