import random

Head = 1
Tail = 2
Tosses = 5

def toss():
    for toss in range(Tosses):
        result = random.randint(Head, Tail)
        if result == Head:
            print("Heads")
        else:
            print("Tails")

toss()            