#include <iostream>
#define ll long long
using namespace std;

void printDuplicates(int a[], int n) {
    int f = 0;
    for (int i = 0; i < n; i++) {
        int k = a[i] % n;
        a[k] = a[k] + n;
        if ((a[k] / n) == 2) {
            f = 1;
            cout << a[i] % n << " ";
        }
    }
    if (f == 0)
        cout << -1;
}

int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i; i < n; ++i) {
        cin >> a[i];
    }
    printDuplicates(a, n);
    return 0;
}