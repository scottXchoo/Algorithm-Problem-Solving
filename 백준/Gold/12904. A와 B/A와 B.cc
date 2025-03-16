#include <iostream>

using namespace std;

int main() {
    string s, t;
    cin >> s >> t;

    while (t.length() > s.length()) {
        char last = t[t.length() - 1];
        t.erase(t.length() - 1, 1);

        if (last == 'B') reverse(t.begin(), t.end());

        if (t == s) {
            cout << 1;
            return 0;
        }
    }

    cout << 0;
    return 0;
}