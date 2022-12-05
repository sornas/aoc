import sys

OTHER = {"A": "rock", "B": "paper", "C": "scissors"}
ME = {"X": "rock", "Y": "paper", "Z": "scissors"}
ME_2 = {"X": "lose", "Y": "draw", "Z": "win"}

WINS_OVER = {"paper": "rock", "rock": "scissors", "scissors": "paper"}
LOSES_TO = {v: k for k, v in WINS_OVER.items()}
WINS_OVER, LOSES_TO = LOSES_TO, WINS_OVER

def main():
    score = 0
    for r in sys.stdin.readlines():
        other, me = r.strip().split(" ")
        todo = ME_2[me]
        other = OTHER[other]
        if todo == "lose":
            me = LOSES_TO[other]
        elif todo == "win":
            me = WINS_OVER[other]
        else:
            me = other

        if me == "rock":
            score += 1
        elif me == "paper":
            score += 2
        else:
            score += 3
        if (me == "rock" and other == "scissors") or (me == "paper" and other == "rock") or (me == "scissors" and other == "paper"):
            # i win
            score += 6
        elif me == other:
            # draw
            score += 3
        else:
            # i lose
            score += 0
    print(score)


main()
