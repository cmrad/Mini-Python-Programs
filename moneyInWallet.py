# simple program to add up the value of all the one-dollar bills,
#five-dollar bills,and ten-dollar-bills that are in a wallet.

nOneDollarBills = 2
nfiveDollarBills = 8
nTenDollarBills=4
nTwentyDollarBills=5
total = nOneDollarBills + (nfiveDollarBills * 5)+(nTenDollarBills*10)\
        +(nTwentyDollarBills*20)
print ('Total amount is:', total)


# Calculate the amount of money interactively
# Use input to get info from the user
nOnes = input('How many ones do you have? ')
nFives = input('How many fives do you have? ')
nTens = input('How many tens do you have? ')
nTwenties = input('How many twenties do you have? ')
# Use int to convert the inputted strings to integer values before multiplying
total = int(nOnes) + (int(nFives) * 5) + (int(nTens) * 10) + (int(nTwenties) * 20)
# Use str to convert to a string, then concatenate on a decimal point and zeros
totalAsString = str(total) + '.00'
# Concatentate strings and print
print ('You have $' + totalAsString)
