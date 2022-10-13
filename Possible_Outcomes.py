def Outcomes():
  import random
  options=("Rock", "Paper", "Scissors")
  usr_choice=input("Pick one: 'Rock', 'Paper', 'Scissors' ")
  usr_choice=usr_choice.lower()
  comp_choice=random.choice(options)
  if (usr_choice == "rock" and comp_choice=="Paper"):
    print("Computer Wins")
  elif (usr_choice == "rock" and comp_choice=="Scissors"):
    print("You Win!")
  elif (usr_choice == "rock" and comp_choice == "Rock"):
    print("No Winner")
  elif(usr_choice == "paper" and comp_choice == "Rock"):
    print("You Win!")
  elif(usr_choice=="paper" and comp_choice=="Paper"):
    print("No Winner")
  elif(usr_choice=="paper" and comp_choice=="Scissors"):
    print("Computer Wins")
  elif(usr_choice=="scissors" and comp_choice=="Rock"):
    print("Computer Wins")
  elif(usr_choice=="scissors" and comp_choice=="Paper"):
    print("You Win!")
  elif(usr_choice=="scissors" and comp_choice=="Scissors"):
    print("No Winner")
  else:
    print("You didnt not pick Rock, Paper, or Scissors")
  print(f"Your Choice: {usr_choice}")
  print(f"Computer's Choice: {comp_choice}")