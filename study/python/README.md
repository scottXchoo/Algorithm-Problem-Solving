# Python 기초 문법 정리 for 코딩테스트

- `[::-1]` : 문자열 거꾸로 출력
- `print(*)` : 한 칸씩 띄우고(공백) 출력
- `set()` : 중복되지 않은 값을 순서없이 보관하는 자료구조
- `eval()` : 문자열로 표현되는 표현식을 실행해서 결괏값을 받아오는 함수
  ```python
  exp = "1 + 2"
  result = eval(exp)
  print(result) # 3
  ```

- sort : 원본 자체 정렬
- sorted : 새로운 list 반환
- lambda : 익명 함수를 지칭하는 용어
  ```python
  # 1. 첫 번째 인자를 기준으로 오름차순 정렬
  # 2. 두 번째 인자를 기준으로 내림차순 정렬
  arr.sort(key = lambda x : (x[0], -x[1]))
  ```
