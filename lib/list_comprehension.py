#!/usr/bin/env python3

def return_evens(num_list):
    evens = [n for n in num_list if n % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    new_str = [string + '!' for string in sentence_list]
    return new_str