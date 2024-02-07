-- 코드를 입력하세요
# '12세 이하'인 '여자'의 PT_NAME, PT_NO, GEND_CD, AGE, TLNO
# IF TLNO이 없다면, NONE으로 출력
# 나이를 기준으로 내림차순 : ORDER BY AGE desc PT_NAME (이렇게 해도 되는 것 맞나??)
# Q. 순서 정렬에서 내림차순, 오름차순 둘 다 따로 적용하려면?
# TLNO가 없으면, "NONE"으로 어떻게 표시할까? SELECT에서 뭔가 조치? 아니면 WHERE?

SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE')
FROM PATIENT
WHERE AGE <= 12 and GEND_CD = 'W'
ORDER BY AGE desc , PT_NAME