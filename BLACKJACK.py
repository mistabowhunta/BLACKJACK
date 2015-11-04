'''
Created on Sep 8, 2015

@author: Isaac

The MIT License (MIT)
Copyright (c) [2015] [Isaac Nason]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import random, sys, time

class Cards:
    def __init__(self, deck, randomCard, deckC, calDeckSum, calDeckCSum):
        self.deck = deck
        self.randomCard = randomCard
        self.deckC = deckC
        self.calDeckSum = calDeckSum
        self.calDeckCSum = calDeckCSum
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
        v = self.deck[e] ### Had to put the randomized # into the dictionary key to get face card
        
        print()
        print("\t\t* * * * *")
        print("\t\t*" "\t*")
        print("\t\t*   {0}"  "\t*".format(v))
        print("\t\t*      " " *")
        print("\t\t* * * * *")
        calDeck = deck
        calDeck = [10 if x==11 or x ==12 or x==13 else x for x in calDeck] ### This comprehensive list replaces 11,12,13 with 10 in deck so can calculate score
        calDeck = [11 if x==0 else x for x in calDeck]### Turns all A's to value 11 by default
        #calDeckSum = self.calDeckSum 
        self.calDeckSum = sum(calDeck)
        #self.calDeckSum = calDeckSum ### have to assign global variable so I can use it in addCard methods TEST this
        if self.calDeckSum > 21:
            calDeck = [1 if x==11 else x for x in calDeck] ### if 11 (Ace) in deck and sum is > 21 the A's value will change to 1
        #print(calDeck) just needed for testing to see the deck
        
        self.calDeckSum = sum(calDeck)
        #self.calDeckSum = calDeckSum
        #print(self.calDeckSum)
        return self.calDeckSum
    
    def addCardComp(self):
        '''Adds another card for computer'''
        while True:
            
            calDeckC = deckC
            calDeckC = [10 if x==11 or x ==12 or x==13 else x for x in calDeckC] ### this changes all 11, 12, or 13 to value of 10 for Computers hand.
            calDeckC = [11 if x==0 else x for x in calDeckC]### Turns all A's to value 11 by default
            self.calDeckCSum = sum(calDeckC)
            if self.calDeckCSum > 21:
                calDeckC = [1 if x==11 else x for x in calDeckC] ### if 11 (Ace) in deck and sum is > 21 the A's value will change to 1
                self.calDeckCSum = sum(calDeckC)
                
            if self.calDeckCSum > self.calDeckSum and self.calDeckCSum <= 21:
                print("\t\t\t\t\tDEALER STAYS")
                time.sleep(2)
                return self.calDeckCSum
            
            if self.calDeckCSum >= 18 and self.calDeckCSum <= 21:
                print("\t\t\t\t\tDEALER STAYS")
                time.sleep(2)
                return self.calDeckCSum
            
            if self.calDeckCSum <= 17 and self.calDeckCSum <= self.calDeckSum:
                randomCard5 = random.randint(0,13)
                deckC.append(randomCard5)
                howLong = len(deckC) - 1
                c = deckC[howLong]
                v = self.deckC[c] ### Had to put the randomized # into the dictionary key
                print("\t\t\t\t\tDEALER HITS!")
                time.sleep(3)
                print()
                print("\t\t* * * * *")
                print("\t\t*" "\t*")
                print("\t\t*   {0}"  "\t*".format(v))
                print("\t\t*      " " *")
                print("\t\t* * * * *")
                continue
            
            
            return self.calDeckCSum
            
    def actions(self):
        '''Hit or stay'''
        
        print("Your total: {0}".format(self.calDeckSum))
        #print("Dealer's total: {0}".format(self.calDeckCSum))
        x = input("HIT or STAY? 1 = HIT or 2 = STAY:")
        if x == "1":
            
            print("\t\t\t\t\tHIT!")
            time.sleep(1)
        elif x == "2":
            
            print("\t\t\t\t\tSTAY")
            time.sleep(1)
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
        a = deckC[0] ### a,b,c,d are the 4 randomly generated cards to display
        b = deckC[1] ### deck was generated from Rcard function in class then passed to MAIN to freeze the #'s
        c = deck[0] ### the frozen #'s are then passed back to this function
        d = deck[1]
        w = self.deckC[a] ### Had to put the randomized #'s into the dictionary keys for the following
        x = self.deckC[b]
        y = self.deck[c]
        z = self.deck[d]
        
        calDeck = deck
        calDeck = [10 if x==11 or x ==12 or x==13 else x for x in calDeck] ### This comprehensive list replaces 11,12,13 with 10 in deck so can calculate score
        calDeck = [11 if x==0 else x for x in calDeck]### Turns all A's to value 11 by default
        self.calDeckSum = sum(calDeck)
        
        calDeckC = deckC
        calDeckC = [10 if x==11 or x ==12 or x==13 else x for x in calDeckC] ### this changes all 11, 12, or 13 to value of 10 for Computers hand.
        calDeckC = [11 if x==0 else x for x in calDeckC]### Turns all A's to value 11 by default
        self.calDeckCSum = sum(calDeckC)

        #print(w) ### GET RID OF THIS AFTER TESTING!!!!!!!!!!!!!!

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
        '''Checks if either lost by busting'''
        
        #print(self.calDeckSum)
        #print(self.calDeckCSum) just needed for testing to see totals can get rid of if don't need anymore
        
        if self.calDeckSum > 21:
            #print("Your total: {0}".format(self.calDeckSum))
            #print("Dealer's total: {0}".format(self.calDeckCSum))
            return 2 ### Player lost b/c they busted at the start
        if self.calDeckCSum > 21:
            #print("Your total: {0}".format(self.calDeckSum))
            #print("Dealer's total: {0}".format(self.calDeckCSum))
            return 1 ### Player won b/c computer busted
        else:
            return 4 ### No one has won or busted
        
    def won2(self):
        '''Checks if player won the comp by having higher cards. Couldn't put in WON method because it checked too soon'''
        
        if self.calDeckSum > self.calDeckCSum:
            print("Your total: {0}".format(self.calDeckSum))
            print("Dealer's total: {0}".format(self.calDeckCSum))
            return 1 ### Player won
        if self.calDeckSum == self.calDeckCSum:
            print("Your total: {0}".format(self.calDeckSum))
            print("Dealer's total: {0}".format(self.calDeckCSum))
            return 3 ### PUSH!
        if self.calDeckCSum > self.calDeckSum:
            print("Your total: {0}".format(self.calDeckSum))
            print("Dealer's total: {0}".format(self.calDeckCSum))
            return 2 ### Computer won
        else:
            pass ### No one has won or busted
        
class Players:
    def __init__(self, player, comp):
        self.player = player
        self.comp = comp
    def tallyScore(self):
        pass
        
        
################## VARIABLES & INTRO ##################
print("\t\t\t\t\t\t\t\t Welcome")
time.sleep(2)
print("\t\t\t\t\t\t\t\t   to")
time.sleep(2)
print("\t\t\t\t\t\t\t\tB")
time.sleep(1)
print("\t\t\t\t\t\t\t\t L")
time.sleep(1)
print("\t\t\t\t\t\t\t\t  A")
time.sleep(1)
print("\t\t\t\t\t\t\t\t   C")
time.sleep(1)
print("\t\t\t\t\t\t\t\t    K")
time.sleep(1)
print("\t\t\t\t\t\t\t\tBLACKJACK!!!")
time.sleep(2)

while True: ### This loop starts the program over with a new random hand
    deck = {0:"A",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}
    deckC = {0:"A",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"} ### computer's deck only for adding cards
    randomCard = "0"
    calDeckSum = 0 ### sum of players cards that is calculated in won() method, need to pass this variable to addCard methods
    calDeckCSum = 0 ### sum of computers cards that is calculated in won() method, need to pass this variable to addCard methods
    player = 0 ### This variable will be passed to Players method to keep the score for player
    comp = 0 ### This variable will be passed to Players method to keep the score for computer
    pWon = 0 ### Need to pass this to won method in Cards class so this can tally, then Players-
             ### class will keep the score (I am using 2 classes to practice inheritance
    cWon = 0 ### This is same as pWon but for computer
    
    clear = "\n" * 100 ### clears the screen 
################## MAIN ######################
    
    x = Cards(deck, randomCard, deckC, calDeckSum, calDeckCSum)
    y = Players(player, comp)
    deck = x.Rcard() ### This grabs and freezes the 2 randomly generated player #’s
    deckC = x.Rcard()### This grabs and freezes the 2 randomly generated comp #’s
    winner = x.blackjack()  ### The frozen cards are 1st going to cardStart then to blackjack method. Starts the chain
    
    while True:
      
        if winner == 1:
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
        elif winner == 2:
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
        elif winner == 3:
            again = input("PUSH!!! Play again? 1 YES 2 NO:")
            if again == "1":
                print(clear)
                break
            elif again == "2":
                print("OK then, it was fun playing. Goodbye.")
                sys.exit(0)
            else:
                print("Come-on-now, enter either a 1 or 2!")
                continue
        elif winner == 4: ### No blackjack
                pass
        else:
            print("ERROR MAIN")
            continue
        
        move = x.actions() ### Asking player to hit or stay
        if move == "1":
            
            x.addCard()
            WON = x.won() ### checking if player busted
            #print(calDeckSum)
            #print(WON) just needed for testing, can get rid of if done testing
            if WON == 1:
                while True: ### Need this loop so if player enters anything other than 1 or 2 it loops back here
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
                break ### only comes to this point if player wants to play again. This break starts back at the beg w new cards
            elif WON == 2:
                while True:
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
                break
            elif WON == 3:
                while True:
                    again = input("PUSH!!! Play again? 1 YES 2 NO:")
                    if again == "1":
                        print(clear)
                        break
                    elif again == "2":
                        print("OK then, it was fun playing. Goodbye.")
                        sys.exit(0)
                    else:
                        print("Come-on-now, enter either a 1 or 2!")
                        continue
                break
            elif WON == 4: ### 4 means no one has won
                continue
            continue    
        elif move == "2": ### Even if player stays the computer still needs a card
            #calDeckCSum = x.addCardComp()   ### Freezing computers total SUM
            #print(calDeckCSum)
            x.addCardComp()
            WON = x.won() ### checking if anyone won
            WON2 = x.won2() ### Checks if player won the comp by having higher cards. Couldn't put that in WON method because it checked too soon
            #print(WON) just needed for testing, can get rid of if done testing
            if WON == 1 or WON2 == 1:
                while True:
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
                break
            elif WON == 2 or WON2 == 2:
                while True:
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
                break
            elif WON == 3 or WON2 == 3: ### pushed
                while True:
                    again = input("PUSH!!! Play again? 1 YES 2 NO:")
                    if again == "1":
                        print(clear)
                        break
                    elif again == "2":
                        print("OK then, it was fun playing. Goodbye.")
                        sys.exit(0)
                    else:
                        print("Come-on-now, enter either a 1 or 2!")
                        continue
                break
            elif WON == 4 or WON2 == 4: ### 4 means no one has won
                continue
            continue
            
            
        else:
            print("Come-on-now, enter either a 1 or 2!")
            continue
            
    ####  THOUGHTS after I freeze a card in MAIN, and call the Class which I assigned as x...it uses the frozen value and can then
    ####   be passed to other methods without the self..
    #### BUG if there are 2 aces it will turn both to value 1.
