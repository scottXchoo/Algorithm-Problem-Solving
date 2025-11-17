# [Gold II] 통나무 옮기기 - 1938 

[문제 링크](https://www.acmicpc.net/problem/1938) 

### 성능 요약

메모리: 2052 KB, 시간: 0 ms

### 분류

구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색

### 제출 일자

2025년 11월 17일 11:37:32

### 문제 설명

<p>가로와 세로의 길이가 같은 평지에서 벌목을 한다. 그 지형은 0과 1로 나타나 있다. 1은 아직 잘려지지 않은 나무를 나타내고 0은 아무 것도 없음을 나타낸다. 다음 지형을 보자.</p>

<pre><strong>B</strong> 0 0 1 1
<strong>B</strong> 0 0 0 0
<strong>B</strong> 0 0 0 0
1 1 0 0 0
<strong>E</strong> <strong>E</strong> <strong>E</strong> 0 0</pre>

<p>위의 지형에서 길이 3인 통나무 BBB를 밀거나 회전시켜 EEE의 위치로 옮기는 작업을 하는 문제를 생각해 보자. BBB와 EEE의 위치는 임의로 주어진다. 단 문제에서 통나무의 길이는 항상 3이며 B의 개수와 E의 개수는 같다. 통나무를 움직이는 방법은 아래와 같이 상하좌우(Up, Down, Left, Right)와 회전(Turn)이 있다.</p>

<table class="table table-bordered" style="width:50%">
	<thead>
		<tr>
			<th style="text-align: center;">코드</th>
			<th style="text-align: center;">의미</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:center"><code>U</code></td>
			<td>통나무를 위로 한 칸 옮긴다.</td>
		</tr>
		<tr>
			<td style="text-align:center"><code>D</code></td>
			<td>통나무를 아래로 한 칸 옮긴다.</td>
		</tr>
		<tr>
			<td style="text-align:center"><code>L</code></td>
			<td>통나무를 왼쪽으로 한 칸 옮긴다.</td>
		</tr>
		<tr>
			<td style="text-align:center"><code>R</code></td>
			<td>통나무를 오른쪽으로 한 칸 옮긴다.</td>
		</tr>
		<tr>
			<td style="text-align:center"><code>T</code></td>
			<td>중심점을 중심으로 90도 회전시킨다.</td>
		</tr>
	</tbody>
</table>

<p>예를 들면, 다음과 같다. (초기상태로부터의 이동)</p>

<table class="table table-bordered" style="width:100%">
	<thead>
		<tr>
			<th style="text-align: center;">초기상태</th>
			<th style="text-align: center;">상(<code>U</code>)</th>
			<th style="text-align: center;">하(<code>D</code>)</th>
			<th style="text-align: center;">좌(<code>L</code>)</th>
			<th style="text-align: center;">우(<code>R</code>)</th>
			<th style="text-align: center;">회전(<code>T</code>)</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 <strong>B B B</strong> 0 0
0 0 0 0 0 0
0 0 0 1 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 <strong>B B B</strong> 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 1 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 <strong>B B B</strong> 0 0
0 0 0 1 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
<strong>B B B</strong> 0 0 0
0 0 0 0 0 0
0 0 0 1 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 <strong>B B B</strong> 0
0 0 0 0 0 0
0 0 0 1 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 <strong>B</strong> 0 0 0
0 0 <strong>B</strong> 0 0 0
0 0 <strong>B</strong> 0 0 0
0 0 0 1 0 0</pre>
			</td>
		</tr>
	</tbody>
</table>

<p>이와 같은 방식으로 이동시킬 때에 그 움직일 위치에 다른 나무, 즉 1이 없어야만 움직일 수 있다. 그리고 움직임은 위의 그림과 같이 한 번에 한 칸씩만 움직인다. 단 움직이는 통나무는 어떤 경우이든지 중간단계에서 한 행이나 한 열에만 놓일 수 있다. 예를 들면 아래 그림에서 a와 같은 단계는 불가능하다. 그리고 회전의 경우에서는 반드시 중심점을 중심으로 90도 회전을 해야 한다. (항상 통나무의 길이가 3이므로 중심점이 있음)</p>

<p>그리고 이런 회전(Turn)이 가능하기 위해서는 그 통나무를 둘러싸고 있는 3*3 정사각형의 구역에 단 한 그루의 나무도 없어야만 한다. 즉, 아래그림 b, d와 같이 ?로 표시된 지역에 다른 나무, 즉 1이 없어야만 회전시킬 수 있다. 따라서 c와 같은 경우에, 통나무는 왼쪽 아직 벌채되지 않은 나무 때문에 회전시킬 수 없다.</p>

<table class="table table-bordered" style="width:100%">
	<thead>
		<tr>
			<th style="text-align: center;">a</th>
			<th style="text-align: center;">b</th>
			<th style="text-align: center;">c</th>
			<th style="text-align: center;">d</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 B 0 0
0 0 B 0 0 0
0 B 0 0 0 0
0 0 0 1 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 ? ? ? 0
0 0 <strong>B B B </strong>0
0 0 ? ? ? 0
0 0 0 0 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 <strong>B</strong> 0 0
0 0 0 <strong>B</strong> 0 0
0 0 0 <strong>B</strong> 0 0
0 0 0 0 0 0</pre>
			</td>
			<td>
			<pre style="text-align:center">0 0 0 0 0 0
0 0 0 0 0 0
0 0 ? <strong>B</strong> ? 0
0 0 ? <strong>B</strong> ? 0
0 0 ? <strong>B</strong> ? 0
0 0 0 0 0 0</pre>
			</td>
		</tr>
	</tbody>
</table>

<p>문제는 통나무를 5개의 기본동작(<code>U</code>, <code>D</code>, <code>L</code>, <code>R</code>, <code>T</code>)만을 사용하여 처음위치(BBB)에서 최종위치(EEE)로 옮기는 프로그램을 작성하는 것이다. 단, 최소 횟수의 단위 동작을 사용해야 한다.</p>

### 입력 

 <p>첫째 줄에 주어진 평지의 한 변의 길이 N이 주어진다. (4 ≤ N ≤ 50) 주어진다. 이어서 그 지형의 정보가 0, 1, B, E로 이루어진 문자열로 주어진다. 한 줄에 입력되는 문자열의 길이는 N이며 입력 문자 사이에는 빈칸이 없다. 통나무와 최종 위치의 개수는 1개이다.</p>

### 출력 

 <p>첫째 줄에 최소 동작 횟수를 출력한다. 이동이 불가능하면 0만을 출력한다.</p>

