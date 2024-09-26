#include <iostream>
#define MAX 11
using namespace std;

int T;
int dp[MAX];

int main() {
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2;

  int n = 11;
  for (int i = 3; i < n; i++) {
	dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
//	dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 1);
//	dp[i] = min(dp[i], dp[i - 3] + 1);
//	cout << i << " " << dp[i] << endl;
  }

  cin >> T;
  int arr[T];
  for (int i = 0; i < T; i++) {
	int num;
	cin >> num;

//	cout << dp[num];
	arr[i] = num;
  }

  for (int i = 0; i < T; i++) {
	int num = arr[i];
	cout << dp[num] << endl;
  }

  return 0;
}