rate = 0
scoreSum = 0

rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    subject, score, grade = input().split()
    if grade == "P":
        continue
    rate += float(score) * rating[grade]
    scoreSum += float(score)
    
print(rate/scoreSum)