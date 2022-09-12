


actions=['r','p','s']

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
        print("you win hola python")
    else:
        print("you lose")
