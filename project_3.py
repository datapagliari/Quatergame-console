"""
This is a game called "Quater-cards", based on the multiplicative properties of quaternion numbers.

Developer: Pat Pagliari
patopagliari@gmail.com
"""

# Modules:
import random
from typing import Type 

#As each card will have a quaternion number, lets create a class to rule them
class q_card:
    def __init__(self, nro, i, j, k): # The four parameters of a quaternion
        self.nro = nro
        self.i = bool(i)
        self.j = bool(j)
        self.k = bool(k)

    def __str__(self): # To print them
        if self.i:
            if self.j:
                if self.k:
                    return "♦ " + str(self.nro*-1) 
                else:
                    return "♦ " + str(self.nro) + "*i*j"
            else:
                if self.k:
                    return "♦ " + str(self.nro) + "*i*k"
                else:
                    return "♦ " + str(self.nro) + "*i"
        else:
            if self.j:
                if self.k:
                    return "♦ " + str(self.nro) + "*j*k"
                else:
                    return "♦ " + str(self.nro) + "*j"
            else:
                if self.k:
                    return "♦ " + str(self.nro) + "*k"
                else:
                    return "♦ " + str(self.nro)

    def is_real(self): # To know if a number is real (without imaginaries parts)
        if (self.i == True and self.j == True and self.k == True) or (self.i == False and self.j == False and self.k == False):
            return True
        else:
            return False

    #The getters
    def getI(self):
        return self.i
    def getJ(self):
        return self.j
    def getK(self):
        return self.k
    def getN(self):
        return int(self.nro)

    # Defining multiplication among quaternions
    def __mul__(self, other):
        if self.i == True and self.j == True and self.k == True:
            self.nro = self.nro * (-1)
            self.i, self.j, self.k = False, False, False
        _newnro = self.nro * other.getN()
        if self.i == other.getI():
            if self.i == True:
                _newnro = _newnro * (-1)
            newi = False
        else:
            newi = True
        if self.j == other.getJ():
            if self.j == True:
                _newnro = _newnro * (-1)
            newj = False
        else:
            newj = True
        if self.k == other.getK():
            if self.k == True:
                _newnro = _newnro * (-1)
            newk = False
        else:
            newk = True
        if newi == True and newj == True and newk == True:
            _newnro = _newnro * (-1)
            newi, newj, newk = False, False, False
        return q_card(_newnro, newi, newj, newk)

def get_deck(): # Returns a shuffled deck (as a list) of 36 q-cards
    mazo = []
    for number in range(1,5):
        mazo.append(q_card(number, False, False, False))
        mazo.append(q_card(number, True, False, False))
        mazo.append(q_card(number, False, True, False))
        mazo.append(q_card(number, True, True, False))
        mazo.append(q_card(number, False, False, True))
        mazo.append(q_card(number, True, False, True))
        mazo.append(q_card(number, False, True, True))
        mazo.append(q_card(number, True, True, True))
    random.shuffle(mazo)
    return mazo

def helpo(): # Print the rules when invoked
    print("----------------------------")
    print("Quater-cards rules:")
    print("A quaternion is an hiper-complex number, of the form A + B*i + C*j + D*k")
    print("Where: i*i = j*j = k*k = -1")
    print("And also: i*j*k = -1")
    print("")
    print("In this game, each card has a quaternion number")
    print("Each player will have three cards in their hands")
    print("There's only one scoreboard in the game: ")
    print("Player 1 win if the final score is a positive number. If it is negative, Player 2 win")
    print("In every turn, a quaternion-number will be the jackpot accumulated")
    print("Each player choose some of their cards, and multiply those numbers with the accumulated")
    print("If the product is a real number (with no values of i, j, or k), the player can score the jackpot")
    print("")
    print("When typing commands, just enter one letter, as asked")
    print("----------------------------")
    t = ""
    while t != "--resume":
        t = input("Type '--resume': ")
  
