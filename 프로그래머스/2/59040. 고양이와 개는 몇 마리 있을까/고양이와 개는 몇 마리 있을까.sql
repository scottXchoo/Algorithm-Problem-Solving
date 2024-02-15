# 고양이와 개가 각각 몇 마리인지 조회
# 고양이를 개보다 먼저 조회 asc
SELECT ANIMAL_TYPE, COUNT(*) as count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE