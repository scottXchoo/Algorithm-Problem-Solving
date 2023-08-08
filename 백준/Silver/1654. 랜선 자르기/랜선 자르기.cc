#include <iostream>
#include <algorithm>

using namespace std;

unsigned int ans;
unsigned int N,K;
unsigned int list[10000];

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);

	cin >> K >> N;
    
	unsigned int maxi = 0;
    
	for (int i = 0; i < K; i++)
	{
		cin >> list[i];
		maxi = max(maxi, list[i]);
	}

	unsigned int left = 1, right = maxi, mid;
	
	while (left <= right)
	{
		// mid 연산
		mid = (left + right) / 2;
        
		// 몫의 합을 저장하는 변수
		unsigned int now = 0; 
        
		for (int i = 0; i < K; i++)
		{
			//mid로 나눈 몫을 저장
			now += list[i] / mid;
		}

		if (now >= N)
		{
			// 현재 mid로 나눈 값이 N보다 크거나 같다면,
			// left를 움직여 길이가 더 긴 경우는 가능한지 검사
			left = mid + 1;
            
			// N개를 만들 수 있을 때, 답을 더 큰 값으로 계속 갱신
			ans = max(ans, mid);
		}
		else
		{
			// 현재 mid로 나눈 값이 N보다 작다면,
			// right 움직여 길이가 더 짧은 경우는 가능한지 검사
			right = mid - 1;
		}
	}
	
	cout << ans << '\n';
}
