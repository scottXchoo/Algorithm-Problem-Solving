-- 코드를 입력하세요
# 동일한 회원이 동일한 상품을 다른 DATE에서 구한 데이터 필요
# 이때, 재구매한 회원 ID와 재구매한 상품 ID 출력
# 회원 ID를 기준으로 오름차순 정렬 & 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬
# COUNT를 이용해야될 것 같음
## USER_ID와 PRODUCT_ID를 Key로 이 Key의 개수를 구한 뒤, 그 개수가 2 이상인 친구들을 만들기?

SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(USER_ID) > 1
ORDER BY USER_ID, PRODUCT_ID desc