#include <iostream>

using namespace std;

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int N, M;
    int arr[1030][1030]{};
    int DP[1030][1030]{};

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 1; i <= N; i++) {
        int sum = 0;
        for (int j = 1; j <= N; j++) {
            sum += arr[i][j];
            DP[i][j] = sum;
        }
    }

    for (int i = 1; i <= M; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int ans = 0;
        for (int j = 0; j < x2 - x1 + 1; j++) {
            ans += DP[x1 + j][y2] - DP[x1 + j][y1 - 1];
        }
        cout << ans << '\n';
    }

    return 0;
}