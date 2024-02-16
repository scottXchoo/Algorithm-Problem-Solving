# 이름에 "EL"이 들어가는 개의 아이디와 이름 조회
# 결과는 이름 순 asc
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME like "%el%" and ANIMAL_TYPE = "Dog"
ORDER BY NAME