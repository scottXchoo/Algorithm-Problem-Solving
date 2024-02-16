# 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty
# 아이디 asc
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")
ORDER BY ANIMAL_ID