'''
Created on Sep 8, 2015

@author: Isaac
'''
import random, sys, time

class Cards:
    def __init__(self, deck, randomCard, deckC):
        self.deck = deck
        self.randomCard = randomCard
        self.deckC = deckC
    def Rcard(self): 
        '''Picks a random card from the deck'''
        randomCard1 = random.randint(0,13)
        randomCard2 = random.randint(0,13)
        self.randomCard = [randomCard1,randomCard2]
        return self.randomCard
    
    def addCard(self):
        '''Adds another card for player'''
        randomCard5 = random.randint(0,13)
        deck.append(randomCard5)
        howLong = len(deck) - 1
        e = deck[howLong]
        v = self.deck[e] ### Had to put the randomized # into the dictionary key
        print()
        print("\t\t* * * * *")
        print("\t\t*" "\t*")
        print("\t\t*   {0}"  "\t*".format(v))
        print("\t\t*      " " *")
        print("\t\t* * * * *")
        return " " 
    
    def addCardComp(self):
        '''Adds another card for computer'''
        randomCard5 = random.randint(0,13)
        deckC.append(randomCard5)
        howLong = len(deckC) - 1
        c = deckC[howLong]
        v = self.deckC[c] ### Had to put the randomized # into the dictionary key
        print()
        print("\t\t* * * * *")
        print("\t\t*" "\t*")
        print("\t\t*   " + v + "\t*")
        print("\t\t*      " " *")
        print("\t\t* * * * *")
        return " "
    
    def actions(self):
        '''Hit or stay. Will also check if player or computer busted or stayed'''
        
        x = input("HIT or STAY? 1 = HIT or 2 = STAY:")
        return x
    
    def blackjack(self):
        '''Tells player or computer if they got a blackjack. Or if both got a blackjack then shoot to won method '''
        x = Cards.cardStart(self)
        if x == 1: ### 1 means player got a blackjack, 2 computer, and 3 is tied
            print("You got a BLACKJACK!!!")
            time.sleep(1)
            print("BLACKJACK!!!")
            time.sleep(1)
            print("BLACKJACK!!!")
            return 1
        elif x == 2:
            print("Dealer BLACKJACKED!")
            return 2
        elif x == 3:
            print("Wow both got a BlackJack...crazy")
            return 3
        elif x == 4:
            return 4
        else:
            return("ERROR BLACKJACK METHOD")
    
    def cardStart(self):
        '''Displays 2 player cards and 2 computer cards at the start of game '''
        a = deckC[0] ### w,y,x,z are the 4 randomly generated cards to display
        b = deckC[1] ### deck was generated from Rcard function in class then passed to MAIN to freeze the #'s
        c = deck[0] ### the frozen #'s are then passed back to this function
        d = deck[1]
        w = self.deckC[a] ### Had to put the randomized #'s into the dictionary keys for the following
        x = self.deckC[b]
        y = self.deck[c]
        z = self.deck[d]
        print(w) ### GET RID OF THIS AFTER TESTING!!!!!!!!!!!!!!

        print("\t\t* * * * *\t* * * * *")
        print("\t\t*"  "\t*\t*"  "\t*")
        print("\t\t*\t*\t*   " + x + "\t*")
        print("\t\t*    "  "   *\t*    "  "   *")
        print("\t\t* * * * *\t* * * * *")
        print("------------------------------------------------------------------")
        print("\t\t* * * * *\t* * * * *")
        print("\t\t*" "\t*\t*"  "\t*")
        print("\t\t*   " + y + "\t*\t*   " + z + "\t*")
        print("\t\t*    "  "   *\t*    "  "   *")
        print("\t\t* * * * *\t* * * * *")
        ####Logic below is finding if there are any starting blackjacks####
        if (z == "A" and (y == "10" or y == "J" or y == "Q" or y == "K")) and (x == "A" and (w == "10" or w == "J" or w == "Q" or w == "K")) :
            return 3 ### each of these 3 (tie),2 (comp),1 (player) is telling blackjack method if anyone has a blackjack
        elif (w == "A" and (x == "10" or x == "J" or x == "Q" or x == "K")) and (y == "A" and (z == "10" or z == "J" or z == "Q" or z == "K")) :
            return 3
        elif w == "A" and (x == "10" or x == "J" or x == "Q" or x == "K"):
            return 2
        elif x == "A" and (w == "10" or w == "J" or w == "Q" or w == "K"):
            return 2
        elif y == "A" and (z == "10" or z == "J" or z == "Q" or z == "K"):
            return 1
        elif z == "A" and (y == "10" or y == "J" or y == "Q" or y == "K"):
            return 1
        else:
            return 4 ### No blackjack
        
    def won(self):
        '''This will check if someone has won or busted'''
        ###Variables players deck###
        calDeck = deck
        calDeck = [10 if x==11 or x ==12 or x==13 else x for x in calDeck] ### This comprehensive list replaces 11,12,13 with 10 in deck so can calculate score
        calDeck = [11 if x==0 else x for x in calDeck]### Turns all A's to value 11 by default
        calDeckSum = sum(calDeck)
        if calDeckSum > 21:
            calDeck = [1 if x==11 else x for x in calDeck] ### if 11 (Ace) in deck and sum is > 21 the A's value will change to 1
            ### FIGURE OUT how to - 10 if A in deck calDeckSum = calDeckSum - 10
        print(calDeck)
        print(calDeckSum)
        ###Variables computers deck###
        calDeckC = deckC
        calDeckC = [10 if x==11 or x ==12 or x==13 else x for x in calDeckC] ### this changes all 11, 12, or 13 to value of 10 for Computers hand.
        calDeckC = [11 if x==0 else x for x in calDeckC]### Turns all A's to value 11 by default
        calDeckCSum = sum(calDeckC)
        if calDeckCSum > 21:
            calDeckC = [1 if x==11 else x for x in calDeckC] ### if 11 (Ace) in deck and sum is > 21 the A's value will change to 1
            ### FIGURE OUT HOW TO - 10 from sum if A calDeckCSum = [-10 if x==11 else x for x in calDeckC]
        print(calDeckC)
        print(calDeckCSum)
        ###Logic for player busting/win ###
        if calDeckSum > 21:
            return 2 ### This is returning that the player lost b/c they busted
        elif calDeckSum <= 21:
            print("HELLO")
            return 4 ### No one has won or busted
        else:
            return "ERROR WON METHOD"
        ###Logic for computer busting/win ###
        if calDeckCSum <= 21 and calDeckCSum > 0:
            return 4 ### No one has won or busted
        elif calDeckCSum > 21:
            return 1 ### This is returning that the player won b/c computer busted
        else:
            return "ERROR WON METHOD"
        
