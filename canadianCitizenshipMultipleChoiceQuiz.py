from question import question
questionPrompts= [
    "In whose honour is Mount Logan named for?\n(a)an athlete\n(b)an aboriginal\n(c) a famous gelogist and a great scientist\n\n",
    "Which is the smallest province in land mass?\n(a)Nova Scotia\n(b) Prince Edward Island\n(c)Newfoundland and Labrador\n\n",
    "What is the highest honour that Canadian's can receive?\n(a)Victoria Cross\n(b)Purple Cross\n(c)Order of the British Empire\n\n"
    ]

questions=[
    question(questionPrompts[0],"c"),
    question(questionPrompts[1],"b"),
    question(questionPrompts[2],"a"),
    ]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer== question.answer:
            score+=1
    print("You got "+ str(score)+ "/" +str(len(questions))+"correct")
    
run_test(questions)
