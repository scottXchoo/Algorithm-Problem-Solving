# 보호 시작일 > 입양일 : 이런 동물 찾아라
# 보호 시작일 asc
SELECT o.ANIMAL_ID, o.NAME
FROM ANIMAL_INS i join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID and i.DATETIME > o.DATETIME
ORDER BY i.DATETIME