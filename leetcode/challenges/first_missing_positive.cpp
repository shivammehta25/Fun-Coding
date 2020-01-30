#include <iostream>
#include <vector>
using namespace std;
#define ll long long

/*
Given an unsorted integer array, find the smallest missing positive integer.
Input: [1,2,0]
Output: 3

Input: [3,4,-1,1]
Output: 2

Input: [7,8,9,11,12]
Output: 1


1: One Approach can be to sort it and then Iterate and find the first non positive number,
But that will be O(NlogN) Solution

2: Trying this to solve in O(N) with constant time complexity
Using: 
*/

class Solution {
   public:
    static void swap(int* x, int* y) {
        int temp;
        temp = *x;
        *x = *y;
        *y = temp;
    }
    static int firstMissingPositive(vector<int>& v) {
        for (auto& i : v) {
            cout << i << " ";
        }

        int x = 5, y = 6;
        cout << x << " " << y << "\n";

        swap(&x, &y);
        cout << x << " " << y;
        return 0;
    }
};

int main() {
    Solution s;
    vector<int> vect{-1, -2, 2, 1, 10};
    s.firstMissingPositive(vect);
    return 0;
}