#include <iostream>
#define ll long long
using namespace std;
int main() {
    ll h, n;
    cin >> h >> n;
    for (int i = 0; i < n; i++) {
        ll a;
        cin >> a;
        h -= a;
    }
    if (h <= 0) {
        cout << "Yes";
    } else {
        cout << "No";
    }
    return 0;
}