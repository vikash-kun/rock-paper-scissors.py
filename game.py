import random 

player_score = 0
computer_score = 0
while player_score <2 and computer_score<2:

 player = int(input("pick your number : "))

 if player == 1 :
    print("You chose: ✊")
 elif player == 2 :
    print("You chose: ✋ ")
 elif player == 3:
    print("You chose: ✌️")   

 computer = random.randint(1 , 3)

 if computer == 1:
    print("CPU chose: ✊")
 elif computer == 2:
    print("CPU chose: ✋")
 elif computer == 3:
    print("CPU chose: ✌️")   

 if player == computer:
    print("It's a tie!")
 elif (player == 1 and computer == 3) or \
     (player == 2 and computer == 1) or \
     (player == 3 and computer == 2):
    print("You win this round!")
    player_score+=1
 else:
    print("CPU wins this round!")  
    computer_score+=1
 print(f"score -> you: {player_score} | CPU: {computer_score}")

 if player_score == 2:
    print("you won the game (best of 3)!")
 else:
    print("CPU won the (best of 3)!")    

     