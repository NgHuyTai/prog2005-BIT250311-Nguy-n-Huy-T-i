n = int(input("Nhập n: "))

print("\nHình 1:")
for i in range(n):
    for j in range(n):
        print(1, end=" ")
    print()

print("\nHình 2:")
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()

print("\nHình 3:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 4:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 5:")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j <= i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 6:")
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHình 7:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("\nHình 8:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

print("\nHình 9:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()