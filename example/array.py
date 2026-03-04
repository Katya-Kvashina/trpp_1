arr = list()
n = int(input("Enter number of elements: "))

if n <= 0:
        print("Error: Number of elements must be positive!")
        exit()

print("Enter elements:")
i = 0
while i < n:
     if n > 15:
        print("Array size should be less than 15")
exit()

print("Enter elements:")
i = 0

while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1

print("Array:")
i = 0
while i < n:
    print(arr[i], end=" ")
    i += 1
print("")