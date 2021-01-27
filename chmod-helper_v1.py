""" 
The CHMOD Helper
----------------
Coded by: ryn0f1sh (Ash Noor)
Version: 001
Date: Jan/26/2021
"""

import sys

# ---- Defining Functions ----

# The Intro Function
def intro():
    print("\n-----------------------"
           "\nWelcome to CHMOD Helper"
           "\n-----------------------")


# The CHMOD Options Function
def chmod():
    print("\n-----------------------"
    "\nChoose The Permissions"
    "\n-----------------------"
    "\n1: Execute [--x ]"
    "\n2: Write [ -w- ]"
    "\n3: Execute & Write [ -wx ]"
    "\n4: Read [ r-- ]"
    "\n5: Read & Execute [ r-x ]"
    "\n6: Read & Write [ rw- ]"
    "\n7: Read, Write, & Execute [ rwx ]" "\n")

    # UI's choices.
    # user
    u = int(input(" What is your choice for USER: "))
    
    # group
    g = int(input(" What is your choice for GROUP: "))

    # everyone
    e = int(input(" What is your choice for EVERYONE: "))

    
    # Concacting the code
    uicode = str(u)+str(g)+str(e)
    code = uicode
    vcode = (u, g, e)

    # code test
    #print("\nTest Code:"+ code)    
    
    # Dispalying the numeric results
    print("\nThis Numeric CHMOD code: "+ code)
    
    # Call the visual function
    visual(vcode)



# Creating the Visuals of the permissions chosen 
def visual(vcode):  
    print("Will give your file these permissions: ", end="")            
    for x in vcode:
        if (x == 1):
            print("--x", end="")
        elif (x == 2):
            print("-w-", end="")
        elif (x == 3):
            print("-wx", end="")
        elif (x == 4):
            print("r--", end="")
        elif (x == 5):
            print("r-x", end="")
        elif (x == 6):
            print("rw-", end="")
        elif (x == 7):
            print("rwx", end="")
        else:
            print("Invalid Option")
    
    # Call the again function
    again()


    
# Another file
def again():
    # Getting the Y/N answer.
   answer = input("\n\nWould you like help with another file? y/n : " )
   if (answer.lower() == 'y'):
       # call the chmod function again
       chmod()
   else:
        # Input to exit
        input("-- Thanks for using CHMOD Helper --"
            "\n-- Press Any Key To Exit --")




# ----- End of Defining Functions ----

# Calling Functions
intro() # <-- calling the intro function
chmod() # <-- calling the CHMOD choices function

