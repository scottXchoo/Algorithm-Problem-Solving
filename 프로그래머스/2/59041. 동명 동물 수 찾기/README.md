# [level 2] 동명 동물 수 찾기 - 59041 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59041) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2024년 2월 4일 17:56:1

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
<p>동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요. </p>

<h5>예시</h5>

<p>예를 들어 <code>ANIMAL_INS</code> 테이블이 다음과 같다면</p>
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
<td>A396810</td>
<td>Dog</td>
<td>2016-08-22 16:13:00</td>
<td>Injured</td>
<td>Raven</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A377750</td>
<td>Dog</td>
<td>2017-10-25 17:17:00</td>
<td>Normal</td>
<td>Lucy</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A355688</td>
<td>Dog</td>
<td>2014-01-26 13:48:00</td>
<td>Normal</td>
<td>Shadow</td>
<td>Neutered Male</td>
</tr>
<tr>
<td>A399421</td>
<td>Dog</td>
<td>2015-08-25 14:08:00</td>
<td>Normal</td>
<td>Lucy</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A400680</td>
<td>Dog</td>
<td>2017-06-17 13:29:00</td>
<td>Normal</td>
<td>Lucy</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A410668</td>
<td>Cat</td>
<td>2015-11-19 13:41:00</td>
<td>Normal</td>
<td>Raven</td>
<td>Spayed Female</td>
</tr>
</tbody>
      </table>
<ul>
<li>Raven 이름은 2번 쓰였습니다.</li>
<li>Lucy 이름은 3번 쓰였습니다</li>
<li>Shadow 이름은 1번 쓰였습니다.</li>
</ul>

<p>따라서 SQL문을 실행하면 다음과 같이 나와야 합니다. </p>
<table class="table">
        <thead><tr>
<th>NAME</th>
<th>COUNT</th>
</tr>
</thead>
        <tbody><tr>
<td>Lucy</td>
<td>3</td>
</tr>
<tr>
<td>Raven</td>
<td>2</td>
</tr>
</tbody>
      </table>
<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges