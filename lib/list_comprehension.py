#!/usr/bin/env python3

def return_evens(sequence):
    return [x for x in sequence if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = return_evens(numbers)
print(result)




def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]
sentences = ["Hello, how are you", "I love programming", "Have a great day"]
result = make_exclamation(sentences)
print(result)

def return_first(sequence):
    return [x for x in sequence if x + 1 == 6]
numbers =[4,8,16,12,6,5]
result = return_first(numbers)
print(result)