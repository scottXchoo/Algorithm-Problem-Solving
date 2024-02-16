# [level 3] 오랜 기간 보호한 동물(2) - 59411 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59411) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 15:7:15

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
<p>입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.</p>

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
<td>A362707</td>
<td>Dog</td>
<td>2016-01-27 12:27:00</td>
<td>Sick</td>
<td>Girly Girl</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A370507</td>
<td>Cat</td>
<td>2014-10-27 14:43:00</td>
<td>Normal</td>
<td>Emily</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A414513</td>
<td>Dog</td>
<td>2016-06-07 09:17:00</td>
<td>Normal</td>
<td>Rocky</td>
<td>Neutered Male</td>
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
<td>2014-06-03 12:30:00</td>
<td>Ariel</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A362707</td>
<td>Dog</td>
<td>2017-01-10 10:44:00</td>
<td>Girly Girl</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A370507</td>
<td>Cat</td>
<td>2015-08-15 09:24:00</td>
<td>Emily</td>
<td>Spayed Female</td>
</tr>
</tbody>
      </table>
<p>SQL문을 실행하면 다음과 같이 나와야 합니다.</p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>NAME</th>
</tr>
</thead>
        <tbody><tr>
<td>A362707</td>
<td>Girly Girl</td>
</tr>
<tr>
<td>A370507</td>
<td>Emily</td>
</tr>
</tbody>
      </table>
<p>※ 입양을 간 동물이 2마리 이상인 경우만 입력으로 주어집니다.</p>

<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges