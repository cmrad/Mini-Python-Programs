#Let’s try side lengths of 3 and 4, and
#see what our program generates for the hypotenuse:

side1 = 3
side2 = 4
hypot = ((side1 ** 2) + (side2 ** 2)) ** 0.5
print ('Side 1 is', side1, ' Side 2 is', side2, ' Hypotenuse is:', hypot)


def calculateHypotenuse(side1, side2):
    side1= float(side1)
    side2 = float(side2)
    hypot = ((side1 ** 2) + (side2 ** 2)) ** 0.5
    return hypot

firstTriangleSide1 = input('Enter side 1: ')
firstTriangleSide2 = input('Enter side 2: ')
hypot1 = calculateHypotenuse(firstTriangleSide1, firstTriangleSide2) # call function to do calc
secondTriangeSide1 = input('Enter the first side: ')
secondTriangeSide2 = input('Enter second side: ')
hypot2 = calculateHypotenuse(secondTriangeSide1, secondTriangeSide2) # call function to do calc
print( 'The hypotenuse of the first triangle is: ', hypot1)
print ('The hypotenuse of the second triangle is: ', hypot2)
