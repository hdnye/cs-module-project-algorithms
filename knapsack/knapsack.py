#!/usr/bin/python
import random
import time
from itertools import combinations
import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    # Your code here

    pass

# First pass solutions
def naive_fill_knapsack(sack, items):
   # Put highest value itemsin sack until full
   # TODO sort items by value
  items.sort(key= lambda x: x.value, reverse=True)
  
    # TODO put most valuable iteems in sack until full
  size = 0
  for item in items:
      size += item.size
      if size > 50:
        return sack
      else: 
        sack.append(item)
  return sack

def brute_force_knapsack(sack, items):
    # Try every combination to find the best
    # TODO - generate all possible combinations of items
  combos = [] # <-- O(n!) not a good search method for large lists

    # TODO - calculate the value of all combinations
  for i in range(1, len(items) + 1):
      list_of_combos = list(combinations(items, i))
      for combo in list_of_combos: 
        combos.append(list(combo))

    # TODO - find the combination with the highest value
    # -- add up all the weight & value of the items, save the best 1
    # set variable to a null or undefined value to find best
  best_value = -1
  for combo in combos:
    value = 0
    size = 0
    for item in combo:
      value += item.value
      size += item.size  
    if size <=50 and value > best_value:
      best_value = value
      # this will be the combo so far that is best we've seen
      # set sack to this combo
      sack = combo
    return sack

  
def greedy_knapsack(sack, items):
  '''Use ratio of [value] / [weight]
     to choose items for sack
  '''
    # TODO - caluclate efficiencies
  for item in items:    
    item.efficiency = item.value / item.size
    # TODO - sort items by efficiency
    items.sort(key= lambda x: x.efficiency, reverse=True)
    # TODO - put items in sack until full
    size = 0
  for item in items:
    size += item.size
    if size > 50:
      return sack
    else:
      sack.append(item)
  return sack



if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')

# class Item:

#     def __init__(self, name, size, value):
#         self.name = name
#         self.size = size
#         self.value = value
#         self.efficiency = 0

#     def __str__(self):
#         return f'{self.name}, {self.size} lbs, ${self.value}'

#     def __repr__(self):
#         return self.__str__()


small_cave = []
medium_cave = []
large_cave = []


def fill_cave_with_items():
    '''Randomly generates Item objects and 
    creates caves of different sizes for testing
    '''
    names = ["painting", "jewel", "coin", "statue", "treasure chest",
             "gold", "silver", "sword", "goblet", "hat"]
    for _ in range(5):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))
    for _ in range(15):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        medium_cave.append(Item(n, w, v))
    for _ in range(25):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        large_cave.append(Item(n, w, v))


def print_results(items, knapsack):
    '''Print out contents of what the algorithm  
    calculated should be added to the knapsack
    '''
    # print(f'\nItems in the cave:')
    # for i in items:
    #     print(i)
    print('\nBest items to put in knapsack: ')
    for item in knapsack:
        print(f'-{item}')
    print(f'\nResult calculated in {time.time()-start:.5f} seconds\n')
    print('\n-------------------------')

fill_cave_with_items()
knapsack = []

# test 1
print('\nStarting test 1, naive approach...')
items = large_cave
start = time.time()
knapsack = naive_fill_knapsack(knapsack, items)
print_results(items, knapsack)

# test 2
# print('\nStarting test 2, brute force...')
# items = medium_cave
# start = time.time()
# knapsack = brute_force_knapsack(knapsack, items)
# print_results(items, knapsack)

# test 3
# print('\nStarting test 2, brute force...')
# items = large_cave
# start = time.time()
# knapsack = brute_force_knapsack(knapsack, items)
# print_results(items, knapsack)

# test 4
print('\nStarting test 4, greedy...')
items = large_cave
start = time.time()
knapsack = greedy_knapsack(knapsack, items)
print_results(items, knapsack)
