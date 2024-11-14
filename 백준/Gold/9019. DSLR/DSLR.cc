#include <iostream>
#include <queue>

using namespace std;

int D(int n) {
  return (n * 2) % 10000;
}

int S(int n) {
  return n == 0 ? 9999 : n - 1;
}

int L(int n) {
  return (n % 1000) * 10 + n / 1000;
}

int R(int n) {
  return (n % 10) * 1000 + n / 10;
}

int main() {
  std::ostream::sync_with_stdio(false);

  int T;
  cin >> T;

  while (T--) {
	int A, B;
	cin >> A >> B;

	queue<pair<int, string>> q;
	vector<bool> visited(10001);
	q.emplace(A, "");
	visited[A] = true;

	while (!q.empty()) {
	  int cur = q.front().first;
	  string curStr = q.front().second;
	  q.pop();

	  if (cur == B) {
		cout << curStr << '\n';
        break;
	  }

	  int next = D(cur);
	  if (!visited[next]) {
		q.emplace(next, curStr + 'D');
		visited[next] = true;
	  }

	  next = S(cur);
	  if (!visited[next]) {
		q.emplace(next, curStr + 'S');
		visited[next] = true;
	  }

	  next = L(cur);
	  if (!visited[next]) {
		q.emplace(next, curStr + 'L');
		visited[next] = true;
	  }

	  next = R(cur);
	  if (!visited[next]) {
		q.emplace(next, curStr + 'R');
		visited[next] = true;
	  }
	}
  }
  return 0;
}