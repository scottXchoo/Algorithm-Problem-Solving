-- 코드를 입력하세요
# 아이디 - 오름차순
# 이름이 없는 동물은 "No name"
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") as NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID