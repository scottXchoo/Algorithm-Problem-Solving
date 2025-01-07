#include <iostream>

using namespace std;

int a, b, c, d, e, f;

int main() {
    cin >> a >> b >> c >> d >> e >> f;

    for (int i = -999; i <= 999; i++) {
        for (int j = -999; j <= 999; j++) {
            if (a*i + b*j == c) {
                if (d*i + e*j == f) {
                    cout << i << " " << j << "\n";
                    break;
                }
            }
        }
    }
    return 0;
}