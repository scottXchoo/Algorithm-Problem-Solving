# [level 4] 우유와 요거트가 담긴 장바구니 - 62284 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/62284) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > Summer／Winter Coding（2019）

### 채점결과

Empty

### 제출 일자

2024년 02월 24일 12:14:38

### 문제 설명

<p><code>CART_PRODUCTS</code> 테이블은 장바구니에 담긴 상품 정보를 담은 테이블입니다. <code>CART_PRODUCTS</code> 테이블의 구조는 다음과 같으며, <code>ID</code>, <code>CART_ID</code>, <code>NAME</code>, <code>PRICE</code>는 각각 테이블의 아이디, 장바구니의 아이디, 상품 종류, 가격을 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
</tr>
</thead>
        <tbody><tr>
<td>ID</td>
<td>INT</td>
</tr>
<tr>
<td>CART_ID</td>
<td>INT</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR</td>
</tr>
<tr>
<td>PRICE</td>
<td>INT</td>
</tr>
</tbody>
      </table>
<p>데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.</p>

<h5>예시</h5>

<p>예를 들어 <code>CART_PRODUCTS</code> 테이블이 다음과 같다면</p>

<p><code>CART_PRODUCTS</code> 테이블</p>
<table class="table">
        <thead><tr>
<th>ID</th>
<th>CART_ID</th>
<th>NAME</th>
<th>PRICE</th>
</tr>
</thead>
        <tbody><tr>
<td>1630</td>
<td>83</td>
<td>Cereal</td>
<td>3980</td>
</tr>
<tr>
<td>1631</td>
<td>83</td>
<td>Multipurpose Supply</td>
<td>3900</td>
</tr>
<tr>
<td>5491</td>
<td>286</td>
<td>Yogurt</td>
<td>2980</td>
</tr>
<tr>
<td>5504</td>
<td>286</td>
<td>Milk</td>
<td>1880</td>
</tr>
<tr>
<td>8435</td>
<td>448</td>
<td>Milk</td>
<td>1880</td>
</tr>
<tr>
<td>8437</td>
<td>448</td>
<td>Yogurt</td>
<td>2980</td>
</tr>
<tr>
<td>8438</td>
<td>448</td>
<td>Tea</td>
<td>11000</td>
</tr>
<tr>
<td>20236</td>
<td>1034</td>
<td>Yogurt</td>
<td>2980</td>
</tr>
<tr>
<td>20237</td>
<td>1034</td>
<td>Butter</td>
<td>4890</td>
</tr>
</tbody>
      </table>
<ul>
<li>83번 장바구니에는 Milk와 Yogurt가 모두 없습니다.</li>
<li>286번 장바구니에는 Milk와 Yogurt가 모두 있습니다.</li>
<li>448번 장바구니에는 Milk와 Yogurt가 모두 있습니다.</li>
<li>1034번 장바구니에는 Milk는 없고 Yogurt만 있습니다.</li>
</ul>

<p>따라서 SQL 문을 실행하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>CART_ID</th>
</tr>
</thead>
        <tbody><tr>
<td>286</td>
</tr>
<tr>
<td>448</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges