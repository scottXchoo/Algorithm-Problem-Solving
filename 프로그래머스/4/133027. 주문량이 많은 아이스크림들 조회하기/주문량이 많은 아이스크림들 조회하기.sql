# FIRST_HALF : FLAVOR
# FIRST_HALF - SHIPMENT_ID는 JULY - SHIPMENT_ID의 외래 키
# JULY - FLAVOR는 FIRST_HALF - FLAVOR 외래 키
# 7월 아이스크림 총 주문량 vs 상반기 아이스크림 총 주문량
# 값이 더 큰 순서대로 상위 3개의 맛 조회
# 같은 맛이라도 다르게 출하될 수 있음
WITH J as (
    select FLAVOR, SUM(TOTAL_ORDER) as TOTAL_ORDER
    from JULY
    group by FLAVOR
),
H as (
    select FLAVOR, SUM(TOTAL_ORDER) as TOTAL_ORDER
    from FIRST_HALF
    group by FLAVOR
)

SELECT FLAVOR
FROM H join J using(FLAVOR)
ORDER BY (H.TOTAL_ORDER + J.TOTAL_ORDER) desc
LIMIT 3
# FROM FIRST_HALF h join JULY j on h.SHIPMENT_ID = j.SHIPMENT_ID and h.FLAVOR = j.SHIPMENT_ID