def bai2():
    s = input("Nhập chuỗi: ")
    char = input("Nhập ký tự: ")
    print("Số lần xuất hiện:", s.count(char))


def bai3():
    def giai_thua(n):
        if n == 0 or n == 1:
            return 1
        return n * giai_thua(n - 1)

    n = int(input("Nhập số: "))
    print("Giai thừa:", giai_thua(n))


def bai6():
    s = input("Nhập chuỗi: ")
    dao = ""
    for i in range(len(s)-1, -1, -1):
        dao += s[i]
    print("Chuỗi đảo:", dao)


def bai7():
    while True:
        pw = input("Nhập mật khẩu: ")
        if pw == "python123":
            print("Đúng mật khẩu!")
            break
        else:
            print("Sai, nhập lại!")


def bai10():
    arr = []
    for i in range(5):
        arr.append(input(f"Nhập chuỗi {i+1}: "))

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Bước {i+1}: {arr}")


# ===== MENU =====
while True:
    print("\n===== MENU =====")
    print("1. Bài 2 - Đếm ký tự")
    print("2. Bài 3 - Giai thừa")
    print("3. Bài 6 - Đảo chuỗi")
    print("4. Bài 7 - Mật khẩu")
    print("5. Bài 10 - Sắp xếp chuỗi")
    print("0. Thoát")

    choice = input("Chọn bài: ")

    if choice == "1":
        bai2()
    elif choice == "2":
        bai3()
    elif choice == "3":
        bai6()
    elif choice == "4":
        bai7()
    elif choice == "5":
        bai10()
    elif choice == "0":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ!")