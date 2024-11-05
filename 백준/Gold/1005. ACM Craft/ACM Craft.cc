#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int T;
  cin >> T;

  while (T--) {
	int N, K;
	cin >> N >> K;

	// Delay time for each building
	unordered_map<int, int> delay;
	for (int i = 0; i < N; i++) {
	  int D;
	  cin >> D;
	  delay[i + 1] = D;
	}

	// Building order
	vector<vector<int>> order(N + 1);
	unordered_map<int, int> indegree;
	for (int i = 0; i < K; i++) {
	  int X, Y;
	  cin >> X >> Y;
	  order[X].push_back(Y);
	  indegree[Y]++;
	}

	queue<int> q;
	for (int i = 1; i <= N; i++) {
	  if (indegree[i] == 0) {
		q.push(i);
	  }
	}

	// Time to reach the destination building
	vector<int> time(N + 1, 0);
	while (!q.empty()) {
	  int c_building = q.front();
	  q.pop();

	  time[c_building] = max(time[c_building], delay[c_building]);
	  for (int i = 0; i < order[c_building].size(); i++) {
		int n_building = order[c_building][i];
		time[n_building] = max(time[n_building], time[c_building] + delay[n_building]);
		indegree[n_building]--;
		if (indegree[n_building] == 0) {
		  q.push(n_building);
		}
	  }
	}

	// Destination building
	int W;
	cin >> W;

	// Print the time to reach the destination building
	cout << time[W] << '\n';
  }

  return 0;
}