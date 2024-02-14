# [level 3] 카테고리 별 도서 판매량 집계하기 - 144855 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/144855) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2024년 2월 3일 17:4:16

### 문제 설명

<p>다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(<code>BOOK</code>), 판매 정보(<code>BOOK_SALES</code>) 테이블입니다.</p>

<p><code>BOOK</code> 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
<th>Description</th>
</tr>
</thead>
        <tbody><tr>
<td>BOOK_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
<td>도서 ID</td>
</tr>
<tr>
<td>CATEGORY</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
<td>카테고리 (경제, 인문, 소설, 생활, 기술)</td>
</tr>
<tr>
<td>AUTHOR_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
<td>저자 ID</td>
</tr>
<tr>
<td>PRICE</td>
<td>INTEGER</td>
<td>FALSE</td>
<td>판매가 (원)</td>
</tr>
<tr>
<td>PUBLISHED_DATE</td>
<td>DATE</td>
<td>FALSE</td>
<td>출판일</td>
</tr>
</tbody>
      </table>
<p><code>BOOK_SALES</code> 테이블은 각 도서의 날짜 별 판매량 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
<th>Description</th>
</tr>
</thead>
        <tbody><tr>
<td>BOOK_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
<td>도서 ID</td>
</tr>
<tr>
<td>SALES_DATE</td>
<td>DATE</td>
<td>FALSE</td>
<td>판매일</td>
</tr>
<tr>
<td>SALES</td>
<td>INTEGER</td>
<td>FALSE</td>
<td>판매량</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>2022년 1월</code>의 카테고리 별 도서 판매량을 합산하고, 카테고리(<code>CATEGORY</code>), 총 판매량(<code>TOTAL_SALES</code>) 리스트를 출력하는 SQL문을 작성해주세요. <br>
결과는 카테고리명을 기준으로 오름차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p>예를 들어 <code>BOOK</code> 테이블과 <code>BOOK_SALES</code> 테이블이 다음과 같다면</p>
<table class="table">
        <thead><tr>
<th>BOOK_ID</th>
<th>CATEGORY</th>
<th>AUTHOR_ID</th>
<th>PRICE</th>
<th>PUBLISHED_DATE</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>인문</td>
<td>1</td>
<td>10000</td>
<td>2020-01-01</td>
</tr>
<tr>
<td>2</td>
<td>경제</td>
<td>1</td>
<td>9000</td>
<td>2021-02-05</td>
</tr>
<tr>
<td>3</td>
<td>경제</td>
<td>2</td>
<td>9000</td>
<td>2021-03-11</td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>BOOK_ID</th>
<th>SALES_DATE</th>
<th>SALES</th>
</tr>
</thead>
        <tbody><tr>
<td>1</td>
<td>2022-01-01</td>
<td>2</td>
</tr>
<tr>
<td>2</td>
<td>2022-01-02</td>
<td>3</td>
</tr>
<tr>
<td>1</td>
<td>2022-01-05</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>2022-01-20</td>
<td>5</td>
</tr>
<tr>
<td>2</td>
<td>2022-01-21</td>
<td>6</td>
</tr>
<tr>
<td>3</td>
<td>2022-01-22</td>
<td>2</td>
</tr>
<tr>
<td>2</td>
<td>2022-02-11</td>
<td>3</td>
</tr>
</tbody>
      </table>
<p>2022년 1월의 도서 별 총 판매량은 도서 ID 가 1 인 도서가 총 3권, 도서 ID 가 2 인 도서가 총 14권 이고, 도서 ID 가 3 인 도서가 총 2권 입니다.</p>

<p>카테고리 별로 판매량을 집계한 결과는 다음과 같습니다.</p>
<table class="table">
        <thead><tr>
<th>CATEGORY</th>
<th>TOTAL_SALES</th>
</tr>
</thead>
        <tbody><tr>
<td>인문</td>
<td>3</td>
</tr>
<tr>
<td>경제</td>
<td>16</td>
</tr>
</tbody>
      </table>
<p>카테고리명을 오름차순으로 정렬하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>CATEGORY</th>
<th>TOTAL_SALES</th>
</tr>
</thead>
        <tbody><tr>
<td>경제</td>
<td>16</td>
</tr>
<tr>
<td>인문</td>
<td>3</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges