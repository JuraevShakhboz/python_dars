class TIME():
    def __init__(self, hour, minut, secund):
        self.hour = hour
        self.minut = minut
        self.secund = secund
        self.sum()

    def sum(self):
        if self.hour < 24 and self.minut < 60 and self.secund < 60:
            self.h = 24 - self.hour
            self.m = 60 - self.minut
            self.s = 60 - self.secund
        else:
            pass

        print(f"24 gacha: {self.h}:{self.m}:{self.s} qoldi!")

ob1 = TIME(int(input("Soatni kiriting: ")), int(input("Minutni kiriting: ")), int(input("Sekundni kiriting: ")))