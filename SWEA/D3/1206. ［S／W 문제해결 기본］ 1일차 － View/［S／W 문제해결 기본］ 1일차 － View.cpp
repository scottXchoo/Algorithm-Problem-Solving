#include <iostream>
#include <algorithm>
using namespace std;
 
int main() {
 
    int test_case;
    int T;
 
    T = 10;
 
    for (test_case = 1; test_case <= T; test_case++) {
 
        //사용할 변수 초기화
        int N;
        int building[1000];
        int res = 0;
 
        //입력
        cin >> N;
        for (int i = 0; i < N; i++) {
            cin >> building[i];
        }
 
        //각 빌딩마다 탐색
        for (int i = 2; i < N - 2; i++) {
 
            //빌딩에 영향을 주는 4개 빌딩 중 가장 높은 높이
            int maxHeight = max(max(building[i - 2], building[i - 1]), max(building[i + 1], building[i + 2]));
 
            //빌딩이 가장 높은 높이보다 높다면, 결과 저장
            if (maxHeight < building[i]) {
                res += building[i] - maxHeight;
            }
        }
 
        //출력
        cout << "#" << test_case << " " << res << "\n";
    }
}
