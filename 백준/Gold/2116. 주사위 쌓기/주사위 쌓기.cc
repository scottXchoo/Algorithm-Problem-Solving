#include <iostream>

#define MAX 10000
#define DICE_SIZE 6

using namespace std;

int N;
int arr[MAX][DICE_SIZE]{};
int opposite[DICE_SIZE] = {5, 3, 4, 1, 2, 0};

int findDownIdx(int j, int x) {
    // 아랫면 인덱스 찾기
    for (int i = 0; i < DICE_SIZE; i++) {
        if (arr[j][i] == x) return i;
    }
    return 0;
}

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < DICE_SIZE; j++) {
            cin >> arr[i][j];
        }
    }

    int answer = 0;
    for (int i = 0; i < DICE_SIZE; i++) {
        // 0번 주사위의 up, down 결정
        int upIdx = i;
        int upNum = arr[0][upIdx];
        int downIdx = opposite[upIdx];

        int sumMax = 0;
        int diceMax = 0;
        // 0번 주사위의 옆면 최댓값 구하기
        for (int k = 0; k < DICE_SIZE; k++) {
            if (k == downIdx || k == upIdx) continue;
            diceMax = max(diceMax, arr[0][k]);
        }
        sumMax += diceMax;

        // 1~5번 주사위
        for (int j = 1; j < N; j++) {
            int downNum = upNum;
            downIdx = findDownIdx(j, downNum);
            int upIdx = opposite[downIdx];
            upNum = arr[j][upIdx];

            int diceMax2 = 0;
            for (int k = 0; k < DICE_SIZE; k++) {
                if (k == downIdx || k == upIdx) continue;
                diceMax2 = max(diceMax2, arr[j][k]);
            }
            sumMax += diceMax2;
        }
        answer = max(answer, sumMax);
    }

    cout << answer;

    return 0;
}