# This class will represent a 'hand' of three cards for each player  
class hando:
    def __init__(self): # takes no arguments, return a list
        self.hh = [None, None, None]

    def repartir(self, deck_h): # given a deck, takes a card for each empty slot in the hand
        for element in range(3):
            if self.hh[element] == None:
                try:
                    self.hh[element] = deck_h.pop()
                except IndexError:
                    self.hh[element] = None
        return self.hh

    def chose_card(self, X): # to choose and play a card in the hand
        if X == "A":
            rta = self.hh[0]
            self.hh[0] = None
        elif X == "B":
            rta = self.hh[1]
            self.hh[1] = None
        elif X == "C":
            rta = self.hh[2]
            self.hh[2] = None
        return rta #extracted card

    def isempty(self): # return True if hand is empty
        for element in self.hh:
            if element != None:
                return False
        return True

    def print_hand(self): # To print the current hand
        lett = ["A) ", "B) ", "C) "]
        for e in range(len(self.hh)):
            print(lett[e] + str(self.hh[e]))

# A class to represent each player:
class player:
    def __init__(self, name) -> None: # init with name, assing
        self.name = name
        self.hand = hando() # creates class-hand instance
        self.end = False 

    def get_card(self, deck): # calls function for getting a hand
        return self.hand.repartir(deck)

    def getHand(self): # return player's hand
        return self.hand

    def getName(self):
        return self.name

    def end_game(self): # player concludes his game
        self.end = True
        return self.end

    def check_end(self): # checks if player concluded
        return self.end


