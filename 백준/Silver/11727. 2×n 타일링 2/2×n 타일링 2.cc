#include <iostream>

using namespace std;

int main() {
  std::ostream::sync_with_stdio(false);

  int n;
  cin >> n;

  int dp[1001] = {0, 1, 3};

  for (int i = 3; i <= n; i++) {
	dp[i] = (dp[i - 2] * 2 + dp[i - 1]) % 10007;
  }

  cout << dp[n] % 10007;

  return 0;
}