arr = []

# Nhập 5 chuỗi
for i in range(5):
    s = input(f"Nhập chuỗi {i+1}: ")
    arr.append(s)

n = len(arr)

print("\nBắt đầu sắp xếp:\n")

# Bubble Sort
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if len(arr[j]) < len(arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    print(f"Bước {i+1}: {arr}")

    if not swapped:
        break

print("\nKết quả cuối:", arr)