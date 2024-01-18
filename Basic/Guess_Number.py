import random
EASY_LEVEL_TURNS=15
MEDIUM_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check(guess,num,turns):
    if(guess>num):
        print("Too high!")
        return turns-1
    elif(guess<num):
        print("Too low!")
        return turns-1
    else:
        print(f"You got it.The answer is {num}.")

def difficulty():
    level=input("Choose dfficulty:'easy' or 'medium' or 'hard'.")
    if(level=='easy'):
        return EASY_LEVEL_TURNS
    elif(level=='medium'):
        return MEDIUM_LEVEL_TURNS
    elif level=='hard':
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to number guessing game!")
    num=random.randint(1,100)
    turns=difficulty()
    guess=0
    while guess!=num:
        print(f"You have {turns} attempts remaining to guess the no.")
        guess=int(input("Make a guess:"))
        turns=check(guess,num,turns)
        if turns==0:
            print("You Lose!")
            return 
game()