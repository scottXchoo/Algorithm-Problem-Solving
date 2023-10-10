# [Gold IV] 게리맨더링 - 17471 

[문제 링크](https://www.acmicpc.net/problem/17471) 

### 성능 요약

메모리: 116500 KB, 시간: 176 ms

### 분류

너비 우선 탐색, 브루트포스 알고리즘, 조합론, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 수학

### 문제 설명

<p>백준시의 시장 최백준은 지난 몇 년간 게리맨더링을 통해서 자신의 당에게 유리하게 선거구를 획정했다. 견제할 권력이 없어진 최백준은 권력을 매우 부당하게 행사했고, 심지어는 시의 이름도 백준시로 변경했다. 이번 선거에서는 최대한 공평하게 선거구를 획정하려고 한다.</p>

<p>백준시는 N개의 구역으로 나누어져 있고, 구역은 1번부터 N번까지 번호가 매겨져 있다. 구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함되어야 한다. 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다. 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.</p>

<p>아래 그림은 6개의 구역이 있는 것이고, 인접한 구역은 선으로 연결되어 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/08218f4c-2653-4861-a4c1-e7ce808f3a85/-/preview/" style="width: 220px; height: 195px;"></p>

<p>아래는 백준시를 두 선거구로 나눈 4가지 방법이며, 가능한 방법과 불가능한 방법에 대한 예시이다.</p>

<table class="table table-bordered" style="width: 100%;">
	<tbody>
		<tr>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/b82fcf21-6f4c-4797-bda6-215e14099d19/-/preview/" style="width: 220px; height: 195px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/32947e26-4ec4-4b20-99f1-106d8386683d/-/preview/" style="width: 220px; height: 195px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/f5dd6143-c013-46d3-ba4c-dadc48bdf5bc/-/preview/" style="width: 220px; height: 195px;"></td>
			<td style="width: 25%; text-align: center;"><img alt="" src="https://upload.acmicpc.net/548b1153-84de-4b85-9697-2561b019a02b/-/preview/" style="width: 220px; height: 195px;"></td>
		</tr>
		<tr>
			<td style="width: 25%; text-align: center;">
			<p>가능한 방법</p>

			<p>[1, 3, 4]와 [2, 5, 6]으로 나누어져 있다.</p>
			</td>
			<td style="width: 25%; text-align: center;">
			<p>가능한 방법</p>

			<p>[1, 2, 3, 4, 6]과 [5]로 나누어져 있다.</p>
			</td>
			<td style="width: 25%; text-align: center;">
			<p>불가능한 방법</p>

			<p>[1, 2, 3, 4]와 [5, 6]으로 나누어져 있는데, 5와 6이 연결되어 있지 않다.</p>
			</td>
			<td style="width: 25%; text-align: center;">
			<p>불가능한 방법</p>

			<p>각 선거구는 적어도 하나의 구역을 포함해야 한다.</p>
			</td>
		</tr>
	</tbody>
</table>

<p>공평하게 선거구를 나누기 위해 두 선거구에 포함된 인구의 차이를 최소로 하려고 한다. 백준시의 정보가 주어졌을 때, 인구 차이의 최솟값을 구해보자.</p>

### 입력 

 <p>첫째 줄에 구역의 개수 N이 주어진다. 둘째 줄에 구역의 인구가 1번 구역부터 N번 구역까지 순서대로 주어진다. 인구는 공백으로 구분되어져 있다.</p>

<p>셋째 줄부터 N개의 줄에 각 구역과 인접한 구역의 정보가 주어진다. 각 정보의 첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호가 주어진다. 모든 값은 정수로 구분되어져 있다.</p>

<p>구역 A가 구역 B와 인접하면 구역 B도 구역 A와 인접하다. 인접한 구역이 없을 수도 있다.</p>

### 출력 

 <p>첫째 줄에 백준시를 두 선거구로 나누었을 때, 두 선거구의 인구 차이의 최솟값을 출력한다. 두 선거구로 나눌 수 없는 경우에는 -1을 출력한다.</p>

