#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_price = None
    max_profit = None

    for buy_price_i in range(0, len(prices) - 1):
        if min_price is None or prices[buy_price_i] < min_price:
            min_price = prices[buy_price_i]

            for sell_price in prices[buy_price_i + 1:]:
                if max_profit is None or (sell_price - min_price) > max_profit:
                    max_profit = sell_price - min_price

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
