# [level 2] 카테고리 별 상품 개수 구하기 - 131529 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131529) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 14:49:12

### 문제 설명

<p>다음은 어느 의류 쇼핑몰에서 판매중인 상품들의 정보를 담은 <code>PRODUCT</code> 테이블입니다. <code>PRODUCT</code> 테이블은 아래와 같은 구조로 되어있으며, <code>PRODUCT_ID</code>, <code>PRODUCT_CODE</code>, <code>PRICE</code>는 각각 상품 ID, 상품코드, 판매가를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>PRODUCT_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRODUCT_CODE</td>
<td>VARCHAR(8)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRICE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>상품 별로 중복되지 않는 8자리 상품코드 값을 가지며, 앞 2자리는 카테고리 코드를 의미합니다.</p>

<hr>

<h5>문제</h5>

<p><code>PRODUCT</code> 테이블에서 상품 카테고리 코드(<code>PRODUCT_CODE</code> 앞 2자리) 별 상품 개수를 출력하는 SQL문을 작성해주세요. 결과는 상품 카테고리 코드를 기준으로 오름차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>PRODUCT</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>PRODUCT_ID</th>
<th>PRODUCT_CODE</th>
<th>PRICE</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>A1000011</td>
<td>10000</td>
</tr>
<tr>
<td>2</td>
<td>A1000045</td>
<td>9000</td>
</tr>
<tr>
<td>3</td>
<td>C3000002</td>
<td>22000</td>
</tr>
<tr>
<td>4</td>
<td>C3000006</td>
<td>15000</td>
</tr>
<tr>
<td>5</td>
<td>C3000010</td>
<td>30000</td>
</tr>
<tr>
<td>6</td>
<td>K1000023</td>
<td>17000</td>
</tr>
</tbody>
      </table>
<p>상품 카테고리 코드 별 상품은 아래와 같으므로,</p>

<ul>
<li><code>A1</code>: <code>PRODUCT_ID</code>가 1, 2 인 상품</li>
<li><code>C3</code>: <code>PRODUCT_ID</code>가 3, 4, 5 인 상품</li>
<li><code>K1</code>: <code>PRODUCT_ID</code>가 6 인 상품</li>
</ul>

<p>다음과 같은 결과가 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>CATEGORY</th>
<th>PRODUCTS</th>
</tr>
</thead>
        <tbody><tr>
<td>A1</td>
<td>2</td>
</tr>
<tr>
<td>C3</td>
<td>3</td>
</tr>
<tr>
<td>K1</td>
<td>1</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges