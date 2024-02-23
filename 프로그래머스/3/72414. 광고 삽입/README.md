# [level 3] 광고 삽입 - 72414 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/72414) 

### 성능 요약

메모리: 14.9 MB, 시간: 56.65 ms

### 구분

코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 02월 23일 12:59:31

### 문제 설명

<p><code>카카오TV</code>에서 유명한 크리에이터로 활동 중인 <code>죠르디</code>는 환경 단체로부터 자신의 가장 인기있는 동영상에 지구온난화의 심각성을 알리기 위한 공익광고를 넣어 달라는 요청을 받았습니다. 평소에 환경 문제에 관심을 가지고 있던 "죠르디"는 요청을 받아들였고 광고효과를 높이기 위해 시청자들이 가장 많이 보는 구간에 공익광고를 넣으려고 합니다. "죠르디"는 시청자들이 해당 동영상의 어떤 구간을 재생했는 지 알 수 있는 재생구간 기록을 구했고, 해당 기록을 바탕으로 공익광고가 삽입될 최적의 위치를 고를 수 있었습니다.<br>
참고로 광고는 재생 중인 동영상의 오른쪽 아래에서 원래 영상과 <code>동시에 재생되는</code> PIP(Picture in Picture) 형태로 제공됩니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/597ec277-4451-4289-8817-2970be644a69/2021_kakao_cf_01.png" title="" alt="2021_kakao_cf_01.png"></p>

<p>다음은 "죠르디"가 공익광고가 삽입될 최적의 위치를 고르는 과정을 그림으로 설명한 것입니다.<br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/e733fafb-1e6b-4d30-bbab-a22f366229e7/2021_kakao_cf_02.png" title="" alt="2021_kakao_cf_02.png"></p>

<ul>
<li>그림의 파란색 선은 광고를 검토 중인 "죠르디" 동영상의 전체 재생 구간을 나타냅니다.

<ul>
<li>위 그림에서, "죠르디" 동영상의 총 재생시간은 <code>02시간 03분 55초</code> 입니다.</li>
</ul></li>
<li>그림의 검은색 선들은 각 시청자들이 "죠르디"의 동영상을 재생한 구간의 위치를 표시하고 있습니다.

<ul>
<li>검은색 선의 가운데 숫자는 각 재생 기록을 구분하는 ID를 나타냅니다.</li>
<li>검은색 선에 표기된 왼쪽 끝 숫자와 오른쪽 끝 숫자는 시청자들이 재생한 동영상 구간의 시작 시각과 종료 시각을 나타냅니다.</li>
<li>위 그림에서, 3번 재생 기록은 <code>00시 25분 50초</code> 부터 <code>00시 48분 29초</code> 까지 총 <code>00시간 22분 39초</code> 동안 죠르디의 동영상을 재생했습니다. <sup id="fnref1"><a href="#fn1">1</a></sup></li>
<li>위 그림에서, 1번 재생 기록은 <code>01시 20분 15초</code> 부터 <code>01시 45분 14초</code> 까지 총 <code>00시간 24분 59초</code> 동안 죠르디의 동영상을 재생했습니다.</li>
</ul></li>
<li>그림의 빨간색 선은 "죠르디"가 선택한 최적의 공익광고 위치를 나타냅니다.

<ul>
<li>만약 공익광고의 재생시간이 <code>00시간 14분 15초</code>라면, 위의 그림처럼 <code>01시 30분 59초</code> 부터 <code>01시 45분 14초</code> 까지 공익광고를 삽입하는 것이 가장 좋습니다. 이 구간을 시청한 시청자들의 누적 재생시간이 가장 크기 때문입니다.</li>
<li><code>01시 30분 59초</code> 부터 <code>01시 45분 14초</code> 까지의 누적 재생시간은 다음과 같이 계산됩니다.

<ul>
<li><code>01시 30분 59초</code> 부터 <code>01시 37분 44초</code> 까지 : 4번, 1번 재생 기록이 두차례 있으므로 재생시간의 합은 <code>00시간 06분 45초</code> X 2 = <code>00시간 13분 30초</code></li>
<li><code>01시 37분 44초</code> 부터 <code>01시 45분 14초</code> 까지 : 4번, 1번, 5번 재생 기록이 세차례 있으므로 재생시간의 합은 <code>00시간 07분 30초</code> X 3 = <code>00시간 22분 30초</code></li>
<li>따라서, 이 구간 시청자들의 누적 재생시간은 <code>00시간 13분 30초</code> + <code>00시간 22분 30초</code> = <code>00시간 36분 00초</code>입니다.</li>
</ul></li>
</ul></li>
</ul>

<hr>

<h4><strong>[문제]</strong></h4>

<p>"죠르디"의 동영상 재생시간 길이 play_time, 공익광고의 재생시간 길이 adv_time, 시청자들이 해당 동영상을 재생했던 구간 정보 logs가 매개변수로 주어질 때, 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입하려고 합니다. 이때, 공익광고가 들어갈 <code>시작 시각</code>을 구해서 return 하도록 solution 함수를 완성해주세요. 만약, 시청자들의 누적 재생시간이 가장 많은 곳이 여러 곳이라면, 그 중에서 <code>가장 빠른 시작 시각</code>을 return 하도록 합니다.</p>

<h4><strong>[제한사항]</strong></h4>

<ul>
<li>play_time, adv_time은 길이 8로 고정된 문자열입니다.

