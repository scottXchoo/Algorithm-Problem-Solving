# [level 3] 조건에 맞는 사용자 정보 조회하기 - 164670 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/164670) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 16:51:13

### 문제 설명

<p>다음은 중고 거래 게시판 정보를 담은 <code>USED_GOODS_BOARD</code> 테이블과 중고 거래 게시판 첨부파일 정보를 담은 <code>USED_GOODS_USER</code> 테이블입니다. <code>USED_GOODS_BOARD</code> 테이블은 다음과 같으며 <code>BOARD_ID</code>, <code>WRITER_ID</code>, <code>TITLE</code>, <code>CONTENTS</code>, <code>PRICE</code>, <code>CREATED_DATE</code>, <code>STATUS</code>, <code>VIEWS</code>는 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>BOARD_ID</td>
<td>VARCHAR(5)</td>
<td>FALSE</td>
</tr>
<tr>
<td>WRITER_ID</td>
<td>VARCHAR(50)</td>
<td>FALSE</td>
</tr>
<tr>
<td>TITLE</td>
<td>VARCHAR(100)</td>
<td>FALSE</td>
</tr>
<tr>
<td>CONTENTS</td>
<td>VARCHAR(1000)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PRICE</td>
<td>NUMBER</td>
<td>FALSE</td>
</tr>
<tr>
<td>CREATED_DATE</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
<tr>
<td>STATUS</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>VIEWS</td>
<td>NUMBER</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p><code>USED_GOODS_USER</code> 테이블은 다음과 같으며 <code>USER_ID</code>, <code>NICKNAME</code>, <code>CITY</code>, <code>STREET_ADDRESS1</code>, <code>STREET_ADDRESS2</code>, <code>TLNO</code>는 각각 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>USER_ID</td>
<td>VARCHAR(50)</td>
<td>FALSE</td>
</tr>
<tr>
<td>NICKANME</td>
<td>VARCHAR(100)</td>
<td>FALSE</td>
</tr>
<tr>
<td>CITY</td>
<td>VARCHAR(100)</td>
<td>FALSE</td>
</tr>
<tr>
<td>STREET_ADDRESS1</td>
<td>VARCHAR(100)</td>
<td>FALSE</td>
</tr>
<tr>
<td>STREET_ADDRESS2</td>
<td>VARCHAR(100)</td>
<td>TRUE</td>
</tr>
<tr>
<td>TLNO</td>
<td>VARCHAR(20)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>USED_GOODS_BOARD</code>와 <code>USED_GOODS_USER</code> 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요. 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(<code>-</code>)을 삽입하여 출력해주세요. 결과는 회원 ID를 기준으로 내림차순 정렬해주세요. </p>

<hr>

<h5>예시</h5>

<p><code>USED_GOODS_BOARD</code> 테이블이 다음과 같고</p>
<table class="table">
        <thead><tr>
<th>BOARD_ID</th>
<th>WRITER_ID</th>
<th>TITLE</th>
<th>CONTENTS</th>
<th>PRICE</th>
<th>CREATED_DATE</th>
<th>STATUS</th>
<th>VIEWS</th>
</tr>
</thead>
        <tbody><tr>
<td>B0001</td>
<td>dhfkzmf09</td>
<td>칼라거펠트 코트</td>
<td>양모 70%이상 코트입니다.</td>
<td>120000</td>
<td>2022-10-14</td>
<td>DONE</td>
<td>104</td>
</tr>
<tr>
<td>B0002</td>
<td>lee871201</td>
<td>국내산 볶음참깨</td>
<td>직접 농사지은 참깨입니다.</td>
<td>3000</td>
<td>2022-10-02</td>
<td>DONE</td>
<td>121</td>
</tr>
<tr>
<td>B0003</td>
<td>dhfkzmf09</td>
<td>나이키 숏패팅</td>
<td>사이즈는 M입니다.</td>
<td>40000</td>
<td>2022-10-17</td>
<td>DONE</td>
<td>98</td>
</tr>
<tr>
<td>B0004</td>
<td>kwag98</td>
<td>반려견 배변패드 팝니다</td>
<td>정말 저렴히 판매합니다. 전부 미개봉 새상품입니다.</td>
<td>12000</td>
<td>2022-10-01</td>
<td>DONE</td>
<td>250</td>
</tr>
<tr>
<td>B0005</td>
<td>dhfkzmf09</td>
<td>PS4</td>
<td>PS5 구매로인해 팝니다.</td>
<td>250000</td>
<td>2022-11-03</td>
<td>DONE</td>
<td>111</td>
</tr>
</tbody>
      </table>
<p><code>USED_GOODS_USER</code> 테이블이 다음과 같을 때</p>
<table class="table">
        <thead><tr>
<th>USER_ID</th>
<th>NICKNAME</th>
<th>CITY</th>
<th>STREET_ADDRESS1</th>
<th>STREET_ADDRESS2</th>
<th>TLNO</th>
</tr>
</thead>
        <tbody><tr>
<td>dhfkzmf09</td>
<td>찐찐</td>
<td>성남시</td>
<td>분당구 수내로 13</td>
<td>A동 1107호</td>
<td>01053422914</td>
</tr>
<tr>
<td>dlPcks90</td>
<td>썹썹</td>
<td>성남시</td>
<td>분당구 수내로 74</td>
<td>401호</td>
<td>01034573944</td>
</tr>
<tr>
<td>cjfwls91</td>
<td>점심만금식</td>
<td>성남시</td>
<td>분당구 내정로 185</td>
<td>501호</td>
<td>01036344964</td>
</tr>
<tr>
<td>dlfghks94</td>
<td>희망</td>
<td>성남시</td>
<td>분당구 내정로 101</td>
<td>203동 102호</td>
<td>01032634154</td>
</tr>
<tr>
<td>rkdhs95</td>
<td>용기</td>
<td>성남시</td>
<td>분당구 수내로 23</td>
<td>501호</td>
<td>01074564564</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>USER_ID</th>
<th>NICKNAME</th>
<th>전체주소</th>
<th>전화번호</th>
</tr>
</thead>
        <tbody><tr>
<td>dhfkzmf09</td>
<td>찐찐</td>
<td>성남시 분당구 수내로 13 A동 1107호</td>
<td>010-5342-2914</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges