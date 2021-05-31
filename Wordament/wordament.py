# This is a script for game 'Wordament'

#--- First Part is to create a new game.
#--- For each play, the elements include:
#---     a 4x4 table in which every grid has a letter

import enchant
endict = enchant.Dict("en_UK")
import random
import string

def GenerateGame(play=True):
    
    # randomly generate letters in grids
    all_letters = []
    one_letter = random.sample(string.ascii_uppercase, 1)
    all_letters.append((one_letter))
    
    # show game in terminal if play==True
    if play == True:
        for i in range(16):
            if i != 0 and i%4 == 0:
                print("\n")
            print(all_letters[i], " ")
            
    # need alphabet and dictionary
    return

GenerateGame()