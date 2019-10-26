#!/bin/python3
"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    lexicon = {}
    for word in magazine:
        if word in lexicon:
            lexicon[word] += 1
            continue
        else: 
            lexicon[word] = 1
    for word in note:
        if word not in lexicon:
            print('No')
            return
        else:
            lexicon[word] -= 1
            if lexicon[word] == 0:
                del lexicon[word]
            
    
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
