#include <bits/stdc++.h>
using namespace std;

int n;
vector <double> s;

int main() {
    cin >> n;
    s.resize(n);
    for(int i = 0; i < n; i++) cin >> s[i];
    sort(s.begin(), s.end());
    for(int i = 0; i < 7; i++) printf("%.3f\n", s[i]);
}