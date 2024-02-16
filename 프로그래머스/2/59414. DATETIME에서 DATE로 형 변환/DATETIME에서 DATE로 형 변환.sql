# 각 동물의 아이디, 이름, 들어온 날짜 조회
# 아이디 asc
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, "%Y-%m-%d") as 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID