# 자동차 종류가 'SUV'인 자동차들의 평균 일일대여 요금을 출력
# 평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림
# 컬럼명은 AVERAGE_FEE
# CAR_TYPE과 DAILY_FEE까지는 잘 꺼냈다.
# 그 다음 궁금한 점 :
## 1) 새로운 col(AVERAGE_FEE)는 어떻게 만들지?
## 2) AVG()를 활용하는 것 맞나? 소수 첫 번째 자리에서 반올림 어떻게 하지?
-- 코드를 입력하세요
SELECT ROUND(SUM(DAILY_FEE) / COUNT(*), 0) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV'