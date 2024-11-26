""" Soroush Saririan
    EGN6933 - Exam 3
    
    This is a code that runs the bulls and cows game while calculating the entropy value for the current guess. """

# Importing the necessary libraries
import random 
import math 
import itertools 
from collections import Counter

class Game:
    # Start by developing the functions for the game
    def __init__(self): #starts the game with a new code and a counter for the attempt number
        self.secret_code=self.generate() # Generates the secret code
        self.turn=0 # Counter for the number of attempts
        self.possible_solutions=self.generate_soln() # Generates all the possible solutions
    
    def generate(self): # Function that creates the random 4 digit secret code
        numbers=list("0123456789") # Numbers 0-9
        random.shuffle(numbers) # Shuffles the numbers
        return "".join(numbers[:4]) # Returns the first 4 numbers
    
    def generate_soln(self): # Generating all the possilbe solutions
        numbers="0123456789"
        return ["".join(p) for p in itertools.permutations(numbers,4)]
    
    def calculate_bc(self,guess,solution): # Determines the number of bulls and cows for each attempt
        bulls=sum(1 for x,y in zip(solution,guess)if x==y) # Determines the number of bulls
        cows=sum(1 for y in guess if y in solution)-bulls # Determines the number of cows
        return bulls,cows
    
    def valid_guess(self,guess): # Will determine if the user input follows the rules (4 digit, no repeating)
        return len(guess)==4 and guess.isdigit() and len(set(guess))==4 # Checks if the input is 4 digits and no repeating
    
    # Now implement the entropy portion 
    def entropy(self,guess):
        counter=Counter(self.calculate_bc(guess,solution) for solution in self.possible_solutions) # Counter for the number of bulls and cows
        total=len(self.possible_solutions) # Total number of possible solutions
        entropy=0 
        for count in counter.values(): 
            prob=count/total # Probability of the count
            entropy-=prob*math.log2(prob) # Entropy calculation
        return entropy

    # Create main function to run everything
    def main(self): # Main function to run the game
        print(f"Welcome to bulls and cows!!!")
        print()

        while True: # Loop to run the game
            print()
            # User inputs a guess
            guess=input(f"Enter a 4 digit guess with no repeating numbers or e/E to exit {self.secret_code}: \n")
            if guess.lower()=='e': # Will quit the game and display the code if user inputs e/E
                print(f"Thanks for playing")
                print(f"The code was {self.secret_code}")
                print()
                break
            
            if not self.valid_guess(guess): # Will prompt the user to re-enter code if the input does not follow rules
                print(f"That is not valid, must be 4 non repeating digits")
                continue

            self.turn+=1 # Adds one to the tun counter to see how many attempts it takes to guess
            bulls,cows=self.calculate_bc(guess,self.secret_code) # Calculates number of bull/cows
            print(f"You have {bulls} bulls and {cows} cows")

            entropy=self.entropy(guess) # To display the current entropy
            print(f"current entropy is: {entropy:.6f}") 

            self.possible_solutions=[solution for solution in self.possible_solutions if self.calculate_bc(guess,solution)==(bulls,cows)]
            print(f"there are {len(self.possible_solutions)} solutions left") # Displays the number of possible solutions left
            if bulls==4: # Code if user selects code correctly and win message is displayed
                print(f"you selected the correct code you win!!!")
                print(f"It took you {self.turn} trys to guess")
                break
            
            
# Start the game with this 
if __name__ == "__main__": 
    game=Game() 
    game.main()


