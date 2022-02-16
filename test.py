input = [6,2,5,1,3]
count = 0
for num in range(len(input)-1):
  if input[num+1] > input[num]:
    count = count + input[num+1] - input[num]
    input[num+1] = input[num]

print(list)
print(count)
