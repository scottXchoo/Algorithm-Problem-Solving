# 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일
# 보호 시작일 asc
WITH sub as (
    select ANIMAL_ID, NAME, DATETIME
    from ANIMAL_INS
    order by DATETIME
)

SELECT NAME, DATETIME
FROM sub
WHERE ANIMAL_ID not in (select ANIMAL_ID from ANIMAL_OUTS)
LIMIT 3