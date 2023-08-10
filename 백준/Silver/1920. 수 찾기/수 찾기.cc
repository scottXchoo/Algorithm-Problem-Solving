#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;

int num[100001];

void binarySearch(int n, int arr[]) {
    int low = 0;
    int high = N - 1;
    int mid;
    
    while(low <= high) {
        mid = (low + high) / 2;
        
        if(num[mid] == n) {
            cout << "1" << '\n';
            return;
        } else if(num[mid] < n) {
            low = mid + 1;
        } else if(num[mid] > n) {
            high = mid - 1;
        }
    }
    cout << "0" << '\n';
    return;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        num[i] = a;
    }
    
    sort(num, num + N);
    
    cin >> M;
    for(int i = 0; i < M; i++) {
        int b;
        cin >> b;
        binarySearch(b, num);
    }
}
