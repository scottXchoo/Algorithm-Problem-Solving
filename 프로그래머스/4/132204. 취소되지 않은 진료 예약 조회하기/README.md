# [level 4] 취소되지 않은 진료 예약 조회하기 - 132204 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/132204) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > String， Date

### 채점결과

Empty

### 제출 일자

2024년 2월 5일 15:40:58

### 문제 설명

<p>다음은 환자 정보를 담은 <code>PATIENT</code> 테이블과 의사 정보를 담은 <code>DOCTOR</code> 테이블, 그리고 진료 예약목록을 담은 <code>APPOINTMENT</code>에 대한 테이블입니다. <code>PATIENT</code> 테이블은 다음과 같으며 <code>PT_NO</code>, <code>PT_NAME</code>, <code>GEND_CD</code>, <code>AGE</code>, <code>TLNO</code>는 각각 환자번호, 환자이름, 성별코드, 나이, 전화번호를 의미합니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>PT_NO</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PT_NAME</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>GEND_CD</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>AGE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>TLNO</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
</tbody>
      </table>
<p><code>DOCTOR</code> 테이블은 다음과 같으며 <code>DR_NAME</code>, <code>DR_ID</code>, <code>LCNS_NO</code>, <code>HIRE_YMD</code>, <code>MCDP_CD</code>, <code>TLNO</code>는 각각 의사이름, 의사ID, 면허번호, 고용일자, 진료과코드, 전화번호를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>DR_NAME</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DR_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>LCNS_NO</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>HIRE_YMD</td>
<td>DATE</td>
<td>FALSE</td>
</tr>
<tr>
<td>MCDP_CD</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>TLNO</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
</tbody>
      </table>
<p><code>APPOINTMENT</code> 테이블은 다음과 같으며 <code>APNT_YMD</code>, <code>APNT_NO</code>, <code>PT_NO</code>, <code>MCDP_CD</code>, <code>MDDR_ID</code>, <code>APNT_CNCL_YN</code>, <code>APNT_CNCL_YMD</code>는 각각 진료 예약일시, 진료예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소날짜를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>APNT_YMD</td>
<td>TIMESTAMP</td>
<td>FALSE</td>
</tr>
<tr>
<td>APNT_NO</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>PT_NO</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>MCDP_CD</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>MDDR_ID</td>
<td>VARCHAR(N)</td>
<td>FALSE</td>
</tr>
<tr>
<td>APNT_CNCL_YN</td>
<td>VARCHAR(N)</td>
<td>TRUE</td>
</tr>
<tr>
<td>APNT_CNCL_YMD</td>
<td>DATE</td>
<td>TRUE</td>
</tr>
</tbody>
      </table>
<hr>

<h5>문제</h5>

<p><code>PATIENT</code>, <code>DOCTOR</code> 그리고 <code>APPOINTMENT</code> 테이블에서 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요. 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성해주세요. 결과는 진료예약일시를 기준으로 오름차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p><code>PATIENT</code> 테이블이 다음과 같고,</p>
<table class="table">
        <thead><tr>
<th>PT_NO</th>
<th>PT_NAME</th>
<th>GEND_CD</th>
<th>AGE</th>
<th>TLNO</th>
</tr>
</thead>
        <tbody><tr>
<td>PT22000019</td>
<td>바라</td>
<td>W</td>
<td>10</td>
<td>01079068799</td>
</tr>
<tr>
<td>PT22000043</td>
<td>오스왈드</td>
<td>M</td>
<td>68</td>
<td>01031294124</td>
</tr>
<tr>
<td>PT22000052</td>
<td>제니</td>
<td>W</td>
<td>60</td>
<td>NULL</td>
</tr>
<tr>
<td>PT22000071</td>
<td>몬몬</td>
<td>M</td>
<td>31</td>
<td>01076489209</td>
</tr>
<tr>
<td>PT22000097</td>
<td>슈가</td>
<td>M</td>
<td>19</td>
<td>NULL</td>
</tr>
</tbody>
      </table>
<p><code>DOCTOR</code> 테이블이 다음과 같고,</p>
<table class="table">
        <thead><tr>
<th>DR_NAME</th>
<th>DR_ID</th>
<th>LCNS_NO</th>
<th>HIRE_YMD</th>
<th>MCDP_CD</th>
<th>TLNO</th>
</tr>
</thead>
        <tbody><tr>
<td>루피</td>
<td>DR20090029</td>
<td>LC00010001</td>
<td>2009-03-01</td>
<td>CS</td>
<td>01085482011</td>
</tr>
<tr>
<td>니모</td>
<td>DR20200012</td>
<td>LC00911162</td>
<td>2020-03-01</td>
<td>CS</td>
<td>01089483921</td>
</tr>
<tr>
<td>핑크퐁</td>
<td>DR20140011</td>
<td>LC00082201</td>
<td>2014-03-01</td>
<td>NP</td>
<td>01098428957</td>
</tr>
<tr>
<td>젤라비</td>
<td>DR20160031</td>
<td>LC00340327</td>
<td>2016-11-01</td>
<td>OB</td>
<td>01023981922</td>
</tr>
<tr>
<td>토리</td>
<td>DR20190129</td>
<td>LC00099911</td>
<td>2019-03-01</td>
<td>NS</td>
<td>01058390758</td>
</tr>
</tbody>
      </table>
<p><code>APPOINTMENT</code> 테이블이 다음과 같을 때,</p>
<table class="table">
        <thead><tr>
<th>APNT_YMD</th>
<th>APNT_NO</th>
<th>PT_NO</th>
<th>MCDP_CD</th>
<th>MDDR_ID</th>
<th>APNT_CNCL_YN</th>
<th>APNT_CNCL_YMD</th>
</tr>
</thead>
        <tbody><tr>
<td>2022-04-13 12:30:00.000000</td>
<td>42</td>
<td>PT22000071</td>
<td>CS</td>
<td>DR20090029</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-04-13 15:30:00.000000</td>
<td>43</td>
<td>PT22000019</td>
<td>CS</td>
<td>DR20200012</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-04-13 09:00:00.000000</td>
<td>46</td>
<td>PT22000043</td>
<td>CS</td>
<td>DR20090029</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-07-09 11:00:00.000000</td>
<td>74</td>
<td>PT22000042</td>
<td>NP</td>
<td>DR20100011</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-12-13 12:30:00.000000</td>
<td>110</td>
<td>PT22000097</td>
<td>NP</td>
<td>DR20160011</td>
<td>Y</td>
<td>2022-12-03</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>APNT_NO</th>
<th>PT_NAME</th>
<th>PT_NO</th>
<th>MCDP_CD</th>
<th>DR_NAME</th>
<th>APNT_YMD</th>
</tr>
</thead>
        <tbody><tr>
<td>46</td>
<td>오스왈드</td>
<td>PT22000043</td>
<td>CS</td>
<td>루피</td>
<td>2022-04-13 09:00:00.000000</td>
</tr>
<tr>
<td>42</td>
<td>몬몬</td>
<td>PT22000071</td>
<td>CS</td>
<td>루피</td>
<td>2022-04-13 12:30:00.000000</td>
</tr>
<tr>
<td>43</td>
<td>바라</td>
<td>PT22000019</td>
<td>CS</td>
<td>니모</td>
<td>2022-04-13 15:30:00.000000</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges