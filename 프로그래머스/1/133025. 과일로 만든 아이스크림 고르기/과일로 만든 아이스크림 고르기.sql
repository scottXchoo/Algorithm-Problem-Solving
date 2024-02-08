-- 코드를 입력하세요
# 총주문량이 3,000보다 높으면서 and
# 주 성분이 과일인 아이스크림의 맛 조회
# 총 주문량 내림차순
SELECT A.FLAVOR
FROM FIRST_HALF A, ICECREAM_INFO B
WHERE A.FLAVOR = B.FLAVOR and TOTAL_ORDER > 3000 and INGREDIENT_TYPE = "fruit_based"
ORDER BY TOTAL_ORDER desc