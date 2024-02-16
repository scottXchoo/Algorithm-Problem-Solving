# [level 2] 중성화 여부 파악하기 - 59409 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/59409) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 15:15:17

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
<p>보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다. 중성화된 동물은 <code>SEX_UPON_INTAKE</code> 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.</p>

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
<li>중성화한 동물: Elijah, Ella</li>
<li>중성화하지 않은 동물: Maxwell 2</li>
</ul>

<p>따라서 SQL문을 실행하면 다음과 같이 나와야 합니다. </p>
<table class="table">
        <thead><tr>
<th>ANIMAL_ID</th>
<th>NAME</th>
<th>중성화</th>
</tr>
</thead>
        <tbody><tr>
<td>A355753</td>
<td>Elijah</td>
<td>O</td>
</tr>
<tr>
<td>A373219</td>
<td>Ella</td>
<td>O</td>
</tr>
<tr>
<td>A382192</td>
<td>Maxwell 2</td>
<td>X</td>
</tr>
</tbody>
      </table>
<p>※ 컬럼 이름은 일치하지 않아도 됩니다.</p>

<hr>

<p>본 문제는 <a href="https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes" target="_blank" rel="noopener">Kaggle의 "Austin Animal Center Shelter Intakes and Outcomes"</a>에서 제공하는 데이터를 사용하였으며 <a href="https://opendatacommons.org/licenses/odbl/1.0/" target="_blank" rel="noopener">ODbL</a>의 적용을 받습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges