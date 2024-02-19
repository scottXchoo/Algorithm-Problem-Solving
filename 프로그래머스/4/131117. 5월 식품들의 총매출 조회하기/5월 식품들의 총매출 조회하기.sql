# 두 테이블에서 생산일자가 22년 5월인 식품들 : PRODUCT_ID가 KEY
# 총매출 desc, 식품 ID asc
WITH ORDER_2205 as (
    select PRODUCT_ID, PRODUCE_DATE, SUM(AMOUNT) as AMOUNT
    from FOOD_ORDER
    where PRODUCE_DATE like "2022-05%"
    group by PRODUCT_ID
)

SELECT PRODUCT_ID, PRODUCT_NAME, (p.PRICE * o.AMOUNT) as TOTAL_SALES
FROM FOOD_PRODUCT p join ORDER_2205 o using(PRODUCT_ID)
ORDER BY TOTAL_SALES desc, PRODUCT_ID

# 생산일자가 22년 5월인 식품인데, PRODUCT_ID가 같은게 두 번 찍힌다면? 다 더한다...