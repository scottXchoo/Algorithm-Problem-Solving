-- 코드를 입력하세요
# 진료과가 CS or GS인
# 의사 이름, ID, 진료과, 고용일자 조회
# 고용일자 내림차순, 이름 오름차순
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d") as HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = "GS" or MCDP_CD = "CS"
ORDER BY HIRE_YMD desc, DR_NAME