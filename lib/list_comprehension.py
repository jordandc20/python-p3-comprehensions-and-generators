#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num%2 ==0]
    # if  num_list== '':
    #     return list()
    # else:
    # return x
    
def make_exclamation(sentence_list): 
    return [f'{sentence}!' for sentence in sentence_list]