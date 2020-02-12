#include <deque>
#include <iostream>
#include <vector>
using namespace std;
#define ll long long

vector<int> maxSlidingWindow(vector<int>& arr, int k) {
    if (arr.empty()) {
        return arr;
    }

    if (k == 1 || k == 0) {
        return arr;
    }
    deque<int> Q(k);
    vector<int> answer;
    for (int i = 0; i < k; i++) {
        while ((!Q.empty()) && arr[Q.back()] <= arr[i])
            Q.pop_back();

        Q.push_back(i);
    }

    for (int i = k; i < arr.size(); i++) {
        answer.push_back(arr[Q[0]]);

        while ((!Q.empty()) && Q.front() <= i - k) {
            Q.pop_front();
        }

        while ((!Q.empty()) && arr[Q.back()] <= arr[i])
            Q.pop_back();

        Q.push_back(i);
    }
    answer.push_back(arr[Q[0]]);

    return answer;
}
}

int main() {
    int n = 7;
    int k = 3;
    vector<int> vect1{10, 20, 30};

    vector<int> arr{12, 1, 78, 90, 57, 89, 56};

    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
