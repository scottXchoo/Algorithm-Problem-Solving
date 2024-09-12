#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
  int r = 31;
  int M = 1234567891;

  int N;
  string L;
  cin >> N;
  cin >> L;

  int hashValue = 0;
  for (int i = 0; i < N; i++) {
	int charToInt = L[i] - 96;
	hashValue += charToInt * int(pow(r, i));
  }

  int answer = hashValue % M;
  cout << answer;

  return 0;
}