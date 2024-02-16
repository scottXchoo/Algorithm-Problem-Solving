# 중성화 되어있다면 "O" & 아니면 "X"
# 아이디 asc
SELECT ANIMAL_ID, NAME,
    CASE
        WHEN SEX_UPON_INTAKE like "Neutered%" or SEX_UPON_INTAKE like "Spayed%" THEN "O"
        ELSE "X"
    END as 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID