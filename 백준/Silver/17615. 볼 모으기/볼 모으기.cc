#include <iostream>

using namespace std;

int main() {
    int N;
    string s;
    cin >> N >> s;

    char lastBall = s[N - 1];
    int idx1 = N - 1;
    for (int i = N - 1; i > 0; i--) {
        if (s[i] != lastBall) {
            idx1 = i;
            break;
        }
    }

    int rCnt1 = 0;
    int bCnt1 = 0;
    for (int i = idx1; i >= 0; i--) {
        if (s[i] == 'R') rCnt1++;
        else bCnt1++;
    }
    int ans1 = min(rCnt1, bCnt1);

    char firstBall = s[0];
    int idx2 = 0;
    for (int i = 0; i < N; i++) {
        if (s[i] != firstBall) {
            idx2 = i;
            break;
        }
    }

    int rCnt2 = 0;
    int bCnt2 = 0;
    for (int i = idx2; i < N; i++) {
        if (s[i] == 'R') rCnt2++;
        else bCnt2++;
    }
    int ans2 = min(rCnt2, bCnt2);

    cout << min(ans1, ans2);


    return 0;
}