# 대여 시작일을 기준으로 22년 8월부터 22년 10월까지
# 총 대여 횟수가 5회 이상인 자동차들
# 월별 자동차 별 총 대여 횟수 as RECORDS
# RECORDS이 0이면, 결과에서 제외
# 월 asc, 자동차 ID desc
WITH checking as (
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between "2022-08-01" and "2022-10-31"
    GROUP BY CAR_ID having COUNT(*) >= 5
)

SELECT MONTH(START_DATE) as MONTH, CAR_ID, COUNT(*) as RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID in (SELECT CAR_ID FROM checking) and START_DATE between "2022-08-01" and "2022-10-31"
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID desc