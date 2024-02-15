# 식품분류별로 가격이 제일 비싼 식푹
# 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
# 심품 가격 desc
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) in (
    select CATEGORY, MAX(PRICE)
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY
)
ORDER BY PRICE desc