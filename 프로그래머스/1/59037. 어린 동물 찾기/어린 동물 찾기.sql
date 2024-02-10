-- 코드를 입력하세요
# 젊은 동물의 아이디와 이름 조회
# 아이디 오름차순
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != "Aged"
ORDER BY ANIMAL_ID