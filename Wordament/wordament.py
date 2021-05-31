# This is a script for game 'Wordament'

#--- First Part is to create a new game.
#--- For each play, the elements include:
#---     a 4x4 table in which every grid has a letter

import enchant
endict = enchant.Dict("en_UK")
import random
import string

def GenerateGame(letters=False, play=False):
    all_letters = []
    if letters == False:
        # randomly generate letters in grids
        for i in range(16):
            #one_letter = random.sample(string.ascii_uppercase, 1)
            k = random.randint(0,25)
            one_letter = string.ascii_uppercase[k]
            all_letters.append((one_letter))
        

            
    if letters:
        # pre-asign letters
        # format should be like letters="abcdabcdabcdabcd" length=16
        if isinstance(letters, str):
            if len(letters)==16:
                print("ok self-defined letter grid received.")
                all_letters = list(letters)
            else:
                print("letters should be a string of 16 letters")
                return
        else:
            print("letters should be a string of 16 letters")
            
        # show game in terminal if play==True
    if play == True:
        for i in range(16):
            if i != 0 and i%4 == 0:
                print(" ")
            print(all_letters[i], end=' ')
        print("\n")
    return all_letters

a = GenerateGame(letters="LSDIOABCUEMWQLXY",play=True)
B = GenerateGame(play=True)

def Find_16(all_letters, show=True):
    answers = []
    
    if show==True:
        for answer in answers:
            print(answer)
    return answers
