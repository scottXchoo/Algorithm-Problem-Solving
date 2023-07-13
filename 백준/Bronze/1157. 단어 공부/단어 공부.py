words = input().upper()
unique_words = list(set(words))

cnt_list = []
for x in unique_words:
	cnt = words.count(x)
	cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
	print("?")
else:
	max_index = cnt_list.index(max(cnt_list))
	print(unique_words[max_index])