### Description ###
# This python script contains a small demonstration game
# The game is one where you learn three patterns and then
# have to guess which pattern is the correct one.
# The game is played in the terminal.
###################
from backend import BackendHandler
import random, time
DEBUG = True
if not DEBUG:
    BACKEND = BackendHandler()
RANDOM = random.Random()


# Patterns
patterns = [
    "circle",
    "line",
    "square"
]

PATTERN_DURATION: float = 0.0
import json
with open(patterns[0] + ".json", "r") as f:
    j = json.load(f)
    for iteration in j["pattern"]:
        PATTERN_DURATION += float(iteration["time"]) / 1000

# Game
print("Welcome to the pattern game!")
print("You will feel the three patterns in order twice so you can learn them.")
print("Each pattern will be felt for {time} seconds.".format(time = PATTERN_DURATION))
print("Then you will have to guess which pattern is the correct one when feeling it.")

# Learn
print("Learn the {nr} patterns.".format(nr = len(patterns)))
for pattern in patterns:
    print("Pattern: " + pattern)
    if not DEBUG:
        BACKEND.send(pattern)
        time.sleep(1)
    input("Press enter to continue to the next pattern...")

# Guess
def guess():
    print("Sending the pattern...")
    pattern = RANDOM.choice(patterns)
    if not DEBUG:
        BACKEND.send(pattern)
    print("Guess the pattern!")
    for i, pattern in enumerate(patterns):
        print("{nr}. {pattern}".format(nr = i + 1, pattern = pattern))
    inp = input("Enter the number of the pattern, or nothing to feel it again: ")
    if inp == "":
        print("Sending the pattern again...")
        if not DEBUG:
            BACKEND.send(pattern)
        print("Guess the pattern!")
        for i, pattern in enumerate(patterns):
            print("{nr}. {pattern}".format(nr = i + 1, pattern = pattern))
        inp = input("Enter the number of the pattern: ")
    if int(inp) == patterns.index(pattern) + 1:
        print("Correct!")
    else:
        print("Incorrect, you guessed {} but the correct pattern was: {}".format(inp, str(patterns.index(pattern) + 1) + ". " + pattern))
    inp = input("Press enter to continue to play again, or type 'exit' to exit: ")
    if inp == "exit":
        exit()

while True:
    print("\033c", end="") # Clear the terminal
    guess()
    RANDOM.seed(RANDOM.random())