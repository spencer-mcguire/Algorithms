#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # create a batches variable batches = 0
    # loop over recepie
    # while loop over ingredients inside other loop
    #
    #
    batches = 0

    for i in recipe.keys():
        print(i)
        print(f"prints the value:{ingredients[i]}")
    # check if the engredient is not in your list
        if i not in ingredients:
            return 0
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("\n\n{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
