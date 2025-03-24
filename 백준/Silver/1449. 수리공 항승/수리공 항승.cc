#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N, L;
    cin >> N >> L;

    int pipe[1001];
    for (int i = 0; i < N; i++) {
        cin >> pipe[i];
    }

    int ans = 1;
    sort(pipe, pipe + N);
    int start = pipe[0];
    for (int i = 1; i < N; i++) {
        if (start + L > pipe[i]) continue;
        start = pipe[i];
        ans++;
    }

    cout << ans;

    return 0;
}