# [level 2] 자동차 평균 대여 기간 구하기 - 157342 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/157342) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 15:55:24

### 문제 설명

<p>다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은 <code>CAR_RENTAL_COMPANY_RENTAL_HISTORY</code> 테이블입니다. <code>CAR_RENTAL_COMPANY_RENTAL_HISTORY</code> 테이블은 아래와 같은 구조로 되어있으며, <code>HISTORY_ID</code>, <code>CAR_ID</code>, <code>START_DATE</code>, <code>END_DATE</code> 는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>HISTORY_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>CAR_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>START_DATE</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
<tr>
<td>END_DATE</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>CAR_RENTAL_COMPANY_RENTAL_HISTORY</code> 테이블에서 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID와 평균 대여 기간(컬럼명: <code>AVERAGE_DURATION</code>) 리스트를 출력하는 SQL문을 작성해주세요. 평균 대여 기간은 소수점 두번째 자리에서 반올림하고, 결과는 평균 대여 기간을 기준으로 내림차순 정렬해주시고, 평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>CAR_RENTAL_COMPANY_RENTAL_HISTORY</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>HISTORY_ID</th>
<th>CAR_ID</th>
<th>START_DATE</th>
<th>END_DATE</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>1</td>
<td>2022-09-27</td>
<td>2022-10-01</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>2022-10-03</td>
<td>2022-11-04</td>
</tr>
<tr>
<td>3</td>
<td>2</td>
<td>2022-09-05</td>
<td>2022-09-05</td>
</tr>
<tr>
<td>4</td>
<td>2</td>
<td>2022-09-08</td>
<td>2022-09-10</td>
</tr>
<tr>
<td>5</td>
<td>3</td>
<td>2022-09-16</td>
<td>2022-10-15</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
<td>2022-11-07</td>
<td>2022-12-06</td>
</tr>
</tbody>
      </table>
<p>자동차 별 평균 대여 기간은</p>

<ul>
<li>자동차 ID가 1인 자동차의 경우, 대여 기간이 각각 5일, 33일, 30일인 기록이 존재하므로 평균 22.7일</li>
<li>자동차 ID가 2인 자동차의 경우, 대여 기간이 각각 1일, 3일인 기록이 존재하므로 평균 2일</li>
<li>자동차 ID가 3인 자동차의 경우, 대여 기간이 30일인 기록만 존재하므로 평균 30일
입니다. 평균 대여 기간이 7일 이상인 자동차는 자동차 ID가 1, 3인 자동차이고, 평균 대여 기간 내림차순 및 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th>CAR_ID</th>
<th>AVERAGE_DURATION</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>30.0</td>
</tr>
<tr>
<td>1</td>
<td>22.7</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges