from random import randint as rand
import time

AVERAGE_TIME = []
GUESS_AVERAGE = []

class timerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

def main():
    guesses = 1

    tic = time.time()

    while rand(0, 10000) != 1:
        guesses+=1

    toc = time.time()

    finishedTime = toc - tic
    
    if guesses is 0:
        raise timerError("Guesses must be above 1")

    print(f"Finished in: {finishedTime:0.4f} and {guesses} guesses")
    
    AVERAGE_TIME.append(finishedTime)

    GUESS_AVERAGE.append(guesses)  

def calc_avg():
    for item in AVERAGE_TIME:
        avg_time = sum(AVERAGE_TIME) / len(AVERAGE_TIME)

    print(f"Your average time was: {avg_time:0.2f} seconds")

    for x in GUESS_AVERAGE:
        avg_guess = sum(GUESS_AVERAGE) / len(GUESS_AVERAGE)

    print(f"Your average guess was: {avg_guess:0.2f} guesses")

    print(f"This program ran {counter} time(s)")

if __name__ == '__main__':
    counter = 0
    for i in range(0,10):
        counter+=1
        main()
    
    calc_avg()

    
