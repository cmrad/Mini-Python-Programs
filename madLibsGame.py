'''
Let’s build an old, popular game: Mad Libs. We’ll start by getting input from the user, just like in a real Mad
Libs game, and use the user’s responses in our story. The starting version of this game has nothing to do with
lists, but once we build the base game, we’ll modify it to use lists.
'''

# MadLib (version 1)
while True:
    name = input('Enter a name: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    noun = input('Enter a noun: ')
    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + \
    adjective + ' ' + noun + '.'
    print()
    print (sentence)
    print()
    # See if the user wants to quit or continue
    answer = input('Type "q" to quit, or anything else (even Return/Enter) to continue:')
    if answer == 'q':
        break
print ('Bye')
'''
Now, we’ll change the program. Rather than having the user enter a name, we’ll build a pool of names and
select one randomly for the user. The pool of predetermined names will be built as a list. We could use any
names for our list, but to make our Mad Libs game fun, our list will look like this:
'''

namesList = ['Roberto Manrique', 'The Teenage Mutant Ninja Turtles', 'Carmen Villalobos', \
'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
'The Beatles', 'Maluma', 'The Pillsbury Doughboy']

'''
Next, we want to choose a random name from this list. This particular list has nine elements in it.
In order to select a random element from the list, we need to generate a random index between 0 and 8
(remember, list indices start at zero).
'''

import random
##randomIndex = random.randrange (<lowerLimit>, <upToButNotIncluding>)

'''
Again, our goal is to select a random number to use as an index of an element in the list. With our list of
nine names, we would call random.randrange , passing in a 0 and a 9. It would return a random integer of 0
to 8 (up to but not including 9). The resulting program would look like this:
'''

# MadLib (version 2)
import random
namesList = ['Roberto Manrique', 'The Teenage Mutant Ninja Turtles', 'Carmen Villalobos', \
'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
'The Beatles', 'Maluma', 'The Pillsbury Doughboy']
while True:
    nameIndex = random.randrange(0, 9) # Choose a random index into the namesList
    name = namesList[nameIndex] # Use the index to choose a random name
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    noun = input('Enter a noun: ')
    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + \
               adjective + ' ' + noun + '.'
    print()
    print (sentence)
    print()
    # See if the user wants to quit or continue
    answer = input('Type "q" to quit, or anything else (even Return/Enter) to continue: ')
    if answer == 'q':
        break
print ('Bye')


# MadLib (version 3)
import random
namesList = ['Roberto Manrique', 'The Teenage Mutant Ninja Turtles', 'Carmen Villalobos', \
'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
'The Beatles', 'Maluma', 'The Pillsbury Doughboy', 'Ellen Degeneres']
nNames = len(namesList) # find out how many names are in the list of names

while True:
    nameIndex = random.randrange(0, nNames) # Choose a random index into the namesList
    name = namesList[nameIndex] # Use the index to choose a random name
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    noun = input('Enter a noun: ')
    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + \
    adjective + ' ' + noun + '.'
    print()
    print (sentence)
    print()
    # See if the user wants to quit or continue
    answer = input('Type "q" to quit, or anything else (even Return/Enter) to continue:')
    if answer == 'q':
        break
print ('Bye')

'''
Notice that in this version, we’ve added another name to our list of names. But we also used the len
function to set a variable, nNames , to the number of elements in our list of names. Finally, we used that
variable in our call to randrange . Using this approach, we can put as many names in our list as we wish, and
the code will adjust at runtime for us.
'''

'''
Similar to the modification to use a list of names, let’s modify the program to include a list of verbs, a list of
adjectives, and a list of nouns. The program should randomly choose a name, a verb, an adjective, and a
noun. You can put as many elements as you want into each list, and the program should create and print a
fully randomized Mad Lib.
'''

# MadLib (version 4)
import random

namesList = ['Roberto Manrique', 'The Teenage Mutant Ninja Turtles', 'Carmen Villalobos', \
'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
'The Beatles', 'Maluma', 'The Pillsbury Doughboy', 'Ellen Degeneres']
nNames = len(namesList) # find out how many names are in the list of names
verbsList = ['screamed', 'burped', 'ran', 'galumphed', 'rolled', 'ate', 'laughed', \
'complained', 'whistled']
nVerbs = len(verbsList)
adjectivesList = ['purple', 'giant', 'lazy', 'curly-haired', 'wireless electric', \
'ten foot tall']
nAdjectives = len(adjectivesList)
nounsList = ['ogre', 'dinosaur', 'Frisbee', 'robot', 'staple gun', 'hot dog vendor', \
'tortoise', 'rodeo clown', 'unicorn', 'Santa hat', 'garbage can']
nNouns = len(nounsList)


while True:
    nameIndex = random.randrange(0, nNames) # Choose a random index into the namesList
    name = namesList[nameIndex] # Use the index to choose a random name
    verbIndex = random.randrange(0, nVerbs)
    verb = verbsList[verbIndex]
    adjectiveIndex = random.randrange(0, nAdjectives)
    adjective = adjectivesList[adjectiveIndex]
    nounIndex = random.randrange(0, nNouns)
    noun = nounsList[nounIndex]
    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + \
    adjective + ' ' + noun + '.'
    print()
    print (sentence)
    print()
    # See if the user wants to quit or continue
    answer = input('Type "q" to quit, or anything else (even Return/Enter) to continue:')
    if answer == 'q':
        break

print('bye')

'''
In the prior code, you may have noticed a pattern. For each of the four lists ( nounsList , verbsList ,
adjectivesList , and nounsList ), we have built essentially the same code. Whenever we wanted to select
a random element, we chose a random index, and then found the element at that index. While this clearly
works, whenever we see essentially the same code repeated, that is a signal that it is probably a good
candidate to turn into a function. In this case, rather than repeating the same set of operations four times,
we’ll build a single function to select a random element from a list and call it four times.
'''

# MadLib (version 5)
import random
def chooseRandomFromList(aList):
    nItems = len(aList)
    randomIndex = random.randrange(0, nItems)
    randomElement = aList[randomIndex]
    return randomElement
namesList = ['Roberto Manrique', 'The Teenage Mutant Ninja Turtles', 'Carmen Villalobos', \
'The Stay Puft Marshmallow Man', 'Shrek', 'Sherlock Holmes', \
'The Beatles', 'Maluma', 'The Pillsbury Doughboy', 'Ellen Degeneres']
verbsList = ['screamed', 'burped', 'ran', 'galumphed', 'rolled', 'ate', 'laughed', \
'complained', 'whistled']
adjectivesList = ['purple', 'giant', 'lazy', 'curly-haired', 'wireless electric', \
'ten foot tall']
nounsList = ['ogre', 'dinosaur', 'Frisbee', 'robot', 'staple gun', 'hot dog vendor', \
'tortoise', 'rodeo clown', 'unicorn', 'Santa hat', 'garbage can']

while True:
    name = chooseRandomFromList(namesList)
    verb = chooseRandomFromList(verbsList)
    adjective = chooseRandomFromList(adjectivesList)
    noun = chooseRandomFromList(nounsList)
    sentence = name + ' ' + verb + ' through the forest, hoping to escape the ' + \
    adjective + ' ' + noun + '.'
    print()
    print (sentence)
    print()
    # See if the user wants to quit or continue
    answer = input('Type "q" to quit, or anything else (even Return/Enter) to continue:')
    if answer == 'q':
        break
print ('Bye')

'''
In this version, we’ve built a small function called chooseRandomFromList . It is designed to expect to
have one parameter passed in when it is called. It is expected to be passed in a list. The aList parameter
variable takes on the value of the list passed in. We used a very generic name here because we do not know
what the contents of the list are, and inside the function, we do not care. The function uses the len function
to see how many items are in the list, chooses a random index, finds the element at that index, and returns
that element. From the main code, we now call the function four times, passing in four different lists. This
version of the code generates the same type of Mad Libs sentences as the earlier version, but it is easier to
read and is less prone to errors.
'''

