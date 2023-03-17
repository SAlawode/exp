# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 23:04:01 2022

@author: samuel
"""

def make_word_dict():
    """Reads a word list and returns a dictionary."""
    d = dict()
    fin = open('word.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d
 
memo = {}
memo[""] = [""]


def is_reducible(word, word_dict):
    """
    Takes a word and returns a list of its reducible children

    Parameters
    ----------
    word : TYPE
        DESCRIPTION.

    Returns
    -------
    A list of reducible children

    """
    if word in memo:
        return memo[word]
    
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)
            
            
    memo[word] =  res
    return res
    

def children(word, word_dict):
    """
    Takes a word and find all the words that can be formed by removing a letter from it

    Parameters
    ----------
    word : string
        The word to find its children.

    Returns
    -------
    List of children.

    """
    res = []
    for letter in word:
        child = word.replace(letter, "")
        if child in word_dict:
            res.append(child)
        
    return res

def all_reducible(word_dict):
    """
    Checks all the words in a word dict and returns a list of reducible in the dictionary

    Returns
    -------
    list of words that are reducible in the dict.

    """
    
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:    
            res.append(word)
    return res

   

def print_trail(word):
    """
    Prints the sequence of words that reduce a string to an empty string
    If there are more than one choice, it chooses the first.

    Parameters
    ----------
    word : string
        The word to be reduced.

    Returns
    -------
    None.

    """
    if len(word) == 0:
        return
    
    print(word, end=" ")
    t = is_reducible(word, word_dict)
    print_trail(t[0])
    
    
def print_longest_words(word_dict):
    """
    Finds the longest reducible words and prints them

    Parameters
    ----------
    word_dict : dictionary of valid words
        DESCRIPTION.

    Returns
    -------
    None.

    """
    words = all_reducible(word_dict)
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
        
    for _,word in t[0:8]:
        print_trail(word)
        print("\n")
        
        
    



if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)
    
    