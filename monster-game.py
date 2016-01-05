import random

# setup variables
myloc = 0,0
monsterloc = 0,0
doorloc = 0,0
x = list(range(20))
y = list(range(20))
square = ()
grid = list()

#build grid
for items in x:
    square = (x[items], y[items])
    grid.append(square)

# Start game
while TRUE:
    print("You are in a dark dungeon. There is no light. Somewhere here there is a door you must find before the monster within captures and devours you.")
    action = input("Type MOVE to begin your search.")

    if action == 'MOVE':
        myloc = move(myloc)
    
        if myloc == monsterloc:
            print("AAAAAHHHHHH! The monster is feasting upon your flesh! GAME OVER")
        elif myloc == doorloc:
            print("You feel a cold round knob, you turn it a light floods the room. You slip through the door and live to see another day! GAME OVER")
        else:
            print("You are safe for now, but you must find that door! You are located in square {}, {}.")
            action = input("Type MOVE to search for the doo.")
    else:
        print("That's not a command I recognize.") 
        action = input("Type MOVE to search for the door.")   
    
    
# Move command    
def move(theloc):
    myloc == random.choice(grid)
    monsterloc == random.choice(grid)
    
    if theloc == myloc:
        print("You're stick in quicksand. You tried to move but you can't.")
    
    return myloc