#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  # #base case
  # if n == 0:
  #   return 1
  # #define all possible rps inputs
  # input = [rock, paper, scissors]

  #define the possible rps inputs
  rps_input = ['rock', 'paper', 'scissors']

  #possible output combinations
  result = []
  turns = n

  def combination_outcome(turnsLeft, game):
    # base case
    if turnsLeft == 0:
      result.append(game)
      return

    for i in rps_input:
        # recursive case
        combination_outcome(turnsLeft - 1, game + [i])

  combination_outcome(turns, [])
  return result




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')