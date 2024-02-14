# [level 2] 진료과별 총 예약 횟수 출력하기 - 132202 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/132202) 

### 성능 요약

메모리: 0.0 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > GROUP BY

### 채점결과

Empty

### 제출 일자

2024년 2월 3일 17:54:31

### 문제 설명

<p>다음은 종합병원의 진료 예약정보를 담은 <code>APPOINTMENT</code> 테이블 입니다.<br>
<code>APPOINTMENT</code> 테이블은 다음과 같으며 <code>APNT_YMD</code>, <code>APNT_NO</code>, <code>PT_NO</code>, <code>MCDP_CD</code>, <code>MDDR_ID</code>, <code>APNT_CNCL_YN</code>, <code>APNT_CNCL_YMD</code>는 각각 진료예약일시, 진료예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소날짜를 나타냅니다.</p>
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
<td>NUMBER(5)</td>
<td>FALSE</td>
</tr>
<tr>
<td>PT_NO</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>MCDP_CD</td>
<td>VARCHAR(6)</td>
<td>FALSE</td>
</tr>
<tr>
<td>MDDR_ID</td>
<td>VARCHAR(10)</td>
<td>FALSE</td>
</tr>
<tr>
<td>APNT_CNCL_YN</td>
<td>VARCHAR(1)</td>
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

<p><code>APPOINTMENT</code> 테이블에서 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회하는 SQL문을 작성해주세요. 이때, 컬럼명은 '진료과 코드', '5월예약건수'로 지정해주시고 결과는 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬해주세요.</p>

<hr>

<h5>예시</h5>

<p><code>APPOINTMENT</code> 테이블이 다음과 같을 때</p>
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
<td>2022-04-14 09:30:00.000000</td>
<td>47</td>
<td>PT22000064</td>
<td>GS</td>
<td>DR20170123</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-04-15 10:30:00.000000</td>
<td>48</td>
<td>PT22000065</td>
<td>OB</td>
<td>DR20100231</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-15 17:30:00.000000</td>
<td>49</td>
<td>PT22000086</td>
<td>OB</td>
<td>DR20100231</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-18 10:30:00.000000</td>
<td>52</td>
<td>PT22000019</td>
<td>GS</td>
<td>DR20100039</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-19 12:00:00.000000</td>
<td>53</td>
<td>PT22000020</td>
<td>FM</td>
<td>DR20010112</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-22 08:30:00.000000</td>
<td>54</td>
<td>PT22000021</td>
<td>GS</td>
<td>DR20100039</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-04 10:30:00.000000</td>
<td>56</td>
<td>PT22000023</td>
<td>FM</td>
<td>DR20090112</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-14 15:30:00.000000</td>
<td>57</td>
<td>PT22000074</td>
<td>CS</td>
<td>DR20200012</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-24 15:30:00.000000</td>
<td>58</td>
<td>PT22000085</td>
<td>CS</td>
<td>DR20200012</td>
<td>N</td>
<td>NULL</td>
</tr>
<tr>
<td>2022-05-28 10:00:00.000000</td>
<td>60</td>
<td>PT22000092</td>
<td>OS</td>
<td>DR20100031</td>
<td>N</td>
<td>NULL</td>
</tr>
</tbody>
      </table>
<p>SQL을 실행하면 다음과 같이 출력되어야 합니다.</p>
<table class="table">
        <thead><tr>
<th>진료과코드</th>
<th>5월예약건수</th>
</tr>
</thead>
        <tbody><tr>
<td>OB</td>
<td>1</td>
</tr>
<tr>
<td>OS</td>
<td>1</td>
</tr>
<tr>
<td>CS</td>
<td>2</td>
</tr>
<tr>
<td>FM</td>
<td>2</td>
</tr>
<tr>
<td>GS</td>
<td>2</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges