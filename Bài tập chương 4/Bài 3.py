def kiem_tra_key(ds, key):
    if key in ds:
        return True
    else:
        return False

# Test
print(kiem_tra_key(sinh_vien, "An"))   # True
print(kiem_tra_key(sinh_vien, "Dũng")) # False