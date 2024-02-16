# 자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진'
# 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트
## 키워드 종류 : '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트'
# 할인율이 적용되는 대여 기간 종류
## 대여 기간이 7일 이상 30일 미만인 경우 : 7일 이상
## 대여 기간이 30일 이상 90일 미만인 경우 : 30일 이상
## 대여 기간이 90일 이상인 경우 : 90일 이상
## 7일 미만인 경우 할인정책 X (WHERE에서 제거?)
# 자동차 종류가 '트럭'인 자동차의
# 대여 금액 desc, 대여 기록 ID desc
WITH CH as (
    SELECT h.HISTORY_ID, c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE, DATEDIFF(h.END_DATE, h.START_DATE) + 1 as DAYS,
        CASE
            WHEN 7 <= DATEDIFF(h.END_DATE, h.START_DATE) + 1 AND DATEDIFF(h.END_DATE, h.START_DATE) + 1 < 30 THEN "7일 이상"
            WHEN 30 <= DATEDIFF(h.END_DATE, h.START_DATE) + 1 AND DATEDIFF(h.END_DATE, h.START_DATE) + 1 < 90 THEN "30일 이상"
            WHEN 90 <= DATEDIFF(h.END_DATE, h.START_DATE) + 1 THEN "90일 이상"
            ELSE NULL
        END as DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h join CAR_RENTAL_COMPANY_CAR c on h.CAR_ID = c.CAR_ID
    WHERE c.CAR_TYPE = "트럭"
)

SELECT ch.HISTORY_ID, IF(ch.DURATION_TYPE is NULL, ch.DAILY_FEE * ch.DAYS
     , FLOOR(ch.DAILY_FEE * ch.DAYS * (1 - discount_rate / 100))) as FEE
FROM CH ch left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    on ch.CAR_TYPE = p.CAR_TYPE and ch.DURATION_TYPE = p.DURATION_TYPE
ORDER BY FEE desc, ch.HISTORY_ID desc