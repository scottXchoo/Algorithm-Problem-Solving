class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        word_counter = Counter(words)
        words_num, words_len = len(words), len(words[0])
        window_size = words_len * words_num
        s_size = len(s)
        if window_size > s_size:
            return []
        
        for i in range(words_len):
            windows = []
            for j in range(0, window_size, words_len):
                windows.append(s[i+j:i+j+words_len])
            window_counter = Counter(windows)
            if window_counter == word_counter:
                answer.append(i)

            for j in range(0, s_size, words_len):
                start, end = i+j, i+j+window_size
                del_word = s[start:start+words_len]
                window_counter[del_word] -= 1
                if window_counter[del_word] == 0:
                    del window_counter[del_word]
                append_word = s[end:end+words_len]
                window_counter[append_word] += 1
                if window_counter == word_counter:
                    answer.append(start + words_len)
            
        return answer