#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    required_ents = recipe.keys()
    lowest_batches_possible = None

    for ingredient in required_ents:
        batches_possible = ingredients.get(
            ingredient, 0) // recipe.get(ingredient)
        if lowest_batches_possible is None or batches_possible < lowest_batches_possible:
            lowest_batches_possible = batches_possible

    return lowest_batches_possible


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
