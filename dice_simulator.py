import random
def dice_simulator(num):
    print(num)
while(True):
    choice = input("want to roll again?yes:no")
    if choice == "yes":
        number=random.randint(1,6)
        dice_simulator(number)
    elif choice =="no":
        print(number)
    else:
        print("invalid statement")
            
      
        
        
        
    
