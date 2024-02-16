# [level 2] 이름에 el이 들어가는 동물 찾기 - 59047 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59047) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 15:22:50

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
<p>보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다. 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.</p>

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
<td>A355753</td>
<td>Dog</td>
<td>2015-09-10 13:14:00</td>
<td>Normal</td>
<td>Elijah</td>
<td>Neutered Male</td>
</tr>
<tr>
<td>A352872</td>
<td>Dog</td>
<td>2015-07-09 17:51:00</td>
<td>Aged</td>
<td>Peanutbutter</td>
<td>Neutered Male</td>
</tr>
<tr>
<td>A353259</td>
<td>Dog</td>
<td>2016-05-08 12:57:00</td>
<td>Injured</td>
<td>Bj</td>
<td>Neutered Male</td>
</tr>
<tr>
<td>A373219</td>
<td>Cat</td>
<td>2014-07-29 11:43:00</td>
<td>Normal</td>
<td>Ella</td>
<td>Spayed Female</td>
</tr>
<tr>
<td>A382192</td>
<td>Dog</td>
<td>2015-03-13 13:14:00</td>
<td>Normal</td>
<td>Maxwell 2</td>
<td>Intact Male</td>
</tr>
</tbody>
      </table>
<ul>
<li>이름에 'el'이 들어가는 동물은 Elijah, Ella, Maxwell 2입니다.</li>
<li>이 중, 개는 Elijah, Maxwell 2입니다.</li>
</ul>

<p>따라서 SQL문을 실행하면 다음과 같이 나와야 합니다. </p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>NAME</th>
</tr>
</thead>
        <tbody><tr>
<td>A355753</td>
<td>Elijah</td>
</tr>
<tr>
<td>A382192</td>
<td>Maxwell 2</td>
</tr>
</tbody>
      </table>
<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges