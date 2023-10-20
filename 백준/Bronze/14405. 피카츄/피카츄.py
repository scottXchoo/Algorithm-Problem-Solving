import sys
word = str(sys.stdin.readline().rstrip("\n"))

# replace를 통해 "pi", "ka", "chu" 발음을 띄어쓰기로 바꾼다.
word = word.replace("pi", " ")
word = word.replace("ka", " ")
word = word.replace("chu", " ")

# .strip()을 통해 띄어쓰기를 붙였을 때 길이가 0이면 피카츄가 발음할 수 있는 문자열인 것이다.
if len(word.strip()) == 0:
    print("YES")
else:
    print("NO")