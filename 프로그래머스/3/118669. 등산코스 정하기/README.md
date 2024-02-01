# [level 3] 등산코스 정하기 - 118669 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/118669) 

### 성능 요약

메모리: 91.3 MB, 시간: 636.99 ms

### 구분

코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 2월 4일 14:29:0

### 문제 설명

<p>XX산은 <code>n</code>개의 지점으로 이루어져 있습니다. 각 지점은 1부터 <code>n</code>까지 번호가 붙어있으며, 출입구, 쉼터, 혹은 산봉우리입니다. 각 지점은 양방향 통행이 가능한 등산로로 연결되어 있으며, 서로 다른 지점을 이동할 때 이 등산로를 이용해야 합니다. 이때, 등산로별로 이동하는데 일정 시간이 소요됩니다.</p>

<p>등산코스는 방문할 지점 번호들을 순서대로 나열하여 표현할 수 있습니다.<br>
예를 들어 <code>1-2-3-2-1</code> 으로 표현하는 등산코스는 1번지점에서 출발하여 2번, 3번, 2번, 1번 지점을 순서대로 방문한다는 뜻입니다.<br>
등산코스를 따라 이동하는 중 쉼터 혹은 산봉우리를 방문할 때마다 휴식을 취할 수 있으며, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 <code>intensity</code>라고 부르기로 합니다.</p>

<p>당신은 XX산의 출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 다시 <strong>원래의</strong> 출입구로 돌아오는 등산코스를 정하려고 합니다. 다시 말해, 등산코스에서 출입구는 <strong>처음과 끝에 한 번씩</strong>, 산봉우리는 <strong>한 번만</strong> 포함되어야 합니다.<br>
당신은 이러한 규칙을 지키면서 <code>intensity</code>가 최소가 되도록 등산코스를 정하려고 합니다.</p>

<p>다음은 XX산의 지점과 등산로를 그림으로 표현한 예시입니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/d1764091-629a-414b-9f77-e2ff1b38c6e0/desc1-1.PNG" title="" alt="desc1-1.PNG"></p>

<ul>
<li>위 그림에서 원에 적힌 숫자는 지점의 번호를 나타내며, 1, 3번 지점에 출입구, 5번 지점에 산봉우리가 있습니다. 각 선분은 등산로를 나타내며, 각 선분에 적힌 수는 이동 시간을 나타냅니다. 예를 들어 1번 지점에서 2번 지점으로 이동할 때는 3시간이 소요됩니다.</li>
</ul>

<p>위의 예시에서 <code>1-2-5-4-3</code> 과 같은 등산코스는 처음 출발한 원래의 출입구로 돌아오지 않기 때문에 잘못된 등산코스입니다. 또한 <code>1-2-5-6-4-3-2-1</code> 과 같은 등산코스는 코스의 처음과 끝 외에 3번 출입구를 방문하기 때문에 잘못된 등산코스입니다.</p>

<p>등산코스를 <code>3-2-5-4-3</code> 과 같이 정했을 때의 이동경로를 그림으로 나타내면 아래와 같습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/ae2b6ccd-290b-4074-aebe-028c13dc4cbe/desc1-2.PNG" title="" alt="desc1-2.PNG"><br>
이때, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간은 5시간입니다. 따라서 이 등산코스의 <code>intensity</code>는 5입니다.</p>

<p>등산코스를 <code>1-2-4-5-6-4-2-1</code> 과 같이 정했을 때의 이동경로를 그림으로 나타내면 아래와 같습니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/165bcca3-ee06-46b4-95f8-7c3cedd2cb42/desc1-3.PNG" title="" alt="desc1-3.PNG"><br>
이때, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간은 3시간입니다. 따라서 이 등산코스의 <code>intensity</code>는 3이며, 이 보다 <code>intensity</code>가 낮은 등산코스는 없습니다.</p>

<p>XX산의 지점 수 <code>n</code>, 각 등산로의 정보를 담은 2차원 정수 배열 <code>paths</code>, 출입구들의 번호가 담긴 정수 배열 <code>gates</code>, 산봉우리들의 번호가 담긴 정수 배열 <code>summits</code>가 매개변수로 주어집니다. 이때, <code>intensity</code>가 최소가 되는 등산코스에 포함된 산봉우리 번호와 <code>intensity</code>의 최솟값을 차례대로 정수 배열에 담아 return 하도록 solution 함수를 완성해주세요. <code>intensity</code>가 최소가 되는 등산코스가 여러 개라면 그중 산봉우리의 번호가 가장 낮은 등산코스를 선택합니다.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>n</code> ≤ 50,000</li>
<li><code>n</code> - 1 ≤ <code>paths</code>의 길이 ≤ 200,000</li>
<li><code>paths</code>의 원소는 <code>[i, j, w]</code> 형태입니다.

<ul>
<li><code>i</code>번 지점과 <code>j</code>번 지점을 연결하는 등산로가 있다는 뜻입니다.</li>
<li><code>w</code>는 두 지점 사이를 이동하는 데 걸리는 시간입니다.</li>
<li>1 ≤ <code>i</code> &lt; <code>j</code> ≤ <code>n</code></li>
<li>1 ≤ <code>w</code> ≤ 10,000,000</li>
<li>서로 다른 두 지점을 직접 연결하는 등산로는 최대 1개입니다.</li>
</ul></li>
<li>1 ≤ <code>gates</code>의 길이 ≤ <code>n</code>

<ul>
<li>1 ≤ <code>gates</code>의 원소 ≤ <code>n</code></li>
<li><code>gates</code>의 원소는 해당 지점이 출입구임을 나타냅니다.</li>
</ul></li>
<li>1 ≤ <code>summits</code>의 길이 ≤ <code>n</code>

<ul>
<li>1 ≤ <code>summits</code>의 원소 ≤ <code>n</code></li>
<li><code>summits</code>의 원소는 해당 지점이 산봉우리임을 나타냅니다.</li>
</ul></li>
<li>출입구이면서 동시에 산봉우리인 지점은 없습니다.</li>
<li><code>gates</code>와 <code>summits</code>에 등장하지 않은 지점은 모두 쉼터입니다.</li>
<li>임의의 두 지점 사이에 이동 가능한 경로가 항상 존재합니다.</li>
<li>return 하는 배열은 <code>[산봉우리의 번호, intensity의 최솟값]</code> 순서여야 합니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>paths</th>
<th>gates</th>
<th>summits</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>6</td>
<td>[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]</td>
<td>[1, 3]</td>
<td>[5]</td>
<td>[5, 3]</td>
</tr>
<tr>
<td>7</td>
<td>[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]</td>
<td>[1]</td>
<td>[2, 3, 4]</td>
<td>[3, 4]</td>
</tr>
<tr>
<td>7</td>
<td>[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]</td>
<td>[3, 7]</td>
<td>[1, 5]</td>
<td>[5, 1]</td>
</tr>
<tr>
<td>5</td>
<td>[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]</td>
<td>[1, 2]</td>
<td>[5]</td>
<td>[5, 6]</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 예시와 같습니다. 등산코스의 <code>intensity</code>가 최소가 되는 산봉우리 번호는 5, <code>intensity</code>의 최솟값은 3이므로 <code>[5, 3]</code>을 return 해야 합니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p>XX산의 지점과 등산로를 그림으로 표현하면 아래와 같습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/b978b0f5-7e8b-4dbe-aeb0-a6c21a3431e4/ex2.PNG" title="" alt="ex2.PNG"></p>

<p>가능한 <code>intensity</code>의 최솟값은 4이며, <code>intensity</code>가 4가 되는 등산코스는 <code>1-4-1</code> 과 <code>1-7-3-7-1</code> 이 있습니다. <code>intensity</code>가 최소가 되는 등산코스가 여러 개이므로 둘 중 산봉우리의 번호가 낮은 <code>1-7-3-7-1</code> 을 선택합니다. 따라서 <code>[3, 4]</code>를 return 해야 합니다.</p>

<p><strong>입출력 예 #3</strong></p>

<p>XX산의 지점과 등산로를 그림으로 표현하면 아래와 같습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/53399b93-368c-42bd-ad68-1230f59479c8/ex3.PNG" title="" alt="ex3.PNG"></p>

<p>가능한 <code>intensity</code>의 최솟값은 1이며, 그때의 등산코스는 <code>7-6-5-6-7</code> 입니다. 따라서 <code>[5, 1]</code>를 return 해야 합니다.</p>

<ul>
<li><code>7-6-5-4-1-4-5-6-7</code> 과 같은 등산코스는 산봉우리를 여러 번 방문하기 때문에 잘못된 등산코스입니다.</li>
</ul>

<p><strong>입출력 예 #4</strong></p>

<p>XX산의 지점과 등산로를 그림으로 표현하면 아래와 같습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0abfa9ed-7b1a-4619-a23d-1becf94d1bc3/ex4.PNG" title="" alt="ex4.PNG"></p>

<p>가능한 <code>intensity</code>의 최솟값은 6, 그때의 등산코스는 <code>2-4-5-4-2</code> 입니다. 따라서 <code>[5, 6]</code>을 return 해야 합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges