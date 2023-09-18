# C++ 기초 문법 정리 for 코딩테스트

### substr()

- 정의 : 문자열을 기반으로 숫자로 변환시키는 것
- `substr(시작 인덱스, 원하는 문자열 길이)` : 시작 인덱스부터 문자열 길이까지
    - `substr(시작 인덱스)` : 문자열 끝까지

### c_str()

- 정의 : string을 C style의 문자열로 바꿀 때, 사용하는 함수
- [참고 자료](https://codingdog.tistory.com/entry/c-string-cstr-%ED%95%A8%EC%88%98-string%EC%9D%84-char-%EB%A1%9C-%EB%B0%94%EA%BF%94%EB%B4%85%EC%8B%9C%EB%8B%A4)

### atoi & atof 함수

- atoi : C style의 문자열을 정수(int)로 변환하여 리턴
- atof : C style의 문자열을 실수(float)로 변환하여 리턴

### fill 함수

- `<algorithm>` 헤더 포함
- `fill(초기화 시키고 싶은 부분의 시작 주소, 초기화 시키고 싶은 부분의 끝 주소, 초기화할 값)`
- 배열 : fill(arr, arr + 5, 10);
    
    ```cpp
     // fill(arr, arr + 5, 10); 와 같은 코드
     for(int i = 0; i < 5; i++)
       arr[i] = 10;
      }
    ```
    
- 벡터 : fill(v.begin(), v.end(), 10);
- memset과 다르게 value 자료형에서의 오버플로우가 아니라면, 원하는 값을 넣을 수 있다.
- fill은 memset보다 느리지만, 안전하다.
- 정말 많은 테스트 케이스가 있는 것이 아니면, fill 쓰자

### memeset 함수

- memset(ptr(메모리의 크기를 변경할 포인터나 “배열”), value(초기화 값), size(초기화 크기 반환 값));
    - 반환 값 : 성공 시, ptr & 실패 시, null
- 주의할 점 : 두 번째 인자인 value는 정수 형태로 함수에 넘겨주지만, 실질적으로 memset 함수 안에서 이 value를 `unsigned char`로 바꿔서 메모리 블록을 다루게 된다.
- `unsigned char`로 변환된다는 것은?
    - 1byte 단위로 메모리를 초기화시킨다는 의미
    - 따라서, int형(4byte), long long(8byte)과 같이 자료형이 1byte가 넘어간다면?
        
        ⇒ 값을 자동으로 4byte 혹은 8byte형으로 늘려버린다.
        
    
    ⇒ 즉, int형이나 long long형 등 1바이트가 넘어가는 자료형에서 -1, 0 이외의 수는 원하는 값으로 초기화 X
    
    - char형과 같은 1바이트 자료형은 원하는 값으로 초기화 가능

### vector

- 벡터 v에서 i번째 요소를 삭제하고 싶다면?
    - v.erase(v.begin() + i);
- 벡터 v를 오름차순/내림차순 정렬하고 싶다면?
    - sort(v.begin(), v.end());
    - sort(v.rbegin(), v.rend());

## Tip for 코딩 테스트

- **#include <bits/stdc++.h>**이 있으면, **prev** 라는 변수명을 쓰기 위해 **#define**을 해줘야 된다.
    
    ```cpp
    #include <bits/stdc++.h>
    using namespace std;
    #define prev chooble
    ```
    
- 출력은 문제에 적힌 그대로 적어주기 (Ex. "YES"면 "Yes"로 적지 않기)
- 짝짓기, 폭발, 아름다운 괄호("()") 문제 => Stack 자료구조
- **시간복잡도 :** 천 만 혹은 1억 이하까지는 괜찮음!
- stack.top()을 참조할 때, 항상 stack.size()를 먼저 체크하고 && 사용하기!

### 입력 부분

```cpp
// N x M 크기의 matrix에 입력 값 넣는 로직
int a[10][10]

cin >> n >> m;
for(int i = 0; i < n; i++) {
	for(int j = 0; j < m; j++) {
    	cin >> a[i][j];
    }
}
```

- 띄어쓰기가 있으면, cin X => **getline(cin, s);**
- **"."** 찍힐 때마다, 끊어주려면?
    - while(true) { string s; getline(cin, s); if(s ==".") break; }
- 테스트 케이스마다 로직이 필요하다면? 초기화 중요!
