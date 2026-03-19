def lay_ten_file(path):
    return path.split("\\")[-1]

def lay_ten_khong_duoi(path):
    ten_file = lay_ten_file(path)
    return ten_file.split(".")[0]

# Test
path = "d:\\music\\muabui.mp3"
print(lay_ten_file(path))       # muabui.mp3
print(lay_ten_khong_duoi(path)) # muabui