#include <bits/stdc++.h>
using namespace std;

int n;
string s;

bool check(string s) {
    // stack을 매번 초기화가 필요하기 때문에 안에다 정의!
    stack<char> stk;
    for(char c : s) {
        if(c == '(') stk.push(c);
        else {
            // ')'는 Push를 아예 안 하네?
            if(!stk.empty()) stk.pop();
            else return false;
        }
    }
    // stack이 다 비워짐? True else False
    return stk.empty();
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> s;
        if(check(s)) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
    return 0;
}