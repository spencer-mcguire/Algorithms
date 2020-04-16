#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # output needs to be a list of lists
    # if no players the game doesnt start, if 1 player only 3 possibilities, if 2 player 9 possible and so on
    # create a base list with rock paper scisors
    rps = [['rock'], ['paper'], ['scissors']]
    # create a list with all possible scissor plays
    all_possible = []
    # __base case__
    # if n = 0 return [[]]
    if n == 0:
        return [[]]

    # if n = 1 return base options (rps)
    # create helper function to cause recursion and trigger possible outcomes
    # helper needs to loop over the rps list
    # add those to a temp list
    #
    def helper(play, round_num):

        # loop the rps list
        for i in range(len(rps)):
            # print(play)
            # append index of loop in rps to play and delete all in rps
            play.append(rps[i])
            print(play)
        # if round_nim = n append play to all possible
        if round_num == n:
            all_possible.append(play[:])
            # else call helper again with current roudn and total round + 1
        else:
            helper(play, round_num+1)
        # pop the current round list
        play.pop()
        # call helper with empty total round and 1 as current round
    helper([], 1)
    return all_possible


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

print(rock_paper_scissors(1))
