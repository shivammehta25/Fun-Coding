#include <iostream>
#define ll long long
using namespace std;

int main() {
    ll h, a;
    cin >> h >> a;
    ll count = 0;
    while (h > 0) {
        h -= a;
        count++;
    }
    cout << count;
    return 0;
}