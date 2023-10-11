#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	listMax = [max(liste) for liste in numbers]
	return listMax

def join_integers(numbers):
	return int("".join([str(elem) for elem in numbers]))

def generate_prime_numbers(limit):
    premiers = []
    nombres = [ number  for number  in range(2,limit +1) ]
    while len(nombres) != 0:
        premiers.append(nombres[0])
        nombres = [i for i in nombres if (i % nombres[0]) != 0]
    return premiers



def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
    liste = []
    if excluded_multiples == None:
            excluded_multiples = 1
    for num in range(1, num_combinations + 1, excluded_multiples):
        for letter in strings:
            liste.append(letter + str(num))
    return liste

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
