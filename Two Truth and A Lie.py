#importing random to use random method
import random



#setting my facts as variables
f1 = 'I support FC Barcelona'
f2 = 'I have a pitbull'
f3 = 'I like to think coding is easy'

#defining play again function
def play_again():
    user_input = input('Would you like to play again!?(Y/N): ')
    while user_input != 'Y' and user_input != 'N':
        user_input = input("Please Choose 'Y' for Yes or 'N' for No: ")
    if user_input == 'Y':
        return True
    else:
        return False


        
    
#set playing as true as default to run loop
playing = True


#playing game while playing is TRUE
while playing == True:

    
    #welcoming user to the game
    print('Welcome to TWO TRUTH AND A LIE')
    print()
    print()

    #setting variables for the game, trying variable for two trys,correct_counter to save their results, rand_num to choose a fact
    trying = 0
    correct_counter = 0
    rand_num = random.randint(1,3)

    #loop if theyve tried less than 2
    while trying < 2:

        #if elif statements to output respective facts
        if rand_num == 1:
            print('Truth or Lie???')
            print(f1)

            print()

            print('Select either:\n1 for Truth\n2 for Lie')
            print()

            #choice variable user input what they think is TRUE or FALSE and output respective result
            choice = input('What do you think??: ') 
            while choice != '1' and choice != '2':
                choice = input('Error. Please select only 1 for Truth or 2 for False.\Choice: ')

            if choice == '1':
                print('Correct!\nYou are right! That is True!')
                print()
                correct_counter += 1
            if choice == '2':
                print('Incorrect!\nYou are wrong! That is True')
                print()

            trying += 1
            rand_num = random.randint(2,3)
            

        elif rand_num == 2:
            print('Truth or Lie???')
            print(f2)

            print()

            
            print('Select either:\n1 for Truth\n2 for Lie')
            print()

            #choice variable user input what they think is TRUE or FALSE and output respective result
            choice = input('What do you think??: ')
            while choice != '1' and choice != '2':
                choice = input('Error. Please select only 1 for Truth or 2 for False.\nChoice: ')

            if choice == '1':
                print('Correct!\nYou are right! That is True!')
                print()
                correct_counter += 1
            if choice == '2':
                print('Incorrect!\nYou are wrong! That is True')
                print()

            trying += 1
            rand_num = random.randrange(1,3,2)
            

        else:
            print('Truth or Lie???')
            print(f3)

            print()

        
            print('Select either:\n1 for Truth\n2 for Lie')
            print()

            #choice variable user input what they think is TRUE or FALSE and output respective result
            choice = input('What do you think??: ')
            while choice != '1' and choice != '2':
                choice = input('Error. Please select only 1 for Truth or 2 for False.\nChoice: ')

            if choice == '2':
                print('Correct!\nYou are right! That is False!')
                print()
                correct_counter += 1
            if choice == '1':
                print('Incorrect!\nYou are wrong! That is False')
                print()

            trying += 1
            rand_num = random.randint(1,2)
        
            
    #output the user results of the game
    print('You got {} out of 2 correct.'.format(correct_counter))
                               
    #playing variable set the return of the play_again function, which ask user if they would like to continue or not             
    playing = play_again()
    




    

    
    

