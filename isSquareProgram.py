'''
Create a program that contains a function called isSquare . The function is passed two parameters that
represent the length and the width of a shape. For simplicity, assume that we are talking about a rectangle,
where the top and bottom sides are the same width, the left and right sides are the same length, and all
angles are 90-degree. isSquare should return one of the following:
• True, if the sides represent a square
• False, if the sides do not represent a square
The function should not print anything.
Write some main program code to call the function with test values for the length and the width of the
sides, and print the following based on the returned result:
xxx and yyy represent a square or xxx and yyy do not represent a square
Allow the user to enter values. Use them in your function call and then print based on
the results.
'''
# Determine if two numbers represent a square
# Function to determine if length and width represent a square
def isSquare(length, width):
    if length == width:
        itsASquare = True
    else:
        itsASquare = False
    return itsASquare

# Intermediate function that checks for a square and prints the result
def printSquare(aLength, aWidth):
    theResult = isSquare(aLength, aWidth)
    if theResult:
        print (aLength, 'and', aWidth, 'represent a square')
    else:
        print (aLength, 'and', aWidth, 'do not represent a square')

#Test cases
printSquare(5, 5)
printSquare(7.5, 8.5)

# Get user inputconvert to floats and call the function.
userLength = input('Enter a length: ')
userLength = float(userLength)
userWidth = input('Enter a width: ')
userWidth = float(userWidth)
printSquare(userLength, userWidth)
