#include <iostream>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  int s[N];
  for (int i = 0; i < N; i++) {
	cin >> s[i];
  }

  int answer = 0;
  int sum = 0;
  for (int i = 0; i < N - 2; i++) {
	for (int j = i + 1; j < N - 1; j++) {
	  for (int k = j + 1; k < N; k++) {
		sum = s[i] + s[j] + s[k];
		if (sum <= M) {
		  answer = max(answer, sum);
		}
	  }
	}
  }

  cout << answer;

  return 0;
}