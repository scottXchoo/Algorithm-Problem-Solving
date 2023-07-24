#include <iostream>
using namespace std;

int main() {
    int arr[9][9];
    int max = 0, row = 0, col = 0;
    
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> arr[i][j];
            if (arr[i][j] > max) {
                max = arr[i][j];
                row = i;
                col = j;
            }
        }
    }
    cout << max << "\n";
    cout << row + 1 << " " << col + 1 << endl;
    
    return 0;
}