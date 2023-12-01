# [Gold II] 원판 돌리기 - 17822 

[문제 링크](https://www.acmicpc.net/problem/17822) 

### 성능 요약

메모리: 116084 KB, 시간: 260 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2023년 12월 1일 11:39:55

### 문제 설명

<p>반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 바닥에 놓여있고, 원판의 중심은 모두 같다. 원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다. 각각의 원판에는 M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현한다. 수의 위치는 다음을 만족한다.</p>

<ul>
	<li>(i, 1)은 (i, 2), (i, M)과 인접하다.</li>
	<li>(i, M)은 (i, M-1), (i, 1)과 인접하다.</li>
	<li>(i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)</li>
	<li>(1, j)는 (2, j)와 인접하다.</li>
	<li>(N, j)는 (N-1, j)와 인접하다.</li>
	<li>(i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)</li>
</ul>

<p>아래 그림은 N = 3, M = 4인 경우이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/5968435b-a1af-4e2a-a612-baff989f44b2/-/preview/" style="width: 300px; height: 295px;"></p>

<p>원판의 회전은 독립적으로 이루어진다. 2번 원판을 회전했을 때, 나머지 원판은 회전하지 않는다. 원판을 회전시킬 때는 수의 위치를 기준으로 하며, 회전시킨 후의 수의 위치는 회전시키기 전과 일치해야 한다.</p>

<p>다음 그림은 원판을 회전시킨 예시이다.</p>

<div class="table-responsive">
<table class="table table-bordered" style="width:100%;">
	<tbody>
		<tr>
			<td style="width: 33%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/977a4e67-5aa7-40d4-92ee-5f59ac75aadb/-/preview/" style="width: 300px; height: 295px;"></td>
			<td style="width: 34%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/f2c1e70b-0a84-46c3-b38d-f7395219b00a/-/preview/" style="width: 300px; height: 295px;"></td>
			<td style="width: 33%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/39d57771-6162-49f5-97b7-0d9fd8911222/-/preview/" style="width: 300px; height: 295px;"></td>
		</tr>
		<tr>
			<td style="width: 33%; text-align: center;">1번 원판을 시계 방향으로 1칸 회전</td>
			<td style="width: 34%; text-align: center;">2, 3번 원판을 반시계 방향으로 3칸 회전</td>
			<td style="width: 33%; text-align: center;">1, 3번 원판을 시계 방향으로 2칸 회전</td>
		</tr>
	</tbody>
</table>
</div>

<p>원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 x<sub>i</sub>, d<sub>i</sub>, k<sub>i</sub>이다.</p>

<ol>
	<li>번호가 x<sub>i</sub>의 배수인 원판을 d<sub>i</sub>방향으로 k<sub>i</sub>칸 회전시킨다. d<sub>i</sub>가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.</li>
	<li>원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
	<ol>
		<li>그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.</li>
		<li>없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.</li>
	</ol>
	</li>
</ol>

<p>원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.</p>

### 입력 

 <p>첫째 줄에 N, M, T이 주어진다.</p>

<p>둘째 줄부터 N개의 줄에 원판에 적힌 수가 주어진다. i번째 줄의 j번째 수는 (i, j)에 적힌 수를 의미한다.</p>

<p>다음 T개의 줄에 x<sub>i</sub>, d<sub>i</sub>, k<sub>i</sub>가 주어진다.</p>

### 출력 

 <p>원판을 T번 회전시킨 후 원판에 적힌 수의 합을 출력한다.</p>

