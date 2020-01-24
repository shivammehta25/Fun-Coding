// Trying to code in Cpp to check time comparison
#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t) {
        --t;
        int a[3], n;
        cin >> a[0] >> a[1] >> a[2] >> n;
        sort(a, a + 3);
        int s = 2 * a[2] - (a[0] + a[1]);
        if (n - s >= 0 && (n - s) % 3 == 0) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}