import math

# In các số lẻ từ 17 đến 111 (giảm dần)
print("Các số lẻ từ 17 đến 111 (giảm dần):")
for i in range(111, 16, -1):
    if i % 2 != 0:
        print(i, end=" ")

print("\n")

# In các số nguyên tố từ 17 đến 111
print("Các số nguyên tố từ 17 đến 111:")
for n in range(17, 112):
    if n > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print(n, end=" ")