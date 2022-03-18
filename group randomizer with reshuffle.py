"""
Program that randomizes objects in groups. Option of whether to add or remove object is asked
"""

print("Welcome to the Team Randomizer program created by Isaiah Rocha, Joel Sanchez, Joshua Naisbitt, and Timothy Pham!")

reset_loop_input = "Y" #sets the loop repeat condition before looping
while reset_loop_input == "Y": #after running the main program, this loop will either repeat or terminate based on user input

    #main program
    import random #imports random module

    def add(user_list_input):
        while "0" not in mylists: #keep run until 0 is inputted
                print("\nCurrent list is: ", mylists, "\n")
                user_list_input = input("What did you want to add to the list? Input 0 when you are finished. \n") #add whatever item you want to list as long as it is not 0
                mylists.append(user_list_input) #adds item to list

    def remove(user_list_remove):
        while user_list_remove != "0": #keep run until 0 is inputted
                print("\nCurrent list is: ", mylists, "\n")
                user_list_remove = input("What would you like to remove? Input 0 when you are finished. \n") #removes whatever item you want to list as long as it is not 0
                if user_list_remove != "0":
                    if user_list_remove not in mylists:
                        print ("\n",user_list_remove, "was not found the in the list. Try again.") #restarts loop if they inputted the wrong item
                    else:
                        mylists.remove(user_list_remove) #removes item to list


    mylists = [] #creates empty list
    numberofgroups = int(input("How many groups do you want?\n")) #sets number of group
    user_list_remove = "1" #sets user remove before looping
    user_list_input = "1" #sets the user input before looping
    add_or_remove = input("\nADD, REMOVE, or NONE: \n")
    while add_or_remove != "NONE":
        if add_or_remove == "ADD":
            add(user_list_input)
            mylists = list(dict.fromkeys(mylists)) #removes duplicates from the list
            mylists.remove("0") #removes 0 from the list
        elif add_or_remove == "REMOVE":
            remove(user_list_remove)
            user_list_remove = "1"
        elif add_or_remove == "NONE": #stops the loop if user inputs NONE
            break
        add_or_remove = input("ADD, REMOVE, or NONE: \n")
    unshuffled = mylists.copy()            
    numberofpeople = len(mylists) # sets the number of people equal to the length of the list
    # reshuffle = "YES"
    
    
    print ("\nThe shuffled lists are\n")
    while numberofpeople > 0 and numberofgroups > 0:
        team = random.sample(mylists, int(numberofpeople/numberofgroups)) #draws from list. number sampled is taken by dividing number of people by number of groups
        for x in team:
            mylists.remove(x) #removes the member list after they are placed in group
        numberofpeople -= int(numberofpeople/numberofgroups) #reduces number of people by number of the sample
        numberofgroups -= 1 #reduces group number by 1
        print(team, "\n") #prints the sampled team

    
    while reset_loop_input != "N":
        reset_loop_input = input("Would you like to make another set of random teams? Enter Y to restart the program, R to reshuffle, or N to terminate: ") #terminates the program
        if reset_loop_input == "Y":
            break
        if reset_loop_input == "R":
            mylists = unshuffled.copy()
            numberofpeople = len(mylists)
            numberofgroups = int(input("How many groups do you want?\n")) #sets number of group
            ("\nThe reshuffled lists are\n")
            while numberofpeople > 0 and numberofgroups > 0:
                team = random.sample(mylists, int(numberofpeople/numberofgroups)) #draws from list. number sampled is taken by dividing number of people by number of groups
                for x in team:
                    mylists.remove(x) #removes the member list after they are placed in group
                numberofpeople -= int(numberofpeople/numberofgroups) #reduces number of people by number of the sample
                numberofgroups -= 1 #reduces group number by 1
                print(team, "\n") #prints the sampled team

quit()
