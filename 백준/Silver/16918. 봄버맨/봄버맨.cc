#include<iostream>

using namespace std;

int R, C, N;
char arr[205][205]{};
int timer[205][205]{};
int dx[4] = { 1,0,-1,0 };
int dy[4] = { 0,1,0,-1 };

void initMap() {
	cin >> R >> C >> N;

	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			cin >> arr[i][j];
}

void incTimer() {
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (arr[i][j] == 'O')
				timer[i][j]++;
}

void plantBomb() {
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (arr[i][j] == '.')
				arr[i][j] = 'O';
}

void explodeBomb() {
	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++)
			if (timer[i][j] == 3) {
				timer[i][j] = 0;  // timer 초기화
				arr[i][j] = '.';  // 폭발시키기
				for (int k = 0; k < 4; k++) {  // timer가 3이 아닌 인접 폭탄 제거
					int nx = i + dx[k];
					int ny = j + dy[k];
					if (arr[nx][ny] == 'O' && timer[nx][ny] < 3) {
						timer[nx][ny] = 0;
						arr[nx][ny] = '.';
					}
				}
			}
}

void printMap() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++)
			cout << arr[i][j];
		cout << '\n';
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	initMap();

	for (int i = 1; i < N + 1; i++) {
		incTimer();  // arr을 검사해서, O이면, timer++;
		if (i == 1) continue;

		if (!(i % 2))  // i가 짝수면 '.'인 곳에 폭탄 설치
			plantBomb();
		else  // i가 홀수면 timer 검사해서 폭발시키고, 폭발된 곳 timer reset
			explodeBomb();
	}
	printMap();
	
	return 0;
}