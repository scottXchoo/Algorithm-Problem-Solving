#include <iostream>
#include <vector>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int N, M;
  cin >> N >> M;

  long num;
  vector<long> dp(N + 1);
  dp[0] = 0;
  for (int i = 1; i <= N; i++) {
	cin >> num;
	dp[i] = dp[i - 1] + num;
  }

  int i, j;
  for (int k = 0; k < M; k++) {
	cin >> i >> j;
	cout << dp[j] - dp[i - 1] << '\n';
  }

  return 0;
}