<ul>
<li>play_time, adv_time은 <code>HH:MM:SS</code> 형식이며, <code>00:00:01</code> 이상 <code>99:59:59</code> 이하입니다.</li>
<li>즉, 동영상 재생시간과 공익광고 재생시간은 <code>00시간 00분 01초</code> 이상 <code>99시간 59분 59초</code> 이하입니다.</li>
<li>공익광고 재생시간은 동영상 재생시간보다 짧거나 같게 주어집니다.</li>
</ul></li>
<li><p>logs는 크기가 1 이상 300,000 이하인 문자열 배열입니다.</p>

<ul>
<li>logs 배열의 각 원소는 시청자의 재생 구간을 나타냅니다.</li>
<li>logs 배열의 각 원소는 길이가 17로 고정된 문자열입니다.</li>
<li>logs 배열의 각 원소는 <code>H1:M1:S1-H2:M2:S2</code> 형식입니다.

<ul>
<li><code>H1:M1:S1</code>은 동영상이 시작된 시각, <code>H2:M2:S2</code>는 동영상이 종료된 시각을 나타냅니다.</li>
<li><code>H1:M1:S1</code>는 <code>H2:M2:S2</code>보다 1초 이상 이전 시각으로 주어집니다.</li>
<li><code>H1:M1:S1</code>와 <code>H2:M2:S2</code>는 play_time 이내의 시각입니다.</li>
</ul></li>
</ul></li>
<li><p>시간을 나타내는 <code>HH, H1, H2</code>의 범위는 00~99, 분을 나타내는 <code>MM, M1, M2</code>의 범위는  00~59, 초를 나타내는 <code>SS, S1, S2</code>의 범위는 00~59까지 사용됩니다. 잘못된 시각은 입력으로 주어지지 않습니다. (예: <code>04:60:24</code>, <code>11:12:78</code>, <code>123:12:45</code> 등)</p></li>
<li><p>return 값의 형식</p>

<ul>
<li>공익광고를 삽입할 시각을 <code>HH:MM:SS</code> 형식의 8자리 문자열로 반환합니다.</li>
</ul></li>
</ul>

<hr>

<h5><strong>[입출력 예]</strong></h5>
<table class="table">
        <thead><tr>
<th>play_time</th>
<th>adv_time</th>
<th>logs</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td><code>"02:03:55"</code></td>
<td><code>"00:14:15"</code></td>
<td><code>["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]</code></td>
<td><code>"01:30:59"</code></td>
</tr>
<tr>
<td><code>"99:59:59"</code></td>
<td><code>"25:00:00"</code></td>
<td><code>["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]</code></td>
<td><code>"01:00:00"</code></td>
</tr>
<tr>
<td><code>"50:00:00"</code></td>
<td><code>"50:00:00"</code></td>
<td><code>["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]</code></td>
<td><code>"00:00:00"</code></td>
</tr>
</tbody>
      </table>
<h5><strong>입출력 예에 대한 설명</strong></h5>

<hr>

<p><strong>입출력 예 #1</strong><br>
문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong><br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0e58c7f5-2b81-43f2-95e1-c504f17aab9b/2021_kakao_cf_03.png" title="" alt="2021_kakao_cf_03.png"></p>

<p><code>01:00:00</code>에 공익광고를 삽입하면 <code>26:00:00</code>까지 재생되며, 이곳이 가장 좋은 위치입니다. 이 구간의 시청자 누적 재생시간은 다음과 같습니다.</p>

<ul>
<li><code>01:00:00-11:00:00</code> : 해당 구간이 1회(2번 기록) 재생되었으므로 누적 재생시간은 <code>10시간 00분 00초</code> 입니다.</li>
<li><code>11:00:00-21:00:00</code> : 해당 구간이 2회(2번, 4번 기록) 재생되었으므로 누적 재생시간은 <code>20시간 00분 00초</code> 입니다.</li>
<li><code>21:00:00-26:00:00</code> : 해당 구간이 1회(4번 기록) 재생되었으므로 누적 재생시간은 <code>05시간 00분 00초</code> 입니다.</li>
<li>따라서, 이 구간의 시청자 누적 재생시간은 <code>10시간 00분 00초</code> + <code>20시간 00분 00초</code> + <code>05시간 00분 00초</code> = <code>35시간 00분 00초</code> 입니다.</li>
<li>초록색으로 표시된 구간(<code>69:59:59-94:59:59</code>)에 광고를 삽입해도 동일한 결과를 얻을 수 있으나, <code>01:00:00</code>이 <code>69:59:59</code> 보다 빠른 시각이므로, <code>"01:00:00"</code>을 return 합니다.</li>
</ul>

<p><strong>입출력 예 #3</strong><br>
<img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/8e564c82-00ce-4e1a-80fc-5cd96e465a69/2021_kakao_cf_04.png" title="" alt="2021_kakao_cf_04.png"></p>

<p>동영상 재생시간과 공익광고 재생시간이 같으므로, 삽입할 수 있는 위치는 맨 처음(<code>00:00:00</code>)이 유일합니다.</p>

<div class="footnotes">
<hr>
<ol>

<li id="fn1">
<p><code>동영상 재생시간 = 재생이 종료된 시각 - 재생이 시작된 시각</code>(예를 들어, <code>00시 00분 01초</code>부터 <code>00시 00분 10초</code>까지 동영상이 재생되었다면, 동영상 재생시간은 <code>9초</code> 입니다.)&nbsp;<a href="#fnref1">↩</a></p>
</li>

</ol>
</div>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges