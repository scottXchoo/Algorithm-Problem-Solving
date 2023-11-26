arr = [int(input()) for i in range(3)]

if sum(arr) == 180:
  if arr.count(60) == 3:
    print("Equilateral")
  elif len(set(arr)) == 2:
    print("Isosceles")
  elif len(set(arr)) == 3:
    print("Scalene")
else:
  print("Error")