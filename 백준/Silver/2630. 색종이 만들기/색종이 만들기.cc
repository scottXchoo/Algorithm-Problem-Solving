#include <iostream>

using namespace std;

int white = 0;
int blue = 0;
int arr[129][129];

void fn(int x, int y, int size) {
    int cut = 0;
    int first_color = arr[x][y];
    for (int i = x; i < x + size; i++) {
        for (int j = y; j < y + size; j++) {
            if (arr[i][j] != first_color) {
                cut = 1;
                break;
            }
        }
    }

    if (cut) {
        fn(x, y, size/2);
        fn(x+size/2, y, size/2);
        fn(x, y+size/2, size/2);
        fn(x+size/2, y+size/2, size/2);
    } else {
        if (first_color == 0) {
            white++;
        } else {
            blue++;
        }
    }
}

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    fn(0, 0, N);
    cout << white << '\n';
    cout << blue << '\n';

    return 0;
}