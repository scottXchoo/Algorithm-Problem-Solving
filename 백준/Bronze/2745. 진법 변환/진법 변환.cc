#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int b, sum = 0;
    cin >> s >> b;
    for(int i = 0; i < s.size(); i++) {
        if(s[i] >= '0' && s[i] <= '9') {
            sum = sum * b + (s[i] - '0');
        } else {
            sum = sum * b + (s[i] - 'A' + 10);
        }
    }
    cout << sum;
    return 0;
}