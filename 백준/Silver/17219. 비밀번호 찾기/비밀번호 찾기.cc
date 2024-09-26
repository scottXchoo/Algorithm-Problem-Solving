#include <iostream>
#include <map>

using namespace std;

int main() {
  cin.tie(nullptr);
  ios::sync_with_stdio(false);

  int N, M;
  cin >> N >> M;

  map<string, string> m;
  string a, b, c;
  for (int i = 0; i < N; i++) {
	cin >> a >> b;
	
	m[a] = b;
  }
  
  for (int i = 0; i < M; i++) {
	cin >> c;
	
	cout << m[c] << '\n';
  }

  return 0;
}