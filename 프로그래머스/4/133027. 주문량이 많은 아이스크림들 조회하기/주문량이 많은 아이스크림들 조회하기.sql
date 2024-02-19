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