# Game Structure
def Quatergame():
    deck = get_deck() # create game deck
    print("Welcome to 'Quater-cards'\nPlease, enter your names\n----------------------------")
    
    # Asking and displaying names
    name1 = input("Player 1, please type your name: ").capitalize()
    name2 = input("Player 2, please type your name: ").capitalize()
    player1 = player(name1)
    player2 = player(name2)
    print(name1 + "'s goal is to finish with a POSITIVE score:")
    print(name2 + "'s goal is to finish with a NEGATIVE score:")
    
    # Help instruction
    print("At anytime you can type '--help' to read the rules and instructions")

    # Starter    
    starter = input("Type any letter to start:\n").capitalize()
    if starter == "--help":
        helpo()
    print("----------------------------")
    print("The deck has been shuffled")
    print("----------------------------")
    print(name1 + "'s cards:")
    player1.get_card(deck)
    player1.getHand().print_hand()
    print("----------------------------")
    print(name2 + "'s cards:")
    player2.get_card(deck)
    player2.getHand().print_hand()
    print("----------------------------")

    # Firs turn:
    turn_p1 = True # To define who's turn is
    arena = None # Value of the accumulated
    points = 0 # Score of the game
    counter = 0 # This will garantize alternance between players

    while player1.check_end() == False or player2.check_end() == False: # Checks if both players ended
        if arena == None and len(deck) != 0: # If arena empty, then add a card
            arena = deck.pop()
            print("A new card has been added to the accumulated\n")
        print("Quaternion accumulated:", arena, "\n")
        
        # Player 1 turn
        if turn_p1 and (player1.check_end() == False):
            print("It's " + name1 + "'s turn (+)")
            choice = ""
            CC = -1
            player1.getHand().repartir(deck) 
            while CC == -1: #Convert chosen letter in number
                print("This are your cards:" )
                player1.getHand().print_hand() # Print hand
                while choice != "A" and choice != "B" and choice != "C":  # Checks input is valid
                    print("Choose your card:")
                    choice = input("A/B/C: ").capitalize()
                    if choice == "--help":
                        helpo()
                carta = player1.getHand().chose_card(choice) # Chosen card
                print(carta)
                print("")
                if carta != None:
                    try:
                        arena = arena * carta # Multiplies card times accumulated
                    except TypeError:
                        print("error acá")
                    print("Quaternion accumulated:", str(arena), "\n")
                    if arena.is_real() == True: # If true, player can collect points
                        print("That's a real number! You can claim " + str(arena.getN()) + " points")
                        new_comm = input("Type 'Y' to claim them: " ).capitalize()
                        if new_comm == "Y":
                            print(arena.getN(), "points added")
                            points += arena.getN()
                            turn_p1 = False
                            print("Score: " + str(points))
                            print(len(deck), "cards remain in the deck")
                            print("----------------------------")
                            arena = None
                        elif new_comm == "--help":
                            helpo()                            
                if player1.getHand().isempty() == False and arena != None: # Checks if could be another playable card in the turn
                    new_comm = input("Type 'E' to end turn, or any other letter to continue: " ).capitalize()
                    if new_comm == "E":
                        CC = 0
                    elif new_comm == "--help":
                        helpo()
                    choice = ""
                else:
                    CC = 0
                    choice = ""
            if len(deck) == 0: # Checks if deck is empty, if True, then player can end his/her game
                newmove = input("Type X to conclude your entire game, or any other letter to continue: ").capitalize()
                if newmove == "X":
                    player1.end_game()
                elif newmove == "--help":
                    helpo()
            if arena != None: # Checks if arena is empty, if true, conclude the turn
                turn_p1 = False
                print("Score: " + str(points))
                print(len(deck), "cards remain in the deck")
                print("----------------------------\n")
        
        # Player 2 turn
        elif (turn_p1 == False) and (player2.check_end() == False):
            print("It's " + name2 + "'s turn (-)")
            choice = ""
            CC = -1
            player2.getHand().repartir(deck)
            while CC == -1: #Convert chosen letter in number
                print("This are your cards:" )
                player2.getHand().print_hand()
                while choice != "A" and choice != "B" and choice != "C": # Checks input is valid
                    print("Choose your card:")
                    choice = input("A/B/C: ").capitalize()
                    if choice == "--help":
                        helpo()
                carta = player2.getHand().chose_card(choice) # Chosen card
                print(carta)
                print("")
                if carta != None:
                    arena = arena * carta # Multiplies card times accumulated
                    print("Quaternion accumulated:", str(arena), "\n")
                    if arena.is_real() == True: # If true, player can collect points
                        print("That's a real number! You can claim " + str(arena.getN()) + " points")
                        new_comm = input("Type 'Y' to claim them: " ).capitalize()
                        if new_comm == "Y":
                            print(arena.getN(), "points added")
                            points += arena.getN()
                            turn_p1 = True
                            print("Score: " + str(points))
                            print(len(deck), "cards remain in the deck")
                            print("----------------------------\n")
                            arena = None
                        elif new_comm == "--help":
                            helpo()
                if player2.getHand().isempty() == False and arena != None: # Checks if could be another playable card in the turn
                    new_comm = input("Type 'E' to end turn, or any other letter to continue: " ).capitalize()
                    if new_comm == "E":
                        CC = 0
                    elif new_comm == "--help":
                        helpo()
                    choice = ""
                else:
                    CC = 0
                    choice = ""
            if len(deck) == 0:  # Checks if deck is empty, if True, then player can end his/her game
                newmove = input("Type X to conclude your entire game, or any other letter to continue: ").capitalize()
                if newmove == "X":
                    player2.end_game()
                elif newmove == "--help":
                    helpo()
            if arena != None: # Checks if arena is empty, if true, conclude the turn
                turn_p1 = True
                print("Score: " + str(points))
                print(len(deck), "cards remain in the deck")
                print("----------------------------")

        elif player1.check_end() == True or player2.check_end() == True: # Checks any players have conclude
            counter += 1 
            if counter % 2 == 0:
                turn_p1 = True
            else:
                turn_p1 = False

    print("FINAL SCORE:", points, "\n") # Print final score
    if points < 0: # if negative, player 2 wins
        print(name2, "wins!\n\n")
    elif points > 0: # if negative, player 1 wins
        print(name1, "wins!\n\n")
    else:
        print("TIE\n\n")
    contini = input("Type 'Q' to play another round of 'Quater-cards': ").capitalize() # Ask for continuation
    if contini == "Q":
        print("----------------------------")
        Quatergame()
    elif contini == "--help":
        helpo()

# Start game
Quatergame()



