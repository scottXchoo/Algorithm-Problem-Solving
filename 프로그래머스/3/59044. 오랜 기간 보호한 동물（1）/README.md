# [level 3] 오랜 기간 보호한 동물(1) - 59044 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59044) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > JOIN

### 채점결과

Empty

### 제출 일자

2024년 2월 1일 17:59:6

### 문제 설명

<p><code>ANIMAL_INS</code> 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. <code>ANIMAL_INS</code> 테이블 구조는 다음과 같으며, <code>ANIMAL_ID</code>, <code>ANIMAL_TYPE</code>, <code>DATETIME</code>, <code>INTAKE_CONDITION</code>, <code>NAME</code>, <code>SEX_UPON_INTAKE</code>는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ANIMAL_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>ANIMAL_TYPE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DATETIME</td>
<td>DATETIME</td>
<td>FALSE</td>
</tr>
<tr>
<td>INTAKE_CONDITION</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>SEX_UPON_INTAKE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p><code>ANIMAL_OUTS</code> 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. <code>ANIMAL_OUTS</code> 테이블 구조는 다음과 같으며, <code>ANIMAL_ID</code>, <code>ANIMAL_TYPE</code>, <code>DATETIME</code>, <code>NAME</code>, <code>SEX_UPON_OUTCOME</code>는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. <code>ANIMAL_OUTS</code> 테이블의 <code>ANIMAL_ID</code>는 <code>ANIMAL_INS</code>의 <code>ANIMAL_ID</code>의 외래 키입니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>TYPE</th>
<th>NULLABLE</th>
</tr>
</thead>
        <tbody><tr>
<td>ANIMAL_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>ANIMAL_TYPE</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DATETIME</td>
<td>DATETIME</td>
<td>FALSE</td>
</tr>
<tr>
<td>NAME</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>SEX_UPON_OUTCOME</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.</p>

<h5>예시</h5>

<p>예를 들어, <code>ANIMAL_INS</code> 테이블과 <code>ANIMAL_OUTS</code> 테이블이 다음과 같다면</p>

<p><code>ANIMAL_INS</code></p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>ANIMAL_TYPE</th>
<th>DATETIME</th>
<th>INTAKE_CONDITION</th>
<th>NAME</th>
<th>SEX_UPON_INTAKE</th>
</tr>
</thead>
        <tbody><tr>
<td>A354597</td>
<td>Cat</td>
<td>2014-05-02 12:16:00</td>
<td>Normal</td>
<td>Ariel</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A373687</td>
<td>Dog</td>
<td>2014-03-20 12:31:00</td>
<td>Normal</td>
<td>Rosie</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A412697</td>
<td>Dog</td>
<td>2016-01-03 16:25:00</td>
<td>Normal</td>
<td>Jackie</td>
<td>Neutered Male</td>
</tr>
<tr>
<td>A413789</td>
<td>Dog</td>
<td>2016-04-19 13:28:00</td>
<td>Normal</td>
<td>Benji</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A414198</td>
<td>Dog</td>
<td>2015-01-29 15:01:00</td>
<td>Normal</td>
<td>Shelly</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A368930</td>
<td>Dog</td>
<td>2014-06-08 13:20:00</td>
<td>Normal</td>
<td></td>
<td>Spayed Female</td>
</tr>
</tbody>
      </table>
<p><code>ANIMAL_OUTS</code></p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>ANIMAL_TYPE</th>
<th>DATETIME</th>
<th>NAME</th>
<th>SEX_UPON_OUTCOME</th>
</tr>
</thead>
        <tbody><tr>
<td>A354597</td>
<td>Cat</td>
<td>2014-05-02 12:16:00</td>
<td>Ariel</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A373687</td>
<td>Dog</td>
<td>2014-03-20 12:31:00</td>
<td>Rosie</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A368930</td>
<td>Dog</td>
<td>2014-06-13 15:52:00</td>
<td></td>
<td>Spayed Female</td>
</tr>
</tbody>
      </table>
<p>SQL문을 실행하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>DATETIME</th>
</tr>
</thead>
        <tbody><tr>
<td>Shelly</td>
<td>2015-01-29 15:01:00</td>
</tr>
<tr>
<td>Jackie</td>
<td>2016-01-03 16:25:00</td>
</tr>
<tr>
<td>Benji</td>
<td>2016-04-19 13:28:00</td>
</tr>
</tbody>
      </table>
<p>※ 입양을 가지 못한 동물이 3마리 이상인 경우만 입력으로 주어집니다.</p>

<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges