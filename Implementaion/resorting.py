s = []
sum = 0

data = list(input())
print(data)
for i in range(len(data)):
    if data[i].isdigit() == True:
        sum += int(data[i])
    else:
        s.append(data[i])

s.sort()
s = "".join(s)
print(s + str(sum))