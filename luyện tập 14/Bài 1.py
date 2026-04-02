# Nhập m và n
m = int(input("Nhập số dòng m: "))
n = int(input("Nhập số cột n: "))

# In hình chữ nhật
for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()  # xuống dòng sau mỗi hàng