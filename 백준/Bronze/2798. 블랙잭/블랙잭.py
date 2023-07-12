from itertools import combinations

card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))
arr = []

for cards in combinations(card_list, 3):
	if sum(cards) > target_num:
		continue
	else:
		arr.append(sum(cards))
print(max(arr))