#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    
    // people 내림차순
    int people_len = people.size();
    sort(people.begin(), people.end(), greater<>());
    for (int i = 0; i < people_len - 1; i++) {
        int cur_num = people[i];
        for (int j = i + 1; j < people_len; j++) {
            int next_num = people[j];
            if (next_num == 0) continue;
            if (cur_num + next_num <= limit) {
                people[i] = cur_num + next_num;
                people[j] = 0;
            }
        }
    }
    
    for (int i = 0; i < people_len; i++) {
        if (people[i] != 0) answer++;
    }
    
    return answer;
}