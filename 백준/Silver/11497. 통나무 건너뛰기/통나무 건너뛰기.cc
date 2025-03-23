#include <iostream>
#include <vector>

using namespace std;

int main() {

    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        vector<int> v(N);

        for (int i = 0; i < N; i++) {
            cin >> v[i];
        }

        sort(v.begin(), v.end());

        int answer = v[1] - v[0];
        for (int j = 2; j < N; j += 2) {
            answer = max(answer, v[j] - v[j - 2]);
        }
        for (int j = 3; j < N; j += 2) {
            answer = max(answer, v[j] - v[j - 2]);
        }

        cout << answer << '\n';
    }


    return 0;
}