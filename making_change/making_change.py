#!/usr/bin/python
'''
 figure out exactly how many ways there are to make change for the amount of money they plopped down in front of you using only pennies, nickels, dimes, quarters, and half-dollars. 
--Since this is a bank, you have an infinite supply of coinange. Write a function `making_change` that receives as input an amount of money in cents as well as an array of coin denominations and calculates the total number of ways in which change can be made for the input amount using the given coin denominations. 

For example, `making_change(10)` should return 4, since there are 4 ways to make change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:
'''
import sys

def making_change(amount, denominations):
    


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")