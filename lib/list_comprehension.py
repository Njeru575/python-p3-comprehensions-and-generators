#!/usr/bin/env python3

def return_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

print(return_evens([0, 1, 3, 5, 7, 8, 9]))  

pass

def make_exclamation(sentences):
    return [sentence + "!" for sentence in sentences]

# Example usage
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

pass