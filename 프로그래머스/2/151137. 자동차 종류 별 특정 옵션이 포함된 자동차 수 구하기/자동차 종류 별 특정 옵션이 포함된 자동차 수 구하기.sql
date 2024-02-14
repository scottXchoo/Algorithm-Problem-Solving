# 통풍시트, 열선시트, 가죽시트 중 하나 이상의 옵션이 포함된
# 종류별로 몇 대인지 출력 as CARS
# 자동차 종류 - asc
SELECT CAR_TYPE, COUNT(*) as CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS like "%통풍시트%"
or OPTIONS like "%열선시트%"
or OPTIONS like "%가죽시트%"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE