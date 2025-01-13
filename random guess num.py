#Nicolas A. Ayala-Alonso
import random
print("welcome to number guesing game, please pay $5 to play")
print("To play this game you guess a number, and if it is correct then you win the grand prize for the day. If wrong you win nothing")
print("Please select difficulty: e, m, h")
diff = input("Please select difficutly: ")
if diff == "e" :
    easysecret =  random.randint(0,10)
    easyguess=(input("please eneter a number from 1 to 10: "))
    if int(easyguess)==easysecret:print("Correct, you've won the jackpot")
    elif int(easyguess)>=easysecret: print("Your guess was too large")
    else:print("Your number was too small")
    if easyguess != easysecret :print("Incorrect, if you want to try again it will be $5, remember 99% of gamblers quit before they make it big")
if diff =="m":
    mediumsecret =  random.randint(0,30)
    mediumguess=(input("please enter a number from 1 to 30: "))
    if int(mediumguess)==mediumsecret: print("Correct, you've won the jackpot")
    elif int(mediumguess)>=mediumsecret: print("Your guess was too large")
    else: print("Your guess was too small")
    if mediumguess!= mediumsecret:print("Incorrect,if you want to try again it will be $5, remember 99% of gamblers quit before they make it big")

if diff=="h":
    hardsecret =  random.randint(0,100)
    hardguess=(input("please enter a number from 1 to 100: "))
    if int(hardguess)==hardsecret: print("Correct, you've won the jackpot")
    elif int(hardguess)>=hardsecret: print("Your guess was too large")
    else:print("Your number was too small")
    print("Incorrect, if you want to try again it will be $5, remember 99% of gamblers quit before they make it big")

guess =  int(input("Enter your guess"))
easysecret =  random.randint(0,10)
mediumsecret =  random.randint(0,30)
hardsecret =  random.randint(0,100)



