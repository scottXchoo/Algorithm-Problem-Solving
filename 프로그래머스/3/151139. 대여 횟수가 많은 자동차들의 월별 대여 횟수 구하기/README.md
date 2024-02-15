# [level 3] 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기 - 151139 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/151139) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2024년 2월 4일 16:39:12

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

<p><code>CAR_RENTAL_COMPANY_RENTAL_HISTORY</code> 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: <code>RECORDS</code>) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬해주세요. 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요.</p>

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
<td>2022-07-27</td>
<td>2022-08-02</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>2022-08-03</td>
<td>2022-08-04</td>
</tr>
<tr>
<td>3</td>
<td>2</td>
<td>2022-08-05</td>
<td>2022-08-05</td>
</tr>
<tr>
<td>4</td>
<td>2</td>
<td>2022-08-09</td>
<td>2022-08-12</td>
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
<td>2022-08-24</td>
<td>2022-08-30</td>
</tr>
<tr>
<td>7</td>
<td>3</td>
<td>2022-10-16</td>
<td>2022-10-19</td>
</tr>
<tr>
<td>8</td>
<td>1</td>
<td>2022-09-03</td>
<td>2022-09-07</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>2022-09-18</td>
<td>2022-09-19</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>2022-09-08</td>
<td>2022-09-10</td>
</tr>
<tr>
<td>11</td>
<td>2</td>
<td>2022-10-16</td>
<td>2022-10-19</td>
</tr>
<tr>
<td>12</td>
<td>1</td>
<td>2022-09-29</td>
<td>2022-10-06</td>
</tr>
<tr>
<td>13</td>
<td>2</td>
<td>2022-10-30</td>
<td>2022-11-01</td>
</tr>
<tr>
<td>14</td>
<td>2</td>
<td>2022-11-05</td>
<td>2022-11-05</td>
</tr>
<tr>
<td>15</td>
<td>3</td>
<td>2022-11-11</td>
<td>2022-11-11</td>
</tr>
</tbody>
      </table>
<p>대여 시작일을 기준으로 총 대여 횟수가 5회 이상인 자동차는 자동차 ID가 1, 2인 자동차입니다. 월 별 자동차 ID별 총 대여 횟수를 구하고 월 오름차순, 자동차 ID 내림차순으로 정렬하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>MONTH</th>
<th>CAR_ID</th>
<th>RECORDS</th>
</tr>
</thead>
        <tbody><tr>
<td>8</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>8</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>9</td>
<td>2</td>
<td>1</td>
</tr>
<tr>
<td>9</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>10</td>
<td>2</td>
<td>2</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges