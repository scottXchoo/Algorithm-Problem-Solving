# ANIMAL_OUTS 테이블의 ANIMAL_ID는 ANIMAL_INS의 ANIMAL_ID의 외래 키입니다.
# 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름
# 보호 기간 desc
SELECT ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O join ANIMAL_INS I using(ANIMAL_ID)
ORDER BY (O.DATETIME - I.DATETIME) desc
LIMIT 2
