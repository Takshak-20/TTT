#### TIC_TAC_TOE Game #### 


def default():
    # To set the initialization of game; printed at the start of every new game
    print("\nWelcome!\n Let's get you started with TTT! (TIC_TAC_TOE >.<)")


def rules():
    print("This is the setup you'd be playing on; a few moments from now.")
    print("Guessed the positions? Isn't the 3 X 3 board similar to the right side of your key board?😁\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position(1-9).")

def start():
	# Asking if the player is ready to begin the game
    return(input("Are you ready to get on board? Enter [Y]es or [N]o.\t")).upper().startswith('Y')


def identifiers():
    # Taking the names of players as input;
    
    name_p1 = input("\nEnter NAME of PLAYER 1:\t").capitalize()
    name_p2 = input("Enter NAME of PLAYER 2:\t").capitalize()
    return(name_p1, name_p2)


def xo():
    # Taking the player choice as input;
    choice_p1 = ' '
    while(choice_p1 != 'X' or choice_p1 != 'O'):          # while loop; if the entered value isn't X or O;
        
        # WHILE LOOP STARTS

        choice_p1 = input(f"\n{name_p1}, Do you want to be X or O?\t")[0].upper()
        # The input above has [0].upper() in the end; the user can enter x, X, xxxx or XXX, etc.; the input will always be taken as X;
        # Thereby, increasing the user input window;
        if(choice_p1 == 'X' or choice_p1 == 'O'): 
            break # terminate the loop if the player has entered a reasonable choice i.e 'X' or 'O';
        print("INVALID INPUT! Try doing it again.") # if the entered value isn't X or O, re-run the while loop;

        #WHILE LOOP ENDS
