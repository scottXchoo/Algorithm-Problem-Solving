-- 코드를 입력하세요
# BOOK b & AUTHOR a | AUTHOR_ID : Key
# BOOK b & BOOK_SALES s | BOOK_ID : Key
# 22년 1월(s.SALES_DATE)의 도서 판매 데이터를 기준
# TOTAL_SALES = 판매량(s.SALES) * 판매가(b.PRICE)
# 저자 별 => 카테고리 별 ⭐️⭐️⭐️
# 저자 ID - 오름차순, 카테고리 - 내림차순
WITH BOOK_AUTHOR as (
    select AUTHOR_ID, AUTHOR_NAME, BOOK_ID, CATEGORY, PRICE
    from BOOK b join AUTHOR a using(AUTHOR_ID)
)
SELECT b.AUTHOR_ID, b.AUTHOR_NAME, b.CATEGORY, SUM(b.PRICE * s.SALES) as TOTAL_SALES
FROM BOOK_AUTHOR b, BOOK_SALES s
WHERE b.BOOK_ID = s.BOOK_ID and s.SALES_DATE like "2022-01%"
GROUP BY b.AUTHOR_NAME, b.CATEGORY
ORDER BY b.AUTHOR_ID, b.CATEGORY desc