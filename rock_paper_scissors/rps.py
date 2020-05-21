#!/usr/bin/python
#how many outcomes?
#where to store outcome?
#iterate over outcomes to get comobos
#Ds to use? easiest to add/remove options?
#rounds limit?
'''
Write a function `rock_paper_scissors` to generate all of the possible plays that can be made in a game of "Rock Paper Scissors", given some input `n`, which represents the number of plays per round. 
'''
import sys

def rock_paper_scissors(n):
  outcomes = ['rock', 'scissors', 'paper',]
  arr = []

  stack =[]
  stack.append([])


  while len (stack) > 0:
    turn = stack.pop()

    if n == 0 or len(turn) ==n:
      arr.append(turn)
    else:
      for option in outcomes:
        stack.append(turn + [option])

  return arr



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')