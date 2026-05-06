n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter the elements separated by space: ").split()))

k = int(input("Enter value of K: "))

possible = True

for i in range(n):
    if (arr[i] - arr[0]) % k != 0:
        possible = False
        break

if not possible:
    print("Output:", -1)

else:
    arr.sort()

    median = arr[n // 2]

    operations = 0

    for i in range(n):
        diff = abs(arr[i] - median)
        operations += diff // k

    print("Output:", operations)