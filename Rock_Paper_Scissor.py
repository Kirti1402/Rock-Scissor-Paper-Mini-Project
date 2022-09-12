#Project Rock,Paper and scissor
import random
print("Let Start")

user_choice=input("Enter Your option rock 'r',paper 'p',Scissor 's', Exit 'e': ")

actions=['r','p','s']
comp_choice=random.choice(actions)
print(f"User choose {user_choice} and Computer choose {comp_choice}")

if user_choice == comp_choice:
    print("Tie")
elif user_choice=='r':
    if comp_choice=='s':
        print("You win")
    else:
        print("you lose")
elif user_choice=='s':
    if comp_choice=='p':
        print("you win")
    else:
        print("you lose")
elif user_choice=='p':
    if comp_choice=='r':
        print("you win hola")
    else:
        print("you lose")
