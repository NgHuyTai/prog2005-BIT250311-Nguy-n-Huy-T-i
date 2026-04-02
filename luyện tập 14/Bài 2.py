n = int(input("Nhập n: "))

print("\nHình 1:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print("\nHình 2:")
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nHình 3:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nHình 4:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

print("\nHình 5:")
for i in range(n, 0, -1):
    print(" "*(n-i), end="")
    for j in range(i):
        print("*", end=" ")
    print()

print("\nHình 6:")
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 7:")
for i in range(n):
    for j in range(n):
        if j == n-1 or i == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 8:")
for i in range(n):
    for j in range(n):
        if i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 9:")
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 10:")
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()