# [Silver I] 민겸 수 - 21314 

[문제 링크](https://www.acmicpc.net/problem/21314) 

### 성능 요약

메모리: 2028 KB, 시간: 0 ms

### 분류

그리디 알고리즘, 구현

### 제출 일자

2025년 5월 24일 17:49:37

### 문제 설명

<p>민겸이는 로마 숫자를 보고 굉장히 흥미롭다고 생각했다. 그래서 민겸이는 새로운 수 체계인 민겸 수를 창조했다.</p>

<p>민겸 숫자는 0 이상의 정수 <em>N</em>에 대해 10<em><sup>N</sup></em> 또는 5 × 10<em><sup>N</sup></em> 꼴의 십진수를 대문자 <code>M</code>과 <code>K</code>로 이루어진 문자열로 표기한다. 10<em><sup>N</sup></em> 꼴의 십진수는 <em>N </em>+ 1개의 <code>M</code>으로, 5 × 10<em><sup>N</sup></em> 꼴의 십진수는 <em>N</em>개의 <code>M</code> 뒤에 1개의 <code>K</code>를 이어붙인 문자열로 나타낸다. 즉, 아래 표처럼 나타낼 수 있다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 500px;">
	<tbody>
		<tr>
			<td style="text-align: center;">변환 전</td>
			<td style="text-align: center;">변환 후</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>1</code></td>
			<td style="text-align: center;"><code>M</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>5</code></td>
			<td style="text-align: center;"><code>K</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>10</code></td>
			<td style="text-align: center;"><code>MM</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>50</code></td>
			<td style="text-align: center;"><code>MK</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>100</code></td>
			<td style="text-align: center;"><code>MMM</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>500</code></td>
			<td style="text-align: center;"><code>MMK</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>1000</code></td>
			<td style="text-align: center;"><code>MMMM</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>5000</code></td>
			<td style="text-align: center;"><code>MMMK</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>...</code></td>
			<td style="text-align: center;"><code>...</code></td>
		</tr>
	</tbody>
</table>

<p>민겸 수는 한 개 이상의 민겸 숫자를 이어붙여 만든다. 예를 들어, 민겸 수 <code>MKKMMK</code>는 <code>MK</code>, <code>K</code>, <code>MMK</code>의 세 민겸 숫자를 이어붙여 만들 수 있다.</p>

<p>민겸 수를 십진수로 변환할 때는, 1개 이상의 민겸 숫자로 문자열을 분리한 뒤, 각각의 민겸 숫자를 십진수로 변환해서 순서대로 이어붙이면 된다. 민겸 숫자를 십진수로 변환하는 것은 십진수를 민겸 숫자로 변환하는 과정을 거꾸로 하면 된다. 예를 들어, 민겸 수 <code>MKKMMK</code>는 아래 그림과 같이 여러 가지 십진수로 변환할 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/3a65029c-5253-4600-8d93-908e4f368161/-/preview/"></p>

<p>민겸이는 위와 같이 하나의 민겸 수가 다양한 십진수로 변환될 수 있다는 사실을 알았다. 문득 민겸이는 변환될 수 있는 십진수 중 가장 큰 값과 가장 작은 값이 궁금해졌다. 민겸이를 위해 하나의 민겸 수가 십진수로 변환되었을 때 가질 수 있는 최댓값과 최솟값을 구해주자.</p>

### 입력 

 <p>민겸 수 하나가 주어진다. 민겸 수는 대문자 <code>M</code>과 <code>K</code>로만 이루어진 문자열이며, 길이는 3,000을 넘지 않는다.</p>

### 출력 

 <p>주어진 민겸 수가 십진수로 변환되었을 때 가질 수 있는 값 중 가장 큰 값과 가장 작은 값을 두 줄로 나누어 출력한다.</p>

