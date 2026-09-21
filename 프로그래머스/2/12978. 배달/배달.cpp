#include <iostream>
#include <vector>
#define M 500001

using namespace std;

int solution(int N, vector<vector<int>> road, int K) {
    int answer = 0;
    int arr[51][51]{};
    
    // init
    for(int i = 1; i <= N; i++){
        for(int j = 1; j <= N; j++){
            if(i == j) arr[i][j] = 0;
            else arr[i][j] = M;
        }
    }
    
    for(int i = 0; i < road.size(); i++){
        int a = road[i][0];
        int b = road[i][1];
        int c = road[i][2];
        
        arr[a][b] = arr[a][b] < c ? arr[a][b] : c;
        arr[b][a] = arr[a][b];
    }
    
    for(int k = 1; k <= N; k++)
        for(int i = 0; i <= N; i++)
            for(int j = 0; j <= N; j++)
                arr[i][j] = arr[i][j] < arr[i][k] + arr[k][j] ? arr[i][j] : arr[i][k] + arr[k][j];
    
    for(int j = 1; j <= N; j++)
        if(arr[1][j] <= K)
            answer++;
    
    return answer;
}