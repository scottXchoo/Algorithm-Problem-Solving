# 조회수(VIEWS) in BOARD 테이블
## 가장 높은 중고거래 게시물
# 기본 경로 : "/home/grep/src/" + 게시글 ID + 파일이름(파일 ID + 파일 이름 + 파일 확장자)
# 조회수가 가장 높은 게시물은 딱 하나
# FILE ID desc
SELECT CONCAT("/home/grep/src/", f.BOARD_ID, "/", f.FILE_ID, f.FILE_NAME, f.FILE_EXT) as FILE_PATH
FROM USED_GOODS_FILE f join USED_GOODS_BOARD b using(BOARD_ID)
WHERE b.VIEWS = (select MAX(VIEWS) from USED_GOODS_BOARD)
ORDER BY f.FILE_ID desc