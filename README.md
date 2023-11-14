# Algorithm_Problem_Solving

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=ckh0601)](https://solved.ac/ckh0601/)

## Greedy | 그리디 알고리즘
- [BOJ 1700 | 멀티탭 스케줄링](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/1700.%E2%80%85%EB%A9%80%ED%8B%B0%ED%83%AD%E2%80%85%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81/%EB%A9%80%ED%8B%B0%ED%83%AD%E2%80%85%EC%8A%A4%EC%BC%80%EC%A4%84%EB%A7%81.py) | Gold 1
  ```python
  # 운영체제에서 페이징 교체 알고리즘 중 Belady's min algorithm (또는 Belady's optimal algorithm)가 있는데, 이 알고리즘을 떠올렸다면 어렵지 않게 풀었을 것 같습니다.
  elif use[i:].index(plug) > far_one:
  	far_one = use[i:].index(plug)
  	temp = plug
  ```
- [BOJ 2109 | 순회강연](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/2109.%E2%80%85%EC%88%9C%ED%9A%8C%EA%B0%95%EC%97%B0/%EC%88%9C%ED%9A%8C%EA%B0%95%EC%97%B0.py) | Gold 3
  ```python
  # 전형적인 그리디 문제
  ## 힙에 p를 넣고 힙의 크기 (= 강연할 횟수)보다 d가 작다면, 가장 작은 p를 pop하기
  heapq.heappush(q, p)
  if len(q) > d: heapq.heappop(q)
  ```

## BFS | 너비 우선 탐색
- [BOJ 17471 | 게리맨더링](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/17471.%E2%80%85%EA%B2%8C%EB%A6%AC%EB%A7%A8%EB%8D%94%EB%A7%81/%EA%B2%8C%EB%A6%AC%EB%A7%A8%EB%8D%94%EB%A7%81.py) | Gold 4
  ```python
  # 조합 : 절반만 만들고 끊기지 않게끔 조건 추가
  combs = list(combinations(range(1, N + 1), i))
  for comb in combs:
  	sum1, node1 = bfs(comb)
  	sum2, node2 = bfs([i for i in range(1, N + 1) if i not in comb])
  if node1 + node2 == N: ans = min(ans, ans(sum1 - sum2))
  ```
- [BOJ 3197 | 백조의 호수](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Platinum/3197.%E2%80%85%EB%B0%B1%EC%A1%B0%EC%9D%98%E2%80%85%ED%98%B8%EC%88%98/%EB%B0%B1%EC%A1%B0%EC%9D%98%E2%80%85%ED%98%B8%EC%88%98.py) | Platinum 5
  ```python
  # 물과 백조를 각각 BFS로 처리
  ## 그리고 deque()을 동시에 처리하고 나중에 업데이트
  if graph[nx][ny] == ".":
    wq1.append((nx, ny))
  else:
    wq2.append((nx, ny))
  ```
- [BOJ 14497 | 주난의 난](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/14497.%E2%80%85%EC%A3%BC%EB%82%9C%EC%9D%98%E2%80%85%EB%82%9C%EF%BC%88%E9%9B%A3%EF%BC%89/%EC%A3%BC%EB%82%9C%EC%9D%98%E2%80%85%EB%82%9C%EF%BC%88%E9%9B%A3%EF%BC%89.py) | Gold 4
  ```python
  # split()하면, index error
  graph.append(list(map(str, input().rstrip())))
  ## appendleft((a, b))를 통해 (a, b)를 바로 탐색할 수 있게 된다.
  ```
- [BOJ 13913 | 숨바꼭질 4](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/13913.%E2%80%85%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%854/%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%854.py) | Gold 4
  ```python
  # 어떻게 이동했는지 추적하는 방법
  if 0 <= nx < 100001 and visited[nx] == 0:
    ## route 라는 배열에 전의 값(x)을 현재 위치(nx)에 할당함
    route[nx] = x // dq.append(nx)
  ## path 라는 함수에서 x로 시작해 route의 값을 역추적하여 arr에 넣는다.
  def path(x): temp = x, arr = []
    for _ in range(visited[x] + 1):
      temp = route[temp]
      arr.append(temp)
    return arr[::-1]
  ```
- [BOJ 12851 | 숨바꼭질 2](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/12851.%E2%80%85%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%852/%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%852.py) | Gold 4
  ```python
  # 방문을 했어도 재방문 할 수 있는 조건 추가
  if (0 <= nx < 100001) and (visited[nx] == 0 or visited[nx] == visited[x] + 1):
      ## vistied 배열에 몇 번 지났는지 누적해서 할당해주기
      visited[nx] = cnt + 1 / dq.append(nx)
  ```
- [BOJ 4179 | 불 !](https://github.com/scottXchoo/Algorithm_Problem_Solving/tree/main/%EB%B0%B1%EC%A4%80/Gold/4179.%E2%80%85%EB%B6%88%EF%BC%81) | Gold 4
  ```python
  # maze(input), human, fire 세 개의 배열 활용
  maze = [] // maze.append(list(input().strip()))
  human, fire = [[0] * C for _ in range(R)]
  ## 불(F)과 사람(H)을 매 분마다 움직이는 것을 구현하기 위해 BFS 함수를 두 개 사용한다.
  def fbfs() & def hbfs()
  ```
- [BOJ 16234 | 인구이동](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/16234.%E2%80%85%EC%9D%B8%EA%B5%AC%E2%80%85%EC%9D%B4%EB%8F%99/%EC%9D%B8%EA%B5%AC%E2%80%85%EC%9D%B4%EB%8F%99.py) | Gold 4
  ```python
  # 두 나라의 인구 차이가 L명 이상, R명 이하면 국경선 오픈 : union(연합국가)
  if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
    union.append((nx, ny))
    dq.append((nx, ny)) // visited[nx][ny] = True
  ```

## DFS | 깊이 우선 탐색
- [BOJ 14889 | 스타트와 링크](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Silver/14889.%E2%80%85%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80%E2%80%85%EB%A7%81%ED%81%AC/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80%E2%80%85%EB%A7%81%ED%81%AC.py) | Silver 1
  ```python
  # 백트래킹 혹은 조합으로 풀 수 있는 문제
  ## 조합 풀이
  members = list(range(N)) # 1부터 N까지의 배열을 이런 식으로 만들 수 있다.
  team2 = list(set(members) - set(team1)) # combinations로 team1을 구한 뒤, team2를 이렇게 구할 수 있다.
  ## 백트래킹 풀이
  if not visited[i]:
    visited[i] = True
    backTracking(depth + 1, i + 1)
    visited[i] = False
  ```
- [BOJ 1189 | 컴백홈](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Silver/1189.%E2%80%85%EC%BB%B4%EB%B0%B1%ED%99%88/%EC%BB%B4%EB%B0%B1%ED%99%88.py) | Silver 1
  ```python
  # 전형적인 DFS와 백트래킹을 곁들인 문제
  ## 주어진 장애물을 활용해서 visited 처리를 할 수 있다.
  graph[nx][ny] = 'T'
  dfs(nx, ny, cnt + 1)
  graph[nx][ny] = '.'
  ```
- [BOJ 14620 | 꽃길](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Silver/14620.%E2%80%85%EA%BD%83%EA%B8%B8/%EA%BD%83%EA%B8%B8.py) | Silver 2
  ```python
  # 풀이가 3개나 있다 : DFS & 백트래킹, 조합(combination) 이용, 재귀함수
  ## 그중 DFS & 백트래킹 풀이를 계속 반복해서 연습하자!
  ```
- [BOJ 15684 | 사다리 조작](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/15684.%E2%80%85%EC%82%AC%EB%8B%A4%EB%A6%AC%E2%80%85%EC%A1%B0%EC%9E%91/%EC%82%AC%EB%8B%A4%EB%A6%AC%E2%80%85%EC%A1%B0%EC%9E%91.py) | Gold 3
  ```python
  for j in range(k, N - 1):
	# 0인 경우 가로줄 만들고 연속된 가로선을 만들지 않기 위해 "j+2" 호츌
	if graph[i][j] == 0:
		graph[i][j] = 1
		dfs(i, j + 2, cnt + 1)
		# 백트래킹 : dfs로 쭉 탐색하다가 끝까지 가면, 해당 사다리 치우기
		graph[i][j] = 0
  ```
- [BOJ 1987 | 알파벳](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/6af170653001965e699ab8be1d77da249c42a3d3/%EB%B0%B1%EC%A4%80/Gold/1987.%E2%80%85%EC%95%8C%ED%8C%8C%EB%B2%B3/%EC%95%8C%ED%8C%8C%EB%B2%B3.py) | Gold 4
  ```python
  # 일반적인 dfs 로직
  def dfs(x, y, cnt): ans = max(ans, cnt)
	for i in range(4): nx, ny = x + dx[i], y + dy[i]
		if 예외 조건들: ## (범위 초과) and (not 알파벳 중복)
		 ## 백트래킹 : 끝까지 갔다가 다시 처음으로 돌아가는 방법
			dfs(nx, ny, cnt + 1)
			alphas.remove(maps[nx][ny])
  # alphas(= visited) 'set' 자료구조 활용
  alphas = set()
  ```
- [BOJ 16637 | 괄호 추가하기](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/e1c04e7b5eb154ebff78467034e7deb7462d3932/%EB%B0%B1%EC%A4%80/Gold/16637.%E2%80%85%EA%B4%84%ED%98%B8%E2%80%85%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0/%EA%B4%84%ED%98%B8%E2%80%85%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0.py) | Gold 3
  ```python
  # calc 함수에서 '+', '-', '*' 처리
  def calc(num1, oper, num2):
  # 모든 경우의 수를 다 구할 필요 X
  ## 반복되는 케이스 3개 구한 뒤, 재귀함수 이용
  ### 1) 계산 끝!
  if idx == n - 1: res = max(res, value)
  ### 2) 괄호 X
  if idx + 2 < n: dfs(idx + 2, calc(value, s[idx + 1], int(s[idx + 2])))
  ### 3) 괄호 O
  if idx + 4 < n: dfs(idx + 4, calc(value, s[idx + 1], calc(int(s[idx + 2]), s[idx + 3], int(s[idx + 4]))))
  ```

## Two Pointer | 투 포인터
- [BOJ 13144 | List of Unique Numbers](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/13144.%E2%80%85List%E2%80%85of%E2%80%85Unique%E2%80%85Numbers/List%E2%80%85of%E2%80%85Unique%E2%80%85Numbers.py) | Gold 4
  ```python
  # 문제 : 수열에서 연속한 1개 이상의 수를 뽑았을 때, 같은 수가 여러 번 등장하지 않는 경우의 수를 구하라.
  ## 문제를 잘못 해석 : `121`이 된다고 생각했고 `12`, `12` 이렇게 같은 수열이 등장하면 안 된다고 생각했다.
  ```
- [BOJ 1644 | 소수의 연속합](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/1644.%E2%80%85%EC%86%8C%EC%88%98%EC%9D%98%E2%80%85%EC%97%B0%EC%86%8D%ED%95%A9/%EC%86%8C%EC%88%98%EC%9D%98%E2%80%85%EC%97%B0%EC%86%8D%ED%95%A9.py) | Gold 3
  ```python
  # 에라토스테네스의 체 : 문제에 소수가 등장하면, 항상 떠올리기!
  temp_sum = sum(arr[start:end])
  if temp_sum == N: # 이렇게 판단할 수 있다.
  ```
## Stack &  Queue | 스택과 큐
- [BOJ 3015 | 오아시스 재결합](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Platinum/3015.%E2%80%85%EC%98%A4%EC%95%84%EC%8B%9C%EC%8A%A4%E2%80%85%EC%9E%AC%EA%B2%B0%ED%95%A9/%EC%98%A4%EC%95%84%EC%8B%9C%EC%8A%A4%E2%80%85%EC%9E%AC%EA%B2%B0%ED%95%A9.py) | Platinum 5
  ```python
  if stack[-1][H] == h: # 스택의 끝 값과 현재 사람이 같을 때, 이 부분 신경써서 복습하기
  ```
- [BOJ 15926 | 현욱이는 괄호왕이야](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/15926.%E2%80%85%ED%98%84%EC%9A%B1%EC%9D%80%E2%80%85%EA%B4%84%ED%98%B8%EC%99%95%EC%9D%B4%EC%95%BC%EF%BC%81%EF%BC%81/%ED%98%84%EC%9A%B1%EC%9D%80%E2%80%85%EA%B4%84%ED%98%B8%EC%99%95%EC%9D%B4%EC%95%BC%EF%BC%81%EF%BC%81.py) | Gold 3
  ```python
  S = input().strip() # 간단히 이렇게 적으면, "(())("를 입력값으로 넣을 수 있다.
  counter[idx] = counter[stack[-1]] = 1 # idx와 스택의 맨 마지막 값에 해당하는 counter를 1로 동시에 바꿔준다.
  ```
- [BOJ 1966 | 프린터 큐](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Silver/1966.%E2%80%85%ED%94%84%EB%A6%B0%ED%84%B0%E2%80%85%ED%81%90/%ED%94%84%EB%A6%B0%ED%84%B0%E2%80%85%ED%81%90.py) | Silver 3
  ```python
  # deque와 index 전용 deque을 만든다.
  dq = deque(list(map(int, input().split())))
  idx_dq = deque(list(range(N))) ## 0부터 N까지 저장
  # 맨 처음꺼를 빼서 맨 뒤로 넣는 방법
  dq.append(dq.popleft())
  idx_dq.append(idx_dq.popleft())
  ```
## Dynamic Programming | 동적 프로그래밍
- [BOJ 12869 | 뮤탈리스크](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/12869.%E2%80%85%EB%AE%A4%ED%83%88%EB%A6%AC%EC%8A%A4%ED%81%AC/%EB%AE%A4%ED%83%88%EB%A6%AC%EC%8A%A4%ED%81%AC.py) | Gold 4
  ```python
  # scv를 3개보다 적게 input으로 받을 때, 처리하는 야무진 방법
  scvs = list(map(int, input().split())) + [0] * (3 - N)
  # 순열(permutation)을 통해 만든 배열 : [(9, 3, 1), (9, 1, 3) ... (1, 3, 9)]
  combs = list(itertools.permutaions([9, 3, 1], 3))
  # if tmp[i] - comp[i]가 0보다 크면, True(1)여서 'tmp[i] - comb[i]'
  # else : False(0)여서 '0'
  next_scv[i] = [0, tmp[i] - comb[i]][tmp[i] - comb[i] > 0] ## 이렇게도 쓰는구나!
  ```

## Bit-Mask | 비트마스크
- [BOJ 14391 | 종이 조각](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/14391.%E2%80%85%EC%A2%85%EC%9D%B4%E2%80%85%EC%A1%B0%EA%B0%81/%EC%A2%85%EC%9D%B4%E2%80%85%EC%A1%B0%EA%B0%81.py) | Gold 3
  
  <img width="500" alt="image" src="https://github.com/scottXchoo/Algorithm_Problem_Solving/assets/107841492/8126233d-c48a-457b-b658-f6becc72c0e2">

  ```python
  # 비트마스크로 푸는 법 생소해서 그런지 바로 이해하기가 어렵다. 주기적으로 풀이법을 반복하자!
  ```

- [BOJ 2234 | 성곽](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/2234.%E2%80%85%EC%84%B1%EA%B3%BD/%EC%84%B1%EA%B3%BD.py) | Gold 3
  ```python
  # "비트마스크와 BFS 조합 + 백트래킹"으로 푸는 문제 : 이 문제 진짜 신박하고 재밌다...
  ## W, H의 위치가 조금 헷갈렸다. y, x로 접근해야 됨
  if maps[x][y] & (1 << i) == 0 # 벽이 없다면 ...
  if maps[i][j] & (1 << k) == (1 << k): # 벽이 있다면 ...
    maps[i][j] -= (1 << k) # 해당 위치에 벽을 제거
    room_del = max(room_del, bfs(i, j)) # 제거한 상태로 bfs 탐색 시작 & 최대 방 크기 업데이트
    maps[i][j] += (1 << k) # 다시 해당 위치에 벽 생성 (백트래킹)
  ```
- [BOJ 1285 | 동전 뒤집기](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/1285.%E2%80%85%EB%8F%99%EC%A0%84%E2%80%85%EB%92%A4%EC%A7%91%EA%B8%B0/%EB%8F%99%EC%A0%84%E2%80%85%EB%92%A4%EC%A7%91%EA%B8%B0.py) | Gold 1
- [BOJ 1062 | 가르침](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/1062.%E2%80%85%EA%B0%80%EB%A5%B4%EC%B9%A8/%EA%B0%80%EB%A5%B4%EC%B9%A8.py) | Gold 4
  ```python
  # 비트마스크 아직 익숙하지가 않다... 무한복습 필요
  words = [input().rstrip() for _ in range(N)]
  def word2bit(word): return bit
  bits = list(map(word2bit, words)
  alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
  ```

## Implementaion | 구현
- [BOJ 17144 | 미세먼지 안녕!](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/17144.%E2%80%85%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80%E2%80%85%EC%95%88%EB%85%95%EF%BC%81/%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80%E2%80%85%EC%95%88%EB%85%95%EF%BC%81.py) | Gold 4
  ```python
  # 1) 미세먼지의 확산, 2) 위에서 반시계방향 순환, 3) 아래에서 시계방향 순환 : 3가지 함수 활용
  up_step = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 동, 북, 서, 남
  down_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 동, 남, 서, 북
  for _ in range(T):
    dust_diffusion() dust_clean_up() dust_clean_down()
  ```
- [BOJ 5430 | AC](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/5430.%E2%80%85AC/AC.py) | Gold 5
  ```python
  # reverse() : 카운트해서 짝수일 때와 홀수 일 때를 나눠서 중복 연산을 피하면 시간초과 X
  arr = input()[1:-1].split(',') # [1, 2, 3, 4] ⇒ 1 2 3 4
  ```
- [BOJ 18111 | 마인크래프트](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Silver/18111.%E2%80%85%EB%A7%88%EC%9D%B8%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8/%EB%A7%88%EC%9D%B8%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8.py) | Silver 2

  <img width="500" alt="image" src="https://github.com/scottXchoo/Algorithm_Problem_Solving/assets/107841492/5aa89d00-a6ed-4cb3-b1a7-a201e28fa72d">
  
  ```python
  ## AS-IS : 기준이 되는 높이를 0부터 256까지 target으로 잡기 (대부분 풀이)
  for target in range(257):
  ## TO-BE : 꼭 0부터 256까지 다 탐색해야할까? 0부터 [maps에 있는 가장 큰 값 + 1]까지만 탐색해도 충분하지 않을까? (나의 풀이) 성공 ✅
  for target in range(max_h):
  ```
	
- [BOJ 14890 | 경사로](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/14890.%E2%80%85%EA%B2%BD%EC%82%AC%EB%A1%9C/%EA%B2%BD%EC%82%AC%EB%A1%9C.py) | Gold 3
  ```python
  # 풀이 여러 번 복습 필요
  # 세로 탐색
  for i in range(N):
    temp = []
    for j in range(N):
      temp.append(maps[j][i])
    if check(temp, L):
      ans += 1
  ```
