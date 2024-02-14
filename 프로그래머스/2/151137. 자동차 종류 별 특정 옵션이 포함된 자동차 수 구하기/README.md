# [level 2] 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기 - 151137 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/151137) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2024년 2월 3일 17:27:6

### 문제 설명

<p>다음은 어느 자동차 대여 회사에서 대여중인 자동차들의 정보를 담은 <code>CAR_RENTAL_COMPANY_CAR</code> 테이블입니다. <code>CAR_RENTAL_COMPANY_CAR</code> 테이블은 아래와 같은 구조로 되어있으며, <code>CAR_ID</code>, <code>CAR_TYPE</code>, <code>DAILY_FEE</code>, <code>OPTIONS</code> 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>CAR_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>CAR_TYPE</td>
<td>VARCHAR(255)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DAILY_FEE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>OPTIONS</td>
<td>VARCHAR(255)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다. 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(옵션 리스트 값 예시: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.</p>

<hr>

<h5>문제</h5>

<p><code>CAR_RENTAL_COMPANY_CAR</code> 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 자동차 종류 별로 몇 대인지 출력하는 SQL문을 작성해주세요. 이때 자동차 수에 대한 컬럼명은 <code>CARS</code>로 지정하고, 결과는 자동차 종류를 기준으로 오름차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>CAR_RENTAL_COMPANY_CAR</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>CAR_ID</th>
<th>CAR_TYPE</th>
<th>DAILY_FEE</th>
<th>OPTIONS</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>세단</td>
<td>16000</td>
<td>가죽시트,열선시트,후방카메라</td>
</tr>
<tr>
<td>2</td>
<td>SUV</td>
<td>14000</td>
<td>스마트키,네비게이션,열선시트</td>
</tr>
<tr>
<td>3</td>
<td>SUV</td>
<td>22000</td>
<td>주차감지센서,후방카메라</td>
</tr>
<tr>
<td>4</td>
<td>트럭</td>
<td>35000</td>
<td>주차감지센서,네비게이션,열선시트</td>
</tr>
<tr>
<td>5</td>
<td>SUV</td>
<td>16000</td>
<td>가죽시트,네비게이션,열선시트,후방카메라,주차감지센서</td>
</tr>
</tbody>
      </table>
<p>'통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차는 자동차 ID가 1, 2, 4, 5인 자동차이고, 자동차 종류 별로 몇 대인지 구하고 자동차 종류를 기준으로 오름차순 정렬하면 다음과 같은 결과가 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>CAR_TYPE</th>
<th>CARS</th>
</tr>
</thead>
        <tbody><tr>
<td>SUV</td>
<td>2</td>
</tr>
<tr>
<td>세단</td>
<td>1</td>
</tr>
<tr>
<td>트럭</td>
<td>1</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges