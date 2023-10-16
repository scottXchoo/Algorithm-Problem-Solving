import sys
input = sys.stdin.readline

X = int(input())
bars = [64]

while sum(bars) != X:
  bars.sort()
  temp = bars[0] / 2
  bars.pop(0)
  bars.append(int(temp))
  if sum(bars) < X:
    bars.append(int(temp))

print(len(bars))