# 테이블 CAR, RENTAL_HISTORY, DISCOUNT_PLAN
# 자동차 종류가 '세단' or 'SUV' 중 CAR
# 종류 별 30일간의 대여 금액이 50만 원 이상 200만 원 미만 DISCOUNT_PLAN
## 두 테이블을 먼저 엮고
# 22년 11월 1일 ~ 30일까지 대여 가능하고
## 이런 자동차의 ID, 종류, 대여 금액 as FEE
# FEE desc, 종류 asc, ID desc

WITH DIS_30DAY as (
    select CAR_TYPE, DISCOUNT_RATE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where DURATION_TYPE = "30일 이상" and CAR_TYPE in ("세단", "SUV")
),
NOT_AVAIL as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE <= '2022-11-01' and END_DATE >= '2022-11-01'
    
)

SELECT CAR_ID, c.CAR_TYPE, FLOOR((30 * c.DAILY_FEE * (1 - d.DISCOUNT_RATE / 100))) as FEE
FROM CAR_RENTAL_COMPANY_CAR c join DIS_30DAY d on c.CAR_TYPE = d.CAR_TYPE
WHERE CAR_ID not in (select CAR_ID from NOT_AVAIL) having FEE between 500000 and 2000000
ORDER BY FEE desc, CAR_TYPE, CAR_ID desc

# CAR_DIS as (
#     select CAR_ID, CAR_TYPE, FLOOR((30 * DAILY_FEE * (1 - d.DISCOUNT_RATE / 100))) as FEE
#     from CAR_RENTAL_COMPANY_CAR c join DIS_30DAY d using(CAR_TYPE)
#     where CAR_TYPE in ("세단", "SUV") having 500000 <= FEE and FEE < 2000000
# )