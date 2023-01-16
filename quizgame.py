print('Welcome to the game of greed!')
start= input("Do you want to play?  ")
if(start.lower()!="yes"):
    quit()
else:
    print("Let us play")
score=0
que=input("What is the capital of India?\n")
if (que=="New Delhi"):
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT")
que=input("What is the capital of UTTAR PRADESH?\n")
if (que=="Lucknow"):
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT")
que=input("What is the capital of madhya pradesh?\n")
if (que=="Bhopal"):
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT")
que=input("What is the capital of maharastra?\n")
if (que=="Mumbai"):
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT")
que=input("What is the capital of gujarat?\n")
if (que=="Gandhinagar"):
    print("CORRECT!")
    score=score+1
else:
    print("INCORRECT")
percent=score/5*100
print("correct answers are " + str(score) + " and percentage is " + str(percent))

if (percent==100):
    print('PERFECT')
elif (75<=percent<100):
    print("ALMOST PERFECT")
elif(50<=percent<75):
    print("GOOD")
elif(25<=percent<50):
    print("AVERAGE")
else:
    print("WORK HARD")