def solution(new_id):
    answer = ''
    
    def big_to_small(new_id):
        return new_id.lower()
    
    def remove_letter(new_id):
        letter = ""
        for i in range(len(new_id)):
            word = new_id[i]
            if word.islower() or word.isdigit() or word == "-" or word == "_" or word == ".":
                letter += word
        return letter
    
    def replace_multiple_dots(new_id):
        result = ""
        last_char = ""
        for char in new_id:
            # 현재 문자가 마침표이고, 마지막 문자도 마침표인 경우 스킵
            if char == "." and last_char == ".":
                continue
            # 그렇지 않으면 결과 문자열에 추가
            result += char
            last_char = char
        return result
            
    def remove_end_point(new_id):
        if len(new_id) == 1 and new_id[0] == ".":
            return ""
        else:
            if new_id[0] == ".":
                new_id = new_id[1:]
            if new_id[-1] == ".":
                new_id = new_id[:-1]
            return new_id
    
    def empty_a(new_id): # len(new_id)가 0이 아닐 때까지
        if len(new_id) == 0:
            new_id += "a"
        return new_id
    
    def long_letter(new_id): # 끝에 마침표가 있으면 "remove_end_point"
        if len(new_id) >= 16:
            new_id = new_id[:15]
        return new_id
    
    def short_letter(new_id):
        letter = ""
        if len(new_id) <= 2:
            letter += new_id
            len_id = len(letter)
            while len_id < 3:
                letter += letter[-1]
                len_id += 1
        if letter == "":
            return new_id
        else:
            return letter
    
    new_id = big_to_small(new_id)
    new_id = remove_letter(new_id)
    new_id = replace_multiple_dots(new_id)
    new_id = remove_end_point(new_id)
    new_id = empty_a(new_id)
    new_id = long_letter(new_id)
    new_id = remove_end_point(new_id)
    new_id = short_letter(new_id)
    
    return new_id