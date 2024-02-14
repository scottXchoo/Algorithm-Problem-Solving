# 22년 5월에 예약한 환자 수
# 진료과코드 별로 조회
# 컬럼명 : 진료과 코드, 5월예약건수
# 진료과별 환자 수 asc, 진료과 코드 asc
SELECT MCDP_CD as '진료과 코드', COUNT(*) as "5월예약건수"
FROM APPOINTMENT
WHERE APNT_YMD like "2022-05%"
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD