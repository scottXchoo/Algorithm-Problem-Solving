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
# a : 1 / n : 8192 / t : 524288 / i : 256 / c : 4
# 'antic' : a + n + t + i + c = 532741
base_bit = word2bit('antic')

if K < 5:
  print(0)
else:
  # [2, 8, 16, 32, 64, 128, 512, 1024, 2048, 4096, 16384, 32768, 65536, 131072, 262144, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432]
  alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]
  ans = 0
  for comb in combinations(alphabet, K-5):
    # base_bit도 a, n, t, i, c 문자의 비트들의 합이니까
    # comb(다른 문자 집합)의 합과 base_bit를 | 함으로써 know_bit 정의
    know_bit = sum(comb) | base_bit
    cnt = 0
    for bit in bits:
      if bit & know_bit == bit: # know_bit 안에 알아야하는 단어인 bit가 있는지 확인
        cnt += 1
    ans = max(ans, cnt)
  print(ans)
