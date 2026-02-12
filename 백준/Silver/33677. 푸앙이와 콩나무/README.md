# [Silver I] 푸앙이와 콩나무 - 33677 

[문제 링크](https://www.acmicpc.net/problem/33677) 

### 성능 요약

메모리: 10236 KB, 시간: 16 ms

### 분류

다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 너비 우선 탐색

### 제출 일자

2026년 2월 12일 11:55:26

### 문제 설명

<p>잭과 콩나무를 감명 깊게 읽은 푸앙이는 동화책에 나오는 신비한 힘을 지닌 콩을 구해 하늘나라에 있는 거인의 성에 올라가려고 한다. 하지만 신비한 힘을 지닌 콩을 구하지 못한 푸앙이는 대신 평범한 콩나무에 하루에 한 번씩 물을 주어 하늘나라에 올라가려 한다. 콩나무는 다음 규칙을 따라 자란다.</p>

<ul>
	<li>물을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>만큼 주면 다음 날 콩나무의 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container> 증가한다.</li>
	<li>물을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>만큼 주면 다음 날 콩나무의 길이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>배가 된다.</li>
	<li>물을 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>5</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$5$</span></mjx-container>만큼 주면 다음 날 콩나무의 길이는 제곱이 된다.</li>
	<li>다른 양의 물을 준 경우에는 콩나무의 길이가 변하지 않는다.</li>
</ul>

<p><mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"> <mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>번째 날의 초기 콩나무 길이는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>이다. 푸앙이가 거인의 성에 도착하려면 콩나무의 길이가 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 되어야 하며, 콩나무의 길이가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 된 날에 푸앙이는 거인의 성에 도착할 수 있게 된다. 푸앙이가 거인의 성에 도착하려면 적어도 며칠이 필요할지와 적어도 얼마나 물이 필요할 지 구해보자.</p>

### 입력 

 <p>첫 번째 줄에 거인의 성에 도착하기 위해 필요한 콩나무의 길이 <mjx-container class="MathJax" jax="CHTML" style="font-size: 111.4%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 푸앙이가 거인의 성에 도착하기 위해 필요한 최소 일수와 최소 일수만에 거인의 성에 도착하기 위해 필요한 물의 양의 최솟값을 공백으로 구분하여 출력한다.</p>

