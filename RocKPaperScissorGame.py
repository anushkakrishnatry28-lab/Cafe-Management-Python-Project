#Roch Paper Scissor Game 
import random
item_list=["rock","paper","scissor"]
user=input("User choice:- ").lower()
Computer=random.choice(item_list)
print("Computer choice:- ",Computer)

if(user=="rock" and Computer=="scissor"):
    print("Rahul wins")
elif(user=="rock" and Computer=="paper"):
    print("Computer wins")
elif(user=="rock" and Computer=="rock"):
    print("Game tie")
elif(user=="paper" and Computer=="scissor"):
    print("Computer wins")
elif(user=="paper" and Computer=="paper"):
    print("Game tie")
elif(user=="paper" and Computer=="rock"):
    print("Rahul wins")
elif(user=="scissor" and Computer=="scissor"):
    print("Game tie")
elif(user=="scissor" and Computer=="paper"):
    print("Rahul wins")
elif(user=="scissor" and Computer=="rock") :
    print("Computer wins")

                                       