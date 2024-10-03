#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int N;
  cin >> N;

  int P, times[N];
  for (int i = 0; i < N; i++) {
	cin >> P;
	times[i] = P;
  }

  sort(times, times + N);

  int ans = 0;
  for (int i = 0; i < N; i++) {
	ans += (N - i) * times[i];
  }

  cout << ans;

  return 0;
}