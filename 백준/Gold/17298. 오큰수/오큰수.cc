#include <bits/stdc++.h>
using namespace std;

int n, a[1000004], ret[1000004];
stack<int> s;

int main() {
    // #0. 입력 부분
    cin >> n;
    memset(ret, -1, sizeof(ret));
    for(int i = 0; i < n; i++) {
        // 0-1. 입력과 동시에 바로 배열 안에 넣을 수 있다
        cin >> a[i];
        // #1. 오큰수 로직 | s.top()을 참조하기 전, s.size() 체크 + &&
        while(s.size() && a[s.top()] < a[i]) {
            // 1-1. stack에 쌓인 index에 해당하는 ret의 값을 오큰수로 변경
            // 1-2. 그리고 오큰수로 변경한 stack의 index는 제거
            ret[s.top()] = a[i]; s.pop();
        }
        // #2. 오큰수 안 나오면, stack에 index를 push하기
        s.push(i);
    }
    // #3. 출력 부분
    for(int i = 0; i < n; i++) cout << ret[i] << " ";
}