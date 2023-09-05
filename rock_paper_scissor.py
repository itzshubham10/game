import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor= ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choice =(rock,paper,scissor)
user_choice= int(input("Enter your choice ,0 for rock 1 for paper 2 for scissor."))


if user_choice >=3 or user_choice<0:
    print("invalid choice,you lose")

else:
    print("user chose",end='\n\n' + choice[user_choice])
    computer_choice = random.randint(0,2)
    print("\nComputer chose",end='\n\n'+ choice[computer_choice])

    if user_choice == computer_choice:
        print(" \nIt's a draw match ")
    elif user_choice ==0 and computer_choice ==2:
        print("\nyou win")
    elif user_choice ==2 and computer_choice ==0:
        print("\nyou lose!")
    elif computer_choice> user_choice:
        print("\nyou lose!")
    elif user_choice>computer_choice:
        print("\nyou win!")

