#Nicolas Ayala-Alonso
#functions
#Main
replies=[]
y=0
import random
def responses():
    global y
    replies.append("Hell yeah")
    replies.append("Absolutely")
    replies.append(" Yes!")
    replies.append("You bet!")
    replies.append("Without fail!")
    replies.append("Nah")
    replies.append("mmmmm.... yeah no")
    replies.append("Never")
    replies.append("Under no circumstances")
    replies.append("Negative")
    replies.append("perchance")
    replies.append("Potentially")
    replies.append("Wind and weather permitting")
    replies.append("mayhap")
    replies.append("perhaps..")
    y=random.choice(replies)

def userint():
    while True:
        global y
        x=userint
        x=input("Please enter your question")
        if x.endswith("?"):
            responses()
            print(y)
        else: print("Error, please enter your question again. Make sure it ends with ?")
        g=input("Would you like to make another question? enter yes or no")
        if g=="yes":
            print("Okay")

        else:
            break
#Main
userint()
