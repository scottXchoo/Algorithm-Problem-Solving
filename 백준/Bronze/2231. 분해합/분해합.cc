#include <iostream>

using namespace std;

int main() {
  int answer = 0;
  int N;
  cin >> N;

  for (int i = 1; i < N; i++) {
	int sum = 0;
	int num = i;

	while (num != 0) {
	  sum += num % 10;
	  num /= 10;
	}

	if (sum + i == N) {
	  answer = i;
	  break;
	}
  }

  cout << answer;

  return 0;
}