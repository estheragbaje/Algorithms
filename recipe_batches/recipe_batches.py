#!/usr/bin/python

import math

"""
There are 2 dictionaries, the recipe dictionary and the ingredient dictionary which contain the same keys but different values
The function should check each of the values in the recipe dictionary and each of the values in the ingredient available dictionary
If any of the values in ingredient dictionary is not up to the value in the recipe dictionary, print 0, cannot make recipe

Divide each value in recipe by the corresponding value in ingredient and print out their respective integer result
Get the highest integer. This is the number of things that can be gotten from this recipe using our ingredients
OR

Else, add all the values in recipe dictionary, assign to a value such as recipe total. Add all the values in ingredient dictionary and assign to a value such as ingredient total
Divide recipe total by ingredient total, take the integer or float value of the result. This gives the number of recipes that can be made
"""

def recipe_batches(recipe, ingredients):
  #initialise batches made from recipe to empty array
  recipe_batches = []

  #get the values in recipe and ingredient
  recipe_values = recipe.values()
  ingredient_value = ingredients.values()

  #If any of the values in ingredient dictionary is not up to the value in the recipe dictionary, return 0
  if len(ingredient_value) < len(recipe_values):
    return 0
  else:
  #Divide each value in recipe by the corresponding value in ingredient and print out their respective integer result
    quantity = recipe[recipe_values] // ingredients[ingredient_value]
    recipe_batches.append(quantity)

  return min(recipe_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))