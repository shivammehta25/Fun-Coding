#include <iostream>
#include <numeric>
#define ll long long
using namespace std;

int main() {
    ll n, k;
    cin >> n >> k;
    int arr[n];
    for (int i; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n, greater<int>());

    ll count = 0;
    if (k >= n) {
        cout << 0;
        return 0;
    }
    cout << accumulate(arr + k, arr + n, count);
    return 0;
}
