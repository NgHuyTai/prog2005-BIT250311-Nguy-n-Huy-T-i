class Nguoi:
    def __init__(self, ten, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi không hợp lệ")  # cách 1
        self._ten = ten
        self._tuoi = tuoi

    # getter
    def get_ten(self):
        return self._ten

    # setter
    def set_tuoi(self, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi phải >= 0")  # cách 2
        self._tuoi = tuoi

    def __str__(self):
        return f"Tên: {self._ten}, Tuổi: {self._tuoi}"

    def chao(self):
        return f"Xin chào, tôi là {self._ten}"

    @classmethod
    def tao_mac_dinh(cls):
        return cls("Unknown", 0)

    @staticmethod
    def thong_tin():
        return "Đây là class Nguoi"

    def __eq__(self, other):
        return self._ten == other._ten and self._tuoi == other._tuoi


# Class kế thừa
class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, mssv):
        super().__init__(ten, tuoi)
        self.mssv = mssv

    def __str__(self):
        return super().__str__() + f", MSSV: {self.mssv}"


# Test
n1 = Nguoi("An", 20)
n2 = Nguoi.tao_mac_dinh()

sv = SinhVien("Bình", 21, "SV001")

print(n1)
print(n2)
print(sv)

print(n1.chao())
print(Nguoi.thong_tin())

print(n1 == n2)