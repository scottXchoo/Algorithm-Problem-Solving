# 게시물 3건 이상 등록한 사용자
# 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력
# 전화번호의 경우 xxx-xxxx-xxxx 같은 형태
# 회원 ID desc
SELECT u.USER_ID, u.NICKNAME, CONCAT_WS(' ', u.CITY, u.STREET_ADDRESS1, u.STREET_ADDRESS2) as 전체주소, CONCAT_WS('-', SUBSTR(u.TLNO, 1, 3), SUBSTR(u.TLNO, 4, 4), SUBSTR(u.TLNO, 8, 4)) as 전화번호
FROM USED_GOODS_BOARD b join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID
GROUP BY u.USER_ID having COUNT(*) >= 3
ORDER BY u.USER_ID desc