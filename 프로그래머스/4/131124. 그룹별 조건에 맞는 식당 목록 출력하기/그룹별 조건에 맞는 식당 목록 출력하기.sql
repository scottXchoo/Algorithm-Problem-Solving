# MEMBER_PROFILE p
# REST_REVIEW r
## p.MEMBER_ID = r.MEMBER_ID
# p와 r 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰 조회
# 리뷰를 가장 많이 작성한 회원의 MEMBER_ID를 알아야겠다.
# 그 ID에 해당하는 애들을 보여주기
WITH review_cnt as (
    select MEMBER_ID, COUNT(*) as cnt
    from REST_REVIEW
    group by MEMBER_ID
    ORDER BY cnt desc
    LIMIT 1
)

SELECT p.MEMBER_NAME, r.REVIEW_TEXT, DATE_FORMAT(r.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
FROM MEMBER_PROFILE p join REST_REVIEW r using(MEMBER_ID)
WHERE MEMBER_ID = (SELECT MEMBER_ID
                  FROM review_cnt)
ORDER BY REVIEW_DATE, r.REVIEW_TEXT