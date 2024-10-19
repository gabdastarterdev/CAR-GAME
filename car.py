# Car Game!
# Made By: Gab!
# 10/19/2024

import time

# Car name
car_name = input("Name Car: ")
# If car didn't get a name give error.
while car_name == "":
    print()
    time.sleep(0.5)
    print("Please Name your car.")
    time.sleep(0.5)
    car_name = input("Name Car: ")
    
    # If car got named then proceed to the game.
    if car_name == "car_name":
        continue
        
command = ""

# Reminder, Use help for instructions.
time.sleep(0.5)
print()
print("Type ""help"" for help!")
print()

while True:
    command = input("/").lower()
    
    # Help command.
    if command == "help":
        time.sleep(0.5)
        print("""
    start - Start your car
    stop - Stop your car
    quit - To quit the game
        """)
        
    # Start car command.
    elif command == "start":
        print()
        print("Car is starting...")
        time.sleep(1.5)
        print(f"Car Started!")
        print()
    
    # Stop car command    
    elif command == "stop":
        print()
        print("Car uncharging...")
        time.sleep(1.2)
        print("Car stopped!")
        print()
        
    # Quit game command
    elif command == "quit":
        print()
        time.sleep(0.8)
        quit1 = print("Are you sure?")
        quit2 = input("Y/N: ")
        time.sleep(0.1)
        if quit2 == "Y":
            break
            
    # Command error    
    elif command == "":
        print()
        print("Please type a command.")   
        print()
     
    # End of if statements    
    else:
         print ("invalid statement you entered is not a command.")  
         
# Author: Gab!