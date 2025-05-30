count = 1
total_odd = 0
total_even = 0

while count <= 100:
    if count % 2 == 1:
        total_odd += count
    else:
        total_even += count
    count += 1

print("1부터 100까지 홀수의 합은 {odd}, 짝수의 합은 {even}입니다.".format(odd=total_odd, even=total_even))

print('K\'im')
print("[{:15,}]".format(1234567890))

for i in range(1, 11, 2):
    print(i)
print(range(1, 11, 2))

#print(sorted(["aaa", "ccccc", "bb", "dddd"], key=len(), reverse=True))

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(arr[-2][1])
