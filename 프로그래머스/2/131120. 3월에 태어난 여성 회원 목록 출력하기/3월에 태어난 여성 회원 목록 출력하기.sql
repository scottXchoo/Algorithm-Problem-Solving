-- 코드를 입력하세요
# 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일 조회
# 전화번호가 NULL이면, 출력대상에서 제외
# 회원ID 오름차순
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE TLNO is not NULL and DATE_FORMAT(DATE_OF_BIRTH, "%m") = "03" and GENDER = "W"
GROUP BY MEMBER_ID