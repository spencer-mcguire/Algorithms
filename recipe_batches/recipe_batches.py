#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    # create a batches variable batches = 0
    # loop over recepie
    # while loop over ingredients inside other loop
    batches = []

    # check if the engredient is not in your list
    if len(recipe) != len(ingredients):
        return 0
    for i in recipe.keys():
        # print(i)
        # print(
        #    f"prints the value: ingredients:{ingredients[i]}, rec: {recipe[i]}")
        # if the keys exists devide the value  of ingredients by key
        temp = ingredients[i] // recipe[i]
        # append it to the batches or it will increment for every key
        batches.append(temp)
        return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 75, 'flour': 51}
    print("\n\n{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
