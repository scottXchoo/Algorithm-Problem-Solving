# '경제'에 속하는 도서 ID, 저자명, 출판일 출력
# 출판일 asc
SELECT book_id, author_name, DATE_FORMAT(published_date, "%Y-%m-%d") as PUBLISHED_DATE
FROM BOOK b join AUTHOR a using(AUTHOR_ID)
WHERE CATEGORY = "경제"
ORDER BY PUBLISHED_DATE
