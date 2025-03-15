#include <iostream>

using namespace std;

int t[17];
int p[17];
int d[17];

int main() {
    int N;
    cin >> N;


    for (int i = 1; i <= N; i++) {
        cin >> t[i] >> p[i];
    }

    for (int i = N; i >= 1; i--) {
        if (i + t[i] <= N + 1) {
            d[i] = max(d[i + t[i]] + p[i], d[i + 1]);
        } else {
            d[i] = d[i + 1];
        }
    }

    int ans = 0;
    for (int i = 1; i <= N; i++) {
        if (ans < d[i]) ans = d[i];
    }

    cout << ans;

    return 0;
}