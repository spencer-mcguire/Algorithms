#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # find the max diff between smallest and largest prices
    # max profit by subtracting some price by another price that comes BEFORE
    # keet curr_min and max_pro_sofar
    # destructue
    current_min = prices[0]
    current_max_profit = 0
    # loop the arr
    for i in range(len(prices) - 1):
        # set profit to the next index - current minimum
        profit = prices[i + 1] - current_min
        # if profit is greater than the current max OR if the current max is 0 and profit is less than 0 set profit to current max
        if profit > current_max_profit or (current_max_profit == 0 and profit < 0):
            # print(profit)
            current_max_profit = profit
        # if next index is less than current min, set that as current min
        if prices[i + 1] < current_min:
            current_min = prices[i + 1]

    return current_max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

#print(find_max_profit([1050, 270, 1540, 3800, 2]))
