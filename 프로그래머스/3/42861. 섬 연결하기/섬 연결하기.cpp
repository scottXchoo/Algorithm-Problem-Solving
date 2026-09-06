#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int parents[101];

int compare(vector<int> a, vector<int> b) {
    return a[2] < b[2];
}

int getParent(int child) {
    if (child == parents[child]) return child;
    else return parents[child] = getParent(parents[child]);
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    sort(costs.begin(), costs.end(), compare);
    
    for (int i = 0; i < n; i++) {
        parents[i] = i;
    }
    
    for (int i = 0; i < costs.size(); i++) {
        int start = getParent(costs[i][0]);
        int end = getParent(costs[i][1]);
        int cost = costs[i][2];
        
        // start = end: 이미 최소 비용인 경로 있다는 뜻
        if (start != end) {
            parents[end] = start;
            answer += cost;
        }
    }
    
    return answer;
}