#include <bits/stdc++.h>
using namespace std;

int n;
vector<string> v;
string s, ret;

void go() {
    // front를 참조할 때, size() 체크 필수!!
    while(true) {
        if(ret.size() && ret.front() == '0') ret.erase(ret.begin());
        else break;
    }
    // [반례] 0000 같이 입력 받으면, "0"을 보여줘야 됨
    if(ret.size() == 0) ret = "0";
    v.push_back(ret);
    ret = "";
}

bool cmp(string a, string b) {
    if(a.size() == b.size()) return a < b;
    return a.size() < b.size();
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> s;
        ret = "";
        for(int j = 0; j < s.size(); j++) {
            // 아스키코드 65 = A, 이보다 작으면 "숫자"
            if(s[j] < 65) ret += s[j];
            else if(ret.size()) go();
        }
        if(ret.size()) go();
    }
    sort(v.begin(), v.end(), cmp);
    
    for(string i : v) cout << i << '\n';
    return 0;
}