#include <bits/stdc++.h>
using namespace std;

bool compareWith(string a, string b) {
    if(a.length() == b.length())
        return a < b;
    return a.length() < b.length();
}

int main() {
    int N;
    vector<string> vec;
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        string str;
        cin >> str;
        if(find(vec.begin(), vec.end(), str) == vec.end()) {
            vec.push_back(str);
        }
    }
    sort(vec.begin(), vec.end(), compareWith);
    
    for(int i = 0; i < vec.size(); i++) {
        cout << vec[i] << '\n';
    }
}