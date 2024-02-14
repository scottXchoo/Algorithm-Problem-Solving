# 22년 10월 16일(between START_DATE and END_DATE)에 대여 중이면, "대여중"
# 그렇지 않으면, "대여 가능"으로 표시 as AVAILABILITY (칼럼 추가)
# 자동차 ID desc
SELECT CAR_ID,
        MAX(CASE
            WHEN "2022-10-16" between START_DATE and END_DATE then "대여중"
            ELSE "대여 가능"
        END) as AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID desc