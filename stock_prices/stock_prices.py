#!/usr/bin/python

"""
Name of function is find_max_profit
What it takes as input is a list/array
keep track of the highest value after a lower value (max_profit_so_far) and the lowest value (current_min_price_so_far)that comes before it
Subtract the lowest value before from the highest value in the array


"""
import argparse

def find_max_profit(prices):
  
  for price in prices:
    
    max_profit_so_far = 0 
    for i in range(len(prices) - 1):
      for j in range(i+1, len(prices)):
        if prices[j] - prices[i] > max_profit_so_far:
          max_profit_so_far = prices[j] - prices[i]

    return max_profit_so_far

  # max_profit_so_far = 0

  # #setting current min price as the first index in the array 
  # current_min_price_so_far = prices[0]

  # #loop through all the prices in prices array
  # for price in prices:
  #   #check which one is smaller using min
  #   current_min_price_so_far = min(current_min_price_so_far, price)

  #   #compare profit
  #   compare_profit = price - current_min_price_so_far

  #   #get the highest profit to be the max profit
  #   max_profit_so_far = max(compare_profit, max_profit_so_far)

  #   return max_profit_so_far



    
        

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))