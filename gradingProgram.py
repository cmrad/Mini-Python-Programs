''''
Here is a real-world example of using if/elif/else statements. Teachers often grade tests, projects, and
homework assignments using a number scale of 0 to 100. At the end of the term, the final grading number
needs to be converted to a letter grade. Here is a sample function that could be used to do this conversion:
'''

#Convert a number score to a letter grade:
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F' #fall through or default case
    return letter

grade1 = letterGrade(75)
print (grade1)
grade2 = letterGrade(82)
print (grade2)
print (letterGrade(95)) #call and print in one statement
