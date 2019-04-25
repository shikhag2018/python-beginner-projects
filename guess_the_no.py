import random
def randomly_generated_no():
    number=random.randint(1,100)
    guess_no(number)
def guess_no(no):
       while(True):
           try:
               user_input=int(input("enter a no between 1 and 100"))
               val=int(user_input)
               if user_input>no:
                   print("too high")
               elif user_input<no:
                   print("too low")
               else:
                   print("you guessed it right\n")
                   choice=input("want to play again?y:n")
                   if choice =="y":
                       randomly_generated_no()
                   elif choice=="n":
                       break
                   else:
                       break
           except ValueError:
              print("enter again")
number=random.randint(1,100)
guess_no(number)
