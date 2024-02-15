# [level 4] 식품분류별 가장 비싼 식품의 정보 조회하기 - 131116 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131116) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2024년 2월 4일 17:43:18

### 문제 설명

<p>다음은 식품의 정보를 담은 <code>FOOD_PRODUCT</code> 테이블입니다. <code>FOOD_PRODUCT</code> 테이블은 다음과 같으며 <code>PRODUCT_ID</code>, <code>PRODUCT_NAME</code>, <code>PRODUCT_CD</code>, <code>CATEGORY</code>, <code>PRICE</code>는 식품 ID, 식품 이름, 식품코드, 식품분류, 식품 가격을 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>PRODUCT_ID</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRODUCT_NAME</td>
<td>VARCHAR(50)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRODUCT_CD</td>
<td>VARCHAR(10)</td>
<td>TRUE</td>
</tr>
<tr>
<td>CATEGORY</td>
<td>VARCHAR(10)</td>
<td>TRUE</td>
</tr>
<tr>
<td>PRICE</td>
<td>NUMBER</td>
<td>TRUE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>FOOD_PRODUCT</code> 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회하는 SQL문을 작성해주세요. 이때 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력시켜 주시고 결과는 식품 가격을 기준으로 내림차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p><code>FOOD_PRODUCT</code> 테이블이 다음과 같을 때</p>
<table class="table">
        <thead><tr>
<th>PRODUCT_ID</th>
<th>PRODUCT_NAME</th>
<th>PRODUCT_CD</th>
<th>CATEGORY</th>
<th>PRICE</th>
</tr>
</thead>
        <tbody><tr>
<td>P0018</td>
<td>맛있는고추기름</td>
<td>CD_OL00008</td>
<td>식용유</td>
<td>6100</td>
</tr>
<tr>
<td>P0019</td>
<td>맛있는카놀라유</td>
<td>CD_OL00009</td>
<td>식용유</td>
<td>5100</td>
</tr>
<tr>
<td>P0020</td>
<td>맛있는산초유</td>
<td>CD_OL00010</td>
<td>식용유</td>
<td>6500</td>
</tr>
<tr>
<td>P0021</td>
<td>맛있는케첩</td>
<td>CD_SC00001</td>
<td>소스</td>
<td>4500</td>
</tr>
<tr>
<td>P0022</td>
<td>맛있는마요네즈</td>
<td>CD_SC00002</td>
<td>소스</td>
<td>4700</td>
</tr>
<tr>
<td>P0039</td>
<td>맛있는황도</td>
<td>CD_CN00008</td>
<td>캔</td>
<td>4100</td>
</tr>
<tr>
<td>P0040</td>
<td>맛있는명이나물</td>
<td>CD_CN00009</td>
<td>캔</td>
<td>3500</td>
</tr>
<tr>
<td>P0041</td>
<td>맛있는보리차</td>
<td>CD_TE00010</td>
<td>차</td>
<td>3400</td>
</tr>
<tr>
<td>P0042</td>
<td>맛있는메밀차</td>
<td>CD_TE00001</td>
<td>차</td>
<td>3500</td>
</tr>
<tr>
<td>P0099</td>
<td>맛있는맛동산</td>
<td>CD_CK00002</td>
<td>과자</td>
<td>1800</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>CATEGORY</th>
<th>MAX_PRICE</th>
<th>PRODUCT_NAME</th>
</tr>
</thead>
        <tbody><tr>
<td>식용유</td>
<td>6500</td>
<td>맛있는산초유</td>
</tr>
<tr>
<td>과자</td>
<td>1800</td>
<td>맛있는맛동산</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges