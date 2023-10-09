# [Gold I] 동전 뒤집기 - 1285 

[문제 링크](https://www.acmicpc.net/problem/1285) 

### 성능 요약

메모리: 120076 KB, 시간: 11664 ms

### 분류

비트마스킹, 브루트포스 알고리즘, 그리디 알고리즘

### 문제 설명

<p>N<sup>2</sup>개의 동전이 N행 N열을 이루어 탁자 위에 놓여 있다. 그 중 일부는 앞면(H)이 위를 향하도록 놓여 있고, 나머지는 뒷면(T)이 위를 향하도록 놓여 있다. <그림 1>은 N이 3일 때의 예이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ccc3937a-da21-460e-b1f4-2ee861f03995/-/preview/" style="width: 150px; height: 151px;"></p>

<p style="text-align: center;"><그림 1></p>

<p>이들 N<sup>2</sup>개의 동전에 대하여 임의의 한 행 또는 한 열에 놓인 N개의 동전을 모두 뒤집는 작업을 수행할 수 있다. 예를 들어 <그림 1>의 상태에서 첫 번째 열에 놓인 동전을 모두 뒤집으면 <그림 2>와 같이 되고, <그림 2>의 상태에서 첫 번째 행에 놓인 동전을 모두 뒤집으면 <그림 3>과 같이 된다.</p>

<table class="table table-bordered td-center">
	<tbody>
		<tr>
			<td><img alt="" src="https://upload.acmicpc.net/410bd5fd-cb16-4bfb-83af-7edd9882e188/-/preview/" style="width: 150px; height: 151px;"></td>
			<td><img alt="" src="https://upload.acmicpc.net/ae08cc98-4db2-4df7-8bb6-0149d1ca59ba/-/preview/" style="width: 150px; height: 151px;"></td>
		</tr>
		<tr>
			<td><그림 2></td>
			<td><그림 3></td>
		</tr>
	</tbody>
</table>
<p><그림 3>의 상태에서 뒷면이 위를 향하여 놓인 동전의 개수는 두 개이다. <그림 1>의 상태에서 이와 같이 한 행 또는 한 열에 놓인 N개의 동전을 모두 뒤집는 작업을 계속 수행할 때 뒷면이 위를 향하도록 놓인 동전의 개수를 2개보다 작게 만들 수는 없다.</p>

<p>N<sup>2</sup>개의 동전들의 초기 상태가 주어질 때, 한 행 또는 한 열에 놓인 N개의 동전을 모두 뒤집는 작업들을 수행하여 뒷면이 위를 향하는 동전 개수를 최소로 하려 한다. 이때의 최소 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 20이하의 자연수 N이 주어진다. 둘째 줄부터 N줄에 걸쳐 N개씩 동전들의 초기 상태가 주어진다. 각 줄에는 한 행에 놓인 N개의 동전의 상태가 왼쪽부터 차례대로 주어지는데, 앞면이 위를 향하도록 놓인 경우 H, 뒷면이 위를 향하도록 놓인 경우 T로 표시되며 이들 사이에 공백은 없다.</p>

### 출력 

 <p>첫째 줄에 한 행 또는 한 열에 놓인 N개의 동전을 모두 뒤집는 작업들을 수행하여 뒷면이 위를 향하여 놓일 수 있는 동전의 최소 개수를 출력한다.</p>

