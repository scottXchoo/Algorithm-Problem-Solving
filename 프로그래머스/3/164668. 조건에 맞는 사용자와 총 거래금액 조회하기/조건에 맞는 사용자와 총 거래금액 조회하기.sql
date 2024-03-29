-- 코드를 입력하세요
# 완료된 중고 거래의 총금액이 70만 원 이상인 사람
# 총거래금액 - 오름차순
SELECT u.USER_ID, u.NICKNAME, SUM(b.PRICE) as TOTAL_SALES
FROM USED_GOODS_USER u join USED_GOODS_BOARD b on b.WRITER_ID = u.USER_ID
WHERE b.STATUS = "DONE"
GROUP BY b.WRITER_ID having SUM(b.PRICE) >= 700000
ORDER BY TOTAL_SALES