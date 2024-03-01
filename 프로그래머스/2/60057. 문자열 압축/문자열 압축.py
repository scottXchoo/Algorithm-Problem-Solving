def solution(s):
    str_len = len(s)
    result = str_len

    for size in range(1, str_len // 2 + 1):
        words = []
        for i in range(0, str_len, size):
            words.append(s[i:i+size])

        stack = [[words[0], 1]]
        for word in words[1:]:
            if stack[-1][0] == word:
                tmp = stack.pop()
                stack.append([tmp[0], tmp[1] + 1])
            else:
                stack.append([word, 1])

        answer = ""
        for word, cnt in stack:
            if cnt > 1:
                answer += str(cnt)
            answer += word

        result = min(result, len(answer))

    return result