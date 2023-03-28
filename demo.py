### Description ###
# This python script contains a small demonstration game
# The game is one where you learn three patterns and then
# have to guess which pattern is the correct one.
# The game is played in the terminal.
###################
from backend import BackendHandler
import random, time
DEBUG = False
if not DEBUG:
    BACKEND = BackendHandler()

# Patterns
PATTERNS = [
    "circle",
    "line",
    "square"
]

PATTERN_DURATION: float = 0.0
import json
with open("patterns/" + PATTERNS[0] + ".json", "r") as f:
    j = json.load(f)
    for iteration in j["pattern"]:
        PATTERN_DURATION += float(iteration["time"]) / 1000

# Guess
def guess():
    print("Sending the pattern...")
    pattern = PATTERNS[random.randint(0, len(PATTERNS) - 1)]
    random.seed(time.time())
    if not DEBUG:
        BACKEND.send(pattern)
    print("Guess the pattern!")
    for i, pat in enumerate(PATTERNS):
        print("{nr}. {pattern}".format(nr = i + 1, pattern = pat))
    inp = input("Enter the number of the pattern, or nothing to feel it again: ")
    if inp == "":
        print("Sending the pattern again...")
        if not DEBUG:
            BACKEND.send(pattern)
        print("Guess the pattern!")
        for i, pat in enumerate(PATTERNS):
            print("{nr}. {pattern}".format(nr = i + 1, pattern = pat))
        inp = ""
        while inp == "":
            inp = input("Enter the number of the pattern: ")
            if inp == "exit":
                exit()
    elif inp == "exit":
        exit()
    if int(inp) == PATTERNS.index(pattern) + 1:
        print("Correct!")
    else:
        print("Incorrect, you guessed {} but the correct pattern was: {}".format(inp, str(PATTERNS.index(pattern) + 1) + ". " + pattern))
    inp = input("Press enter to continue to play again, or type 'exit' to exit: ")
    if inp == "exit":
        exit()

if __name__ == "__main__":
    # Game
    print("\033c", end="") # Clear the terminal
    print("Welcome to the pattern game!")
    print("You will feel the three patterns in order twice so you can learn them.")
    print("Each pattern will be felt for {time} seconds.".format(time = PATTERN_DURATION))
    print("Then you will have to guess which pattern is the correct one when feeling it.")

    # Learn
    input("Press enter to begin learning the {nr} patterns.".format(nr = len(PATTERNS)))
    print("\033c", end="") # Clear the terminal

    for i, pattern in enumerate(PATTERNS):
        print("Pattern: " + pattern)
        if not DEBUG:
            BACKEND.send(pattern)
            time.sleep(PATTERN_DURATION)
            input("Press enter to feel the pattern again")
            BACKEND.send(pattern)
            time.sleep(PATTERN_DURATION)
            if i != len(PATTERNS) - 1:
                input("Press enter to continue to the next pattern")
            else:
                input("Press enter to begin guessing")
            print("\033c", end="") # Clear the terminal

    # Game
    while True:
        guess()
        print("\033c", end="") # Clear the terminal