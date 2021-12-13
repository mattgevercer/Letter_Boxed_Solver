#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:15:55 2021

@author: mattgevercer
"""
import string
from string import punctuation
from itertools import permutations
from itertools import product
y = input('Please input the Letter Boxed letters as a single string with no space or punctuation between letters. Write the letters starting with the top side of the square, continuing clockwise: ')
x = [i for i in y]

#load word list
with open('corncob_lowercase.txt', "r") as word_list:
    words = word_list.read().split('\n')

#get rid of words with punctuation and numbers, and those less than 3 letters
for i in reversed(range(len(words))):
   if any(p in words[i] for p in punctuation):
       words.pop(i)
   elif any(n in words[i] for n in string.digits):
       words.pop(i)
   elif len(words[i]) < 3:
       words.pop(i)

def subset(words):
    """
    Parameters
    ----------
    words : a list of english words

    Returns
    -------
    A subsetted list of words that are legal for Letter Boxed.
    """                      
    #get rid of words that don't conatin letters in box 
    for i in reversed(range(len(words))):
        letters = [j for j in words[i]]
        if set(letters).issubset(set(x)) == False:
            words.pop(i)
    #get rid of LB-illegal words
        else:
            broke = 0
            for n in range(3,13,3): #iterate through sides of square
                if broke ==1:
                    break
                else:
                    for m in range(len(letters)-1): #iterate through pairs of letters
                        check = (letters[m],letters[m+1])
                        if check in product(x[n-3:n],repeat = 2):#cartesian product of 2 letters in a side
                            words.pop(i)
                            broke = 1
                            break                

subset(words)

def initial_state(words):
    """
    Parameters
    ----------
    words : List of English words
    Returns : Word with highest Number of unique letters
    -------
    """
    unique = []
    for i in words:
        letters = [j for j in i]
        unique.append(len(set(letters)))
    max_i = unique.index(max(unique))
    return words[max_i]

def word_chain(tup):
    """
    Parameters
    ----------
    tup : a tuple with strings as entries

    Returns: True if last letter of word n is same as first letter of word n+1, False otherwise
    -------
    """
    check = []
    for i in range(len(tup)-1):
        check.append(tup[i][-1] == tup[i+1][0])
    return all(check)

best_word = initial_state(words)
best_word_letters = [i for i in best_word]
if set(best_word_letters) == set(x):
    print('the best single word is: '+ best_word)
else:
    #sort word in descending order according to length of element
    words.sort(key=len,reverse=True)
    solutions =[]
    r = 2 #first check all the 2 r permutations
    perms = permutations(words,r)
    ans = [i for i in perms] #list of permutations
    count = 0
    while len(solutions) < 1: #stops when we have three potential solutions  
        q = ''.join([str(x) for x in ans[count]]) #concatenated permutation
        letters = [i for i in q]
        if set(letters) == set(x) and word_chain(ans[count]):
            solutions.append(ans[count])
        if count == len(ans)-1:
            r += 1
            perms = permutations(words,r)
            ans = [i for i in perms]
            count = 0
        else:
            count += 1
    print('Try these as solutions: ')
    print(solutions)



    