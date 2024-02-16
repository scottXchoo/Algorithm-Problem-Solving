# [level 3] 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기 - 164671 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/164671) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 16:32:12

### 문제 설명

<p>다음은 중고거래 게시판 정보를 담은 <code>USED_GOODS_BOARD</code> 테이블과 중고거래 게시판 첨부파일 정보를 담은 <code>USED_GOODS_FILE</code> 테이블입니다. <code>USED_GOODS_BOARD</code> 테이블은 다음과 같으며 <code>BOARD_ID</code>, <code>WRITER_ID</code>, <code>TITLE</code>, <code>CONTENTS</code>, <code>PRICE</code>, <code>CREATED_DATE</code>, <code>STATUS</code>, <code>VIEWS</code>은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.</p>
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
<p><code>USED_GOODS_FILE</code> 테이블은 다음과 같으며 <code>FILE_ID</code>, <code>FILE_EXT</code>, <code>FILE_NAME</code>, <code>BOARD_ID</code>는 각각 파일 ID, 파일 확장자, 파일 이름, 게시글 ID를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>FILE_ID</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>FILE_EXT</td>
<td>VARCHAR(5)</td>
<td>FALSE</td>
</tr>
<tr>
<td>FILE_NAME</td>
<td>VARCHAR(256)</td>
<td>FALSE</td>
</tr>
<tr>
<td>BOARD_ID</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>USED_GOODS_BOARD</code>와 <code>USED_GOODS_FILE</code> 테이블에서 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회하는  SQL문을 작성해주세요. 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬해주세요. 기본적인 파일경로는 /home/grep/src/ 이며, 게시글 ID를 기준으로 디렉토리가 구분되고, 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성되도록 출력해주세요. 조회수가 가장 높은 게시물은 하나만 존재합니다.</p>

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
<td>kwag98</td>
<td>반려견 배변패드 팝니다</td>
<td>정말 저렴히 판매합니다. 전부 미개봉 새상품입니다.</td>
<td>12000</td>
<td>2022-10-01</td>
<td>DONE</td>
<td>250</td>
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
<td>goung12</td>
<td>배드민턴 라켓</td>
<td>사놓고 방치만 해서 팝니다.</td>
<td>9000</td>
<td>2022-10-02</td>
<td>SALE</td>
<td>212</td>
</tr>
<tr>
<td>B0004</td>
<td>keel1990</td>
<td>디올 귀걸이</td>
<td>신세계강남점에서 구입. 정품 아닐시 백퍼센트 환불</td>
<td>130000</td>
<td>2022-10-02</td>
<td>SALE</td>
<td>199</td>
</tr>
<tr>
<td>B0005</td>
<td>haphli01</td>
<td>스팸클래식 팔아요</td>
<td>유통기한 2025년까지에요</td>
<td>10000</td>
<td>2022-10-02</td>
<td>SALE</td>
<td>121</td>
</tr>
</tbody>
      </table>
<p><code>USED_GOODS_FILE</code> 테이블이 다음과 같을 때</p>
<table class="table">
        <thead><tr>
<th>FILE_ID</th>
<th>FILE_EXT</th>
<th>FILE_NAME</th>
<th>BOARD_ID</th>
</tr>
</thead>
        <tbody><tr>
<td>IMG_000001</td>
<td>.jpg</td>
<td>photo1</td>
<td>B0001</td>
</tr>
<tr>
<td>IMG_000002</td>
<td>.jpg</td>
<td>photo2</td>
<td>B0001</td>
</tr>
<tr>
<td>IMG_000003</td>
<td>.png</td>
<td>사진</td>
<td>B0002</td>
</tr>
<tr>
<td>IMG_000004</td>
<td>.jpg</td>
<td>사진</td>
<td>B0003</td>
</tr>
<tr>
<td>IMG_000005</td>
<td>.jpg</td>
<td>photo</td>
<td>B0004</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>FILE_PATH</th>
</tr>
</thead>
        <tbody><tr>
<td>/home/grep/src/B0001/IMG_000001photo1.jpg</td>
</tr>
<tr>
<td>/home/grep/src/B0001/IMG_000002photo2.jpg</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges