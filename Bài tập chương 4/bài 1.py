def thong_ke(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat

# Test
t = (1, 5, 3, 9, 2)
kq = thong_ke(t)
print("Tổng:", kq[0])
print("Max:", kq[1])
print("Min:", kq[2])