#include <iostream>
#include <algorithm>

using namespace std;

int compare(const string &a, const string &b) {
  // 길이 같으면, 사전 순서
  if (a.length() == b.length()) {
	return a < b;
	// 길이 다르면, 짧은 것부터
  } else {
	return a.length() < b.length();
  }
}

string word[20000];
int main() {
  int N;
  cin >> N;
  for (int i = 0; i < N; i++) {
	cin >> word[i];
  }

  sort(word, word + N, compare);

  for (int i = 0; i < N; i++) {
	if (word[i] == word[i - 1]) continue;

	cout << word[i] << "\n";
  }

  return 0;
}