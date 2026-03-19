arr = []

for i in range(5):
    s = input(f"Nhập chuỗi {i+1}: ")
    arr.append(s)

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if len(arr[j]) < len(arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(f"Bước {i+1}: {arr}")