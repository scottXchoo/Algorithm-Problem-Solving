#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N, X;

int main() {
	vector<int> result;
	
	cin >> N;
	
	priority_queue<int> q;
	for (int i = 0; i < N; i++) {
		cin >> X;
		if (X != 0) {
			q.push(X);
		} else {
			if (q.empty()) {
				result.push_back(0);
			} else {
				result.push_back(q.top());
				q.pop();
			}
		}
	}
	
	for (int i = 0; i < result.size(); i++) {
		cout << result[i] << "\n";
	}

	return 0;
}