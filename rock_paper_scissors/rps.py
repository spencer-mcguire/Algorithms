#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # output needs to be a list of lists
    # if no players the game doesnt start, if 1 player only 3 possibilities, if 2 player 9 possible and so on
    # create a base list with rock paper scisors
    rps = [['rock'], ['paper'], ['scissors']]
    # create a list with all possible scissor plays
    # __base case__
    # if n = 0 return [[]]
    if n == 0:
        return [[]]

    if n == 1:
        return rps
    # if n = 1 return base options (rps)
    # create helper function to cause recursion and trigger possible outcomes
    #
    else:
        base = rock_paper_scissors(n-1)
        print(f"base = {base}")
        all_possible = []
        for i in range(3):
            for j in range(len(base)):
                all_possible = [base[j][:]]
        for i in range(all_possible):
            if i < len(all_possible)/3:
                all_possible[i].insert(0, 'rock')
            elif i < len(all_possible)*2/3:
                all_possible[i].insert(0, 'paper')
            else:
                all_possible[i].insert(0, 'scissors')
        return all_possible


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

print(rock_paper_scissors(2))
