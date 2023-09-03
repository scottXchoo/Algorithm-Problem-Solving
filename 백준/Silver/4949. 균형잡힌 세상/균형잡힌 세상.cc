#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while(true) {
        string s;
        getline(cin, s);
        if(s == ".") break;
        
        stack<int> stk;
        bool check = true;
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == ')') {
                if(stk.size() == 0 || stk.top() == '[') {
                    check = false;
                    break;
                } else {
                    stk.pop();
                }
            }
            if(s[i] == ']') {
                if(stk.size() == 0 || stk.top() == '(') {
                    check = false;
                    break;
                } else {
                    stk.pop();
                }
            } 
            if(s[i] == '(' || s[i] == '[') stk.push(s[i]);
        }
        
        if(check && stk.size() == 0) cout << "yes\n";
        else cout << "no\n";
    }
}