from sys import stdin
from itertools import permutations
from collections import deque


def bfs():
    q = deque([[*scv, 0]])

    while q:
        cur_state = q.popleft()

        # 정렬된 상태에서 체력이 큰 SCV의 체력이 없다면 종료.
        if cur_state[THREE] == 0:
            return cur_state[CNT]

        # 공격 가능한 경우의 수만큼 큐에 추가.
        for case in attack_case:
            next_scv = [0] * 3

            # visited에 방문 여부를 체크하기 위해 0보다 작은 경우 0으로 변환.
            for i in range(3):
                next_scv[i] = \
                    cur_state[i] - case[i] if cur_state[i] - case[i] > 0 else 0

            # 정렬된 상태로 큐에 추가.
            next_scv.sort()

            if not visited[next_scv[ONE]][next_scv[TWO]][next_scv[THREE]]:
                visited[next_scv[ONE]][next_scv[TWO]][next_scv[THREE]] = True
                q.append([*next_scv, cur_state[CNT] + 1])


if __name__ == '__main__':
    ONE, TWO, THREE, CNT = 0, 1, 2, 3
    n = int(stdin.readline())
    # n이 3보다 작을 경우, 0을 추가해주어 n이 1, 2인 경우 별도로 처리하지 않아도 됨.
    scv = sorted(list(map(int, stdin.readline().split())) + (3 - n) * [0])
    attack_case = list(permutations([9, 3, 1], 3))
    visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
    print(bfs())