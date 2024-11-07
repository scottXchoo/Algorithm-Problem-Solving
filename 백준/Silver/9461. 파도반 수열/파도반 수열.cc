#include <iostream>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int T;
  cin >> T;

  while (T--) {
	int N;
	cin >> N;

	long long dp[101] = {0, 1, 1, 1, 2, 2};
	for (int i = 6; i <= N; i++) {
	  dp[i] = dp[i - 1] + dp[i - 5];
	}

	cout << dp[N] << '\n';
  }

  return 0;
}