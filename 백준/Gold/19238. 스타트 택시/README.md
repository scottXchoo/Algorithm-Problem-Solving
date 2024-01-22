# [Gold II] 스타트 택시 - 19238 

[문제 링크](https://www.acmicpc.net/problem/19238) 

### 성능 요약

메모리: 114980 KB, 시간: 204 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색, 구현, 시뮬레이션

### 제출 일자

2024년 1월 22일 21:19:32

### 문제 설명

<p>스타트링크가 "스타트 택시"라는 이름의 택시 사업을 시작했다. 스타트 택시는 특이하게도 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.</p>

<p>택시 기사 최백준은 오늘 M명의 승객을 태우는 것이 목표이다. 백준이 활동할 영역은 N×N 크기의 격자로 나타낼 수 있고, 각 칸은 비어 있거나 벽이 놓여 있다. 택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다. 알고리즘 경력이 많은 백준은 특정 위치로 이동할 때 항상 최단경로로만 이동한다.</p>

<p>M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다. 여러 승객이 같이 탑승하는 경우는 없다. 따라서 백준은 한 승객을 태워 목적지로 이동시키는 일을 M번 반복해야 한다. 각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다.</p>

<p>백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 연료는 한 칸 이동할 때마다 1만큼 소모된다. 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다. 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/b4dfd78f-5276-44a4-a1f1-a5ccde6fbc8b/-/preview/" style="width: 395px; height: 396px;"></p>

<p style="text-align: center;"><그림 1></p>

<p><그림 1>은 택시가 활동할 영역의 지도를 나타내며, 택시와 세 명의 승객의 출발지와 목적지가 표시되어 있다. 택시의 현재 연료 양은 15이다. 현재 택시에서 각 손님까지의 최단거리는 각각 9, 6, 7이므로, 택시는 2번 승객의 출발지로 이동한다.</p>

<table class="table table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 50%; text-align: center;">
			<p><img alt="" src="https://upload.acmicpc.net/3a0360d0-7aa4-4f6e-89aa-8f29ceb3db8d/-/preview/" style="width: 358px; height: 355px;"></p>

			<p><그림 2></p>
			</td>
			<td style="width: 50%; text-align: center;">
			<p><img alt="" src="https://upload.acmicpc.net/fb1d41e5-a420-4957-8fe8-1a6f822b284e/-/preview/" style="width: 355px; height: 354px;"></p>

			<p><그림 3></p>
			</td>
		</tr>
	</tbody>
</table>

<p><그림 2>는 택시가 2번 승객의 출발지로 가는 경로를, <그림 3>은 2번 승객의 출발지에서 목적지로 가는 경로를 나타낸다. 목적지로 이동할 때까지 소비한 연료는 6이고, 이동하고 나서 12가 충전되므로 남은 연료의 양은 15이다. 이제 택시에서 각 손님까지의 최단거리는 둘 다 7이므로, 택시는 둘 중 행 번호가 더 작은 1번 승객의 출발지로 이동한다.</p>

<table class="table table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 50%; text-align: center;">
			<p><img alt="" src="https://upload.acmicpc.net/a4ad059c-f909-4cf2-a401-9d72a69a2549/-/preview/" style="width: 355px; height: 356px;"></p>

			<p><그림 4></p>
			</td>
			<td style="width: 50%; text-align: center;">
			<p><img alt="" src="https://upload.acmicpc.net/3abc49bb-33a3-4828-a6c3-1be22fd3967d/-/preview/" style="width: 357px; height: 356px;"></p>

			<p><그림 5></p>
			</td>
		</tr>
	</tbody>
</table>

<p><그림 4>와 <그림 5>는 택시가 1번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 남은 연료의 양은 15 - 7 - 7 + 7×2 = 15이다.</p>

<table class="table table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 50%; text-align: center;">
			<p><img alt="" src="https://upload.acmicpc.net/86aa0566-f468-4343-a83d-d978f0120cec/-/preview/" style="width: 354px; height: 353px;"></p>

			<p><그림 6></p>
			</td>
			<td style="width: 50%; text-align: center;">
			<p><img alt="" src="https://upload.acmicpc.net/aebc9d40-2c56-4e6c-b914-d8d9b55f8ff5/-/preview/" style="width: 362px; height: 354px;"></p>

			<p><그림 7></p>
			</td>
		</tr>
	</tbody>
</table>

<p><그림 6>과 <그림 7>은 택시가 3번 승객을 태워 목적지로 이동시키는 경로를 나타낸다. 최종적으로 남은 연료의 양은 15 - 5 - 4 + 4×2 = 14이다.</p>

<p>모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N<sup>2</sup>, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.</p>

<p>다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.</p>

<p>다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.</p>

<p>그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.</p>

### 출력 

 <p>모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력한다. 단, 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다. 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.</p>

