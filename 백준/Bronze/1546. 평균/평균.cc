#include <iostream>

using namespace std;

int main() {
  int N;
  cin >> N;

  double s[N];
  double M = 0;
  for (int i = 0; i < N; i++) {
	cin >> s[i];
	M = max(M, s[i]);
  }

  double answer = 0;
  for (int i = 0; i < N; i++) {
	answer += s[i] / M * 100;
  }

  cout << answer / N;

  return 0;
}