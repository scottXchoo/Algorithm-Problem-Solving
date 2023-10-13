import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

def word2bit(word):
  bit = 0
  for char in word:
    bit = bit | 1 << (ord(char) - ord('a'))
  return bit

bits = list(map(word2bit, words))
base_bit = word2bit('antic')

if K < 5:
  print(0)
else:
  alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
  ans = 0
  for comb in combinations(alphabet, K-5):
    know_bit = sum(comb) | base_bit
    cnt = 0
    for bit in bits:
      if bit & know_bit == bit:
        cnt += 1
    ans = max(ans, cnt)
  print(ans)