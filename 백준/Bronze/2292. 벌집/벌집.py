n = int(input())

beeHouse = 1
c = 1

while n > beeHouse:
    beeHouse += 6*c
    c += 1
    
print(c)