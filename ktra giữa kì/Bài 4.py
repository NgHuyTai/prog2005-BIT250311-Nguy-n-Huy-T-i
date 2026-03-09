n = int(input("Nhập số phần tử của mảng: "))

a = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    a.append(x)

print("Mảng ban đầu:", a)

# Sắp xếp chọn giảm dần
for i in range(n - 1):
    max_index = i

    for j in range(i + 1, n):
        if a[j] > a[max_index]:
            max_index = j

    # đổi chỗ
    a[i], a[max_index] = a[max_index], a[i]

    print(f"Sau bước {i + 1}:", a)