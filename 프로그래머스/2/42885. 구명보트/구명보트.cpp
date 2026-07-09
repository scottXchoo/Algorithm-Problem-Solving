#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0, cnt = 0, size = people.size();
    int st = 0, end = size - 1;
    
    sort(people.begin(), people.end());
    
    while(st <= end){
        if(people[st] + people[end] <= limit){  // 둘이 탈 수 있을 때
            st++;
            end--;
        }
        else  // 최댓값 혼자 탈 때
            end--;
        answer++;  // 보트 하나 탑승
    }
    
    return answer;
}