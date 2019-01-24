# Guess the Number (version 1)
#Show introduction
#Choose random target
target = 10 # start with a known value

#Initialize a guess counter
#Loop forever
#Ask the user to for a guess
userGuess = input('Take a guess: ')
userGuess = int(userGuess)

#Increment guess counter
#If user's guess is correct, congratulate user, we're done
if userGuess == target:
    print ('You got it!')

#If user's guess is too low, tell user
elif userGuess < target:
    print ('Your guess was too low.')
#If user's guess is too high, tell user
else:
    print ('Your guess was too high.')
#If reached max guesses, tell answer correct answer, we're done.

#Next, we’ll add code to keep track of the number of guesses and allow the user to make multiple guesses:

# Guess the Number (version 2)
#Show introduction
#Choose random target
target = 10 # start with a known value
#Initialize a guess counter
guessCounter = 0

#Loop forever
while True:
#Ask the user to for a guess
    userGuess = input('Take a guess: ')
    userGuess = int(userGuess)
    
    #Increment guess counter
    guessCounter = guessCounter + 1

    #If user's guess is correct, congratulate user, we're done
    if userGuess == target:
        print ('You got it!')
        print ('It only took you', guessCounter, 'guess(es).')
        break
    #If user's guess is too low, tell user
    elif userGuess < target:
        print ('Your guess was too low.')
    #If user's guess is too high, tell user
    else:
        print ('Your guess was too high.')
    #If reached max guesses, tell answer correct answer, we're done.
    if guessCounter == 5:
        print ('Sorry, you did not get it in 5 guesses')
        print ('The number was:', target)
print ('Thanks for playing.')
'''
we’ll finally add in the randomization code.
We’ll also finish the program by building the introduction and add some constants to make it more flexible
'''
# Guess the Number (version 3)
import random
MAX_GUESSES = 5 # maximum number of guesses allowed
MAX_RANGE = 20 # highest possible number

#Show introduction
print ('Welcome to my Guess the Number program.')
print ('Guess my number between 1 and', MAX_RANGE)
print ('You will have', MAX_GUESSES, 'guesses.')

#Choose random target
target = random.randrange(1, MAX_RANGE + 1)

#Initialize a guess counter
guessCounter = 0

#Loop forever
while True:
    #Ask the user to for a guess
    userGuess = input('Take a guess: ')
    userGuess = int(userGuess)
    #Increment guess counter
    guessCounter = guessCounter + 1
    #If user's guess is correct, congratulate user, we're done
    if userGuess == target:
        print ('You got it!')
        print ('It only took you', guessCounter, 'guess(es).')
        break
    #If user's guess is too low, tell user
    elif userGuess < target:
        print ('Your guess was too low.')
    #If user's guess is too high, tell user
    else:
        print ('Your guess was too high.')
    #If reached max guesses, tell answer correct answer, we're done.
    if guessCounter == MAX_GUESSES:
        print ('Sorry, you did not get it in', MAX_GUESSES, 'guesses.')
        print ('The number was:', target)
        break
print ('Thanks for playing.')


## Playing the Game multiple times

'''
#
Playing multiple games loop
    Play multiple rounds of the current game
        Play a round or move within a game
    Ask if the user wants to play again, if not, exit
The implementation would consist of an outer while loop, and another inner while loop that plays a
single round. After the end of the inner loop, we ask the user if they want to play again. If they do, the outer
loops runs again, and the game restarts.
The other approach is to take the code that implements one round, and put that inside a function.
Then the main code can be a simple loop that calls the function to play a round of the game. Let’s build that
version. We’ll move all the code dealing with one round into a function called playOneRound
'''
# Guess the Number (version 4)
import random
MAX_GUESSES = 5 # maximum number of guesses allowed
MAX_RANGE = 20 # highest possible number
#Show introduction
print ('Welcome to my Guess the Number program.')
print ('Guess my number between 1 and', MAX_RANGE)
print ('You will have', MAX_GUESSES, 'guesses.')

def playOneRound():
    #Choose random target
    target = random.randrange(1, MAX_RANGE + 1)
    #Initialize a guess counter
    guessCounter = 0
    #Loop forever
    while True:
        #Ask the user to for a guess
        userGuess = input('Take a guess: ')
        userGuess = int(userGuess)
        #Increment guess counter
        guessCounter = guessCounter + 1
        #If user's guess is correct, congratulate user, we're done
        if userGuess == target:
            print ('You got it!')
            print ('It only took you', guessCounter, 'guess(es).')
            break
        #If user's guess is too low, tell user
        elif userGuess < target:
            print ('Your guess was too low.')
        #If user's guess is too high, tell user
        else:
            print ('Your guess was too high.')
        #If reached max guesses, tell answer correct answer, we're done.
        if guessCounter == MAX_GUESSES:
            print ('Sorry, you did not get it in', MAX_GUESSES, 'guesses.')
            print ('The number was:', target)
            break

#main code
while True:
    playOneRound() # call a function to play one round of the game
    goAgain = input('Play again? (Press ENTER to continue, or q to quit): ')
    if goAgain == 'q':
        break
print ('Thanks for playing.')


#To ensure a fully functional game, we’ll add in a try/except block to catch potential user errors:
# Guess the Number (version 5 - final)
import random
MAX_GUESSES = 5 # maximum number of guesses allowed
MAX_RANGE = 20 # highest possible number
#Show introduction
print ('Welcome to my Guess the Number program.')
print ('Guess my number between 1 and', MAX_RANGE)
print ('You will have', MAX_GUESSES, 'guesses.')

def playOneRound():
    #Choose random target
    target = random.randrange(1, MAX_RANGE + 1)
    #Initialize a guess counter
    guessCounter = 0
    #Loop forever
    while True:
        #Ask the user to for a guess
        userGuess = input('Take a guess: ')
        # Check for potential error
        try:
            userGuess = int(userGuess)
        except:
            print ('Hey, that was NOT an integer!')
            continue
        #Increment guess counter
        guessCounter = guessCounter + 1
        #If user's guess is correct, congratulate user, we're done
        if userGuess == target:
            print ('You got it!')
            print ('It only took you', guessCounter, 'guess(es).')
            break
        #If user's guess is too low, tell user
        elif userGuess < target:
            print ('Your guess was too low.')
        #If user's guess is too high, tell user
        else:
            print ('Your guess was too high.')
        #If reached max guesses, tell answer correct answer, we're done.
        if guessCounter == MAX_GUESSES:
            print ('Sorry, you did not get it in', MAX_GUESSES, 'guesses.')
            print ('The number was:', target)
            break
#main code
while True:
    playOneRound() # call a function to play one round of the game
    goAgain = input('Play again? (Press ENTER to continue, or q to quit): ')
    if goAgain == 'q':
        break
print ('Thanks for playing.')




