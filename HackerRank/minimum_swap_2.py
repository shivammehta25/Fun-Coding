#!/usr/bin/env python3
"""
This is from the URL  :https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen
In this we need to find the minimum amount of swaps required for an array to be sorted
"""

def minimum_swap(arr):
    """
    Takes an array and finds the minimum swaps needed
    
    The input is first reduced into the subtracted index equivalent format then if the index is equal to the value things remains unchanged
    otherwise the value is swapped with the index of that value.
    
    arr: array to find the solution to
    
    Returns: 
    swap : integer , minimum number of swaps
    """
    arr = [i-1 for i in arr]
    swap = 0
    for i in range(len(arr)):
        if i == arr[i]:
            continue
        index = arr.index(i)
        arr[i], arr[index] = arr[index], arr[i]
        swap += 1
    return swap


def main():
    """
    The main driver function to run the code
    """
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(minimum_swap(arr))
    

def test():
    """
    The Test function to test the code and assert values
    """

    arr_1 = [4, 3, 1, 2]
    assert minimum_swap(arr_1) == 3

    arr_2 = [2, 3, 4, 1, 5]
    assert minimum_swap(arr_2) == 3

    print("Tests Successful")


if __name__ == '__main__':
    test()  
