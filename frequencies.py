"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for it in items:
        item = str(it)
        if item in frequencies.keys():
            frequencies[item] = frequencies.get(item) + 1
        else:
            frequencies[item] = 1
    return frequencies
