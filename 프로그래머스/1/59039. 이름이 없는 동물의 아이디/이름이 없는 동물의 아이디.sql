-- 코드를 입력하세요
# 이름이 NULL인 동물의 ID를 보여줘라
# ID - 오름차순
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is NULL
ORDER BY ANIMAL_ID
