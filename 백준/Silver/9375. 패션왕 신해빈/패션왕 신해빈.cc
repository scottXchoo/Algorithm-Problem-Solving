#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  unordered_map<string, int> clothes;

  int N, M;
  cin >> N;

  for (int i = 0; i < N; i++) {
	cin >> M;
	for (int j = 0; j < M; j++) {
	  string name, type;
	  cin >> name >> type;

	  if (clothes[type] == 0) {
		clothes[type] = 1;
	  } else {
		clothes[type]++;
	  }
	}

	int sum = 1;
	for (const auto &c : clothes) {
	  sum *= c.second + 1;
	}

	cout << sum - 1 << '\n';
	clothes.clear();
  }

  return 0;
}