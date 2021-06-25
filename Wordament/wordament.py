# This is a script for game 'Wordament'

#--- First Part is to create a new game.
#--- For each play, the elements include:
#---     a 4x4 table in which every grid has a letter

import enchant
endict = enchant.Dict("en_UK")
import random
import string
    
class Wordament(object):
    def __init__(self, flag=False, bonus=False,
                 letters=["L","N","A","R",
                          "E","S","P","B",
                          "T","R","A","NT",
                          "R","E","I","J"],
                 scores=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]):
        
        self.flag = flag
        self.bonus = bonus
        self.letters = letters
        self.scores = scores
        
        ###

        
        
        
        ###
        self.highscores = []
        self.highscore(30)


    def find_paths(self, start_point=0):
        
        
        
        return
    
    
    # def answer(self):
        
    #     self.answer = answer_words
    #     return
    
    
    # def highscore(N=10):
    #     if len(self.highscores) < N:
    #         self.answer()
    #     print(self.highscores[:N])    
    #     return
    
    
    def show_list(self):
        #self.highscores
        highscores = ""
        print(highscores)
        return
    
    def calculate_score(scores_list):
        length = len(scores_list)
        the_score = 0
        return the_score
        
    # def shuffle(self):
    #     for i in range(16):
    #         #one_letter = random.sample(string.ascii_uppercase, 1)
    #         k = random.randint(0,25)
    #         one_letter = string.ascii_uppercase[k]
    #         self.letters.append((one_letter))    
            
    def refresh(self):
        self.flag = True
        self.index_list=[]
        
    def search_from(self, an_index):
        #self.index_list[]
        return
        
    def next_index(an_index):
        new_i = 100
        new_up = an_index - 4
        return
        
###################


def neighbour(grid_index):
    return

def generate_letters(s="L N A R E S P B T R A NT R E I J"):
    letters = s.split(" ")
    if len(letters) == 16:
        string = " ".join(letters)
        print("Grid letters have been successfully generated. Letters = [{0}]".format(string))
        return letters
    else:
        print("WARNING: Letter generation failed! There should be 16 letters in total!")
        return
    
    
generate_letters(s="a b c d e f g h i j k l m n o p")
    
############################################################################## abandon

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

# a = GenerateGame(letters="LSDIOABCUEMWQLXY",play=True)
# B = GenerateGame(play=True)

def Find_16(all_letters, show=True):
    answers = []
    
    if show==True:
        for answer in answers:
            print(answer)
    return answers

