#include <iostream>

using namespace std;

int main() {
  int N, T, P, s[6], cnt = 0;

  cin >> N;

  for (int & i : s) {
	cin >> i;
  }

  cin >> T >> P;

  for (int i : s) {
	cnt += (i / T) + (i % T != 0);
  }

  cout << cnt << '\n' << N / P << " " << N % P << '\n';

  return 0;
}