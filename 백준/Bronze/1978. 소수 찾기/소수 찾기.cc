#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int n) {
  if (n < 2) return false;
  for (int i = 2; i <= sqrt(n); i++) {
	if (n % i == 0) return false;
  }
  return true;
}

int main() {
  int N = 0;
  int answer = 0;

  cin >> N;
  int list[N];

  for (int i = 0; i < N; i++) {
	cin >> list[i];

	if (isPrime(list[i])) {
	  answer += 1;
	}
  }

  cout << answer;

  return 0;
}