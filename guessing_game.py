import random
guesses = 0

def picknum(myguess, guesses):
    thenum = 0
    if guesses <=3:
        thenum = random.randint(1,10)
        
        if myguess == thenum:
            print("Holy shit! You're a super genius! Your guess {} is the same as the computer's number: {}.".format(myguess,thenum))
        else:
            print("Wrong guess! You guessed {}. The computer's number is {}.".format(myguess,thenum))
    else:
        print("Sorry. You've made {} guesses. That's too many. Game over, dude.".format(guesses))
    
    return thenum

print("Pick a number between 1 and 10.")
picknum(input("> "), guesses)
guesses+=1