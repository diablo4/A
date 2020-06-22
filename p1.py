sum = 0
avg = 0
count = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum = sum + i
        count = count + 1

avg = sum / count

print(sum)
print(avg)