# 입양을 간 기록 O and 보호소에 들어온 기록 X
# 동물 ID asc
WITH ins as (
    select ANIMAL_ID
    from ANIMAL_INS
    group by ANIMAL_ID
)
SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE ANIMAL_ID not in (select ANIMAL_ID from ins)
ORDER BY ANIMAL_ID