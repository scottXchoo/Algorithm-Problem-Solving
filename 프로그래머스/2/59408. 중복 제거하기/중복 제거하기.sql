-- 코드를 입력하세요
# 동물의 이름이 몇 개?
# 이름이 NULL이면 집계 X
SELECT COUNT(DISTINCT NAME) as count
FROM ANIMAL_INS
WHERE NAME is not NULL