class Players:
    def __init__(self, player, comp):
        self.player = player
        self.comp = comp
    def tallyScore(self):
        pass
        
        
################## VARIABLES ##################
deck = {0:"A",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}
deckC = {0:"A",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"} ### computer's deck only for adding cards
randomCard = "0"
player = 0 ### This variable will be passed to Players method to keep the score for player
comp = 0 ### This variable will be passed to Players method to keep the score for computer
pWon = 0 ### Need to pass this to won method in Cards class so this can tally, then Players-
         ### class will keep the score (I am using 2 classes to practice inheritance
cWon = 0 ### This is same as pWon but for computer

clear = "\n" * 100 ### clears the screen 
################## MAIN ######################

x = Cards(deck, randomCard, deckC)
y = Players(player, comp)
deck = x.Rcard() ### This grabs and freezes the 4 randomly generated #’s
deckC = x.Rcard()
while True:

    winner = x.blackjack()     
    winner1 = x.won()
                                  ### The frozen cards are 1st going to cardStart then to blackjack then to won methods. 
                    ###This starts the chain. 
        
    while True:
        
        if winner == 1 or winner1 == 1:
            again = input("You WON this round. Play again? 1 YES 2 NO:")
            if again == "1":
                print(clear)
                break
            elif again == "2":
                print("OK then, it was fun playing. Goodbye.")
                sys.exit(0)
            else:
                print("Come-on-now, enter either a 1 or 2!")
                continue
        elif winner == 2 or winner1 == 2:
            again = input("You LOST this round. Play again? 1 YES 2 NO:")
            if again == "1":
                print(clear)
                break
            elif again == "2":
                print("OK then, it was fun playing. Goodbye.")
                sys.exit(0)
            else:
                print("Come-on-now, enter either a 1 or 2!")
                continue
        elif winner == 3 or winner1 == 3:
            again = input("You TIED this round. Play again? 1 YES 2 NO:")
            if again == "1":
                print(clear)
                break
            elif again == "2":
                print("OK then, it was fun playing. Goodbye.")
                sys.exit(0)
            else:
                print("Come-on-now, enter either a 1 or 2!")
                continue
        elif winner == 4 or winner1 == 4: ### No blackjack
                pass
        else:
            print("ERROR MAIN")
            continue
        #move = x.actions() 
        while True:
            move = x.actions() ### Asking player to hit or stay
            if move == "1":
                x.addCard()
                x.won() ### checking if anyone won
                print(winner)
                print(winner1)
                break
            elif move == "2": ### Even if player stays the computer still needs a card
                x.addCardComp()
                x.won()
                break 
            else:
                print("Come-on-now, enter either a 1 or 2!")
                continue
            
