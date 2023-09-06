#include <bits/stdc++.h>
using namespace std;

int n, r, temp, root;
vector<int> adj[54];

int dfs(int here) {
    // 1-1. 변수 초기화
      // ret : 리프노드 수 (= 정답) & child : 자식노드 수
    int ret = 0;
    int child = 0;
    
    for(int there : adj[here]) {
        // 1-2. 지운 노드(r)는 건너뛰기 (= erase)
        if(there == r) continue;
        // 1-3. 누적된 자식노드들의 수
        ret += dfs(there);
        // 1-4. 자식노드의 수
        child++;
    }
    // 1-5. 자식노드의 수 = 0 => 리프노드 라는 뜻
    if(child == 0) return 1;
    return ret;
}

int main() {
    // #0. 입력 부분
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        // 0-1. "-1"을 받으면, root로 처리
        if(temp == -1) root = i;
        // 0-2. Tree 구조 : vector adj에 i를 push_back
        else adj[temp].push_back(i);
    }
    cin >> r;
    
    // #2. 반례 처리 | 지워진 노드가 root 라면, return 0
      // why? 루트노드부터 탐색하지 않는 로직이기 때문
    if(root == r) {
        cout << 0 << "\n"; return 0;
    }
    
    // #1. DFS 로직 | root부터 탐색 시작
    cout << dfs(root) << "\n";
    return 0;
}