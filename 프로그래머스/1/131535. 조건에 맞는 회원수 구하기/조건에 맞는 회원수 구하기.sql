-- 코드를 입력하세요
# GENDER : 비어있거나 0(남자) or 1(여자)
# 21년에 가입한 회원 중 나이가 20세 이상 29세 이하 (between)인 회원은 몇 명(count)
SELECT COUNT(*) as USERS
FROM USER_INFO
WHERE JOINED like "2021%" and AGE between 20 and 29