# Algorithm_Problem_Solving

코딩테스트 준비를 위해서 매일 1-2문제씩 풀면서 기억할만한 문제들을 대표적인 알고리즘을 기준으로 정리할 에정입니다. (Inspired by [subinium](https://github.com/subinium))

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=ckh0601)](https://solved.ac/ckh0601/)

## BFS | 너비 우선 탐색
- [BOJ 4179 | 불 !](https://github.com/scottXchoo/Algorithm_Problem_Solving/tree/main/%EB%B0%B1%EC%A4%80/Gold/4179.%E2%80%85%EB%B6%88%EF%BC%81)
  ```python
  # maze(input), human, fire 세 개의 배열 활용
  maze = [] // maze.append(list(input().strip()))
  human, fire = [[0] * C for _ in range(R)]
  ## 불(F)과 사람(H)을 매 분마다 움직이는 것을 구현하기 위해 BFS 함수를 두 개 사용한다.
  def fbfs() & def hbfs()
  ```
- [BOJ 16234 | 인구이동](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/16234.%E2%80%85%EC%9D%B8%EA%B5%AC%E2%80%85%EC%9D%B4%EB%8F%99/%EC%9D%B8%EA%B5%AC%E2%80%85%EC%9D%B4%EB%8F%99.py)
  ```python
  # 두 나라의 인구 차이가 L명 이상, R명 이하면 국경선 오픈 : union(연합국가)
  if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
    union.append((nx, ny))
    dq.append((nx, ny)) // visited[nx][ny] = True
  ```
- [BOJ 12851 | 숨바꼭질 2](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/12851.%E2%80%85%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%852/%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%852.py)
  ```python
  # 방문을 했어도 재방문 할 수 있는 조건 추가
  if (0 <= nx < 100001) and (visited[nx] == 0 or visited[nx] == visited[x] + 1):
      ## vistied 배열에 몇 번 지났는지 누적해서 할당해주기
      visited[nx] = cnt + 1 / dq.append(nx)
  ```
- [BOJ 13913 | 숨바꼭질 4](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/13913.%E2%80%85%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%854/%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88%E2%80%854.py)
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

## DFS | 깊이 우선 탐색
- [BOJ 16637 | 괄호 추가하기](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/e1c04e7b5eb154ebff78467034e7deb7462d3932/%EB%B0%B1%EC%A4%80/Gold/16637.%E2%80%85%EA%B4%84%ED%98%B8%E2%80%85%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0/%EA%B4%84%ED%98%B8%E2%80%85%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0.py)
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

## Dynamic Programming | 동적 프로그래밍
- [BOJ 12869 | 뮤탈리스크](https://github.com/scottXchoo/Algorithm_Problem_Solving/blob/main/%EB%B0%B1%EC%A4%80/Gold/12869.%E2%80%85%EB%AE%A4%ED%83%88%EB%A6%AC%EC%8A%A4%ED%81%AC/%EB%AE%A4%ED%83%88%EB%A6%AC%EC%8A%A4%ED%81%AC.py)
  ```python
  # scv를 3개보다 적게 input으로 받을 때, 처리하는 야무진 방법
  scvs = list(map(int, input().split())) + [0] * (3 - N)
  # 순열(permutation)을 통해 만든 배열 : [(9, 3, 1), (9, 1, 3) ... (1, 3, 9)]
  combs = list(itertools.permutaions([9, 3, 1], 3))
  # if tmp[i] - comp[i]가 0보다 크면, True(1)여서 'tmp[i] - comb[i]'
  # else : False(0)여서 '0'
  next_scv[i] = [0, tmp[i] - comb[i]][tmp[i] - comb[i] > 0] ## 이렇게도 쓰는구나!
  ```
