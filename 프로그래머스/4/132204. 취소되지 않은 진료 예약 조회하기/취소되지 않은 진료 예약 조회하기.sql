# PATIENT, DOCTOR, APPOINTMENT : 환자번호(PT_NO) / 의사ID(DR_ID & MDDR_ID)
# 22년 4월 13일 취소되지 않은 CS 진료 예약 내역을 조회
# 진료예약일시 asc
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
FROM APPOINTMENT a join DOCTOR d on d.DR_ID = a.MDDR_ID join PATIENT p using(PT_NO)
WHERE a.APNT_CNCL_YN = "N" and a.APNT_YMD like "2022-04-13%" and a.MCDP_CD = "CS"
ORDER BY a.APNT_YMD