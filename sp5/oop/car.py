class Xe:

    # ham khoi tao
    def __init__(self, bien_so, mau_sac="TIM"):
        self.bien_so = bien_so
        self.mau_sac = mau_sac

    def show(self):
        print("Car: " + self.bien_so + " Mau " + self.mau_sac)


class XeOto(Xe):

    # bien so , mau sac  thua ke tu XE
    # so cho la thuoc tinh (attr) moi cua XE OTO
    def __init__(self, bien_so, mau_sac, so_cho):
        super().__init__(bien_so, mau_sac)
        self.so_cho = so_cho

    def show(self):
        print("Xe O to: " + self.bien_so + " So Cho :" + str(self.so_cho))

class Animal:
    # ten
    def __init__(self, name):
        self.name = name

    # ham noi - ABC
    def noi(self):
        print("ABC")


# class Dog << Animal
class Dog(Animal):
    # ham noi - go go
    def noi(self):
        print("Go Go")


# class Cat << Animal
class Cat(Animal):
    # ham noi - meo meo
    def noi(self):
        print("Meo Meo")


dog1 = Dog("ABC")
dog1.noi()

cat1 = Cat("Muop")
cat1.noi()




xe_oto = XeOto("A11","TIM", 4)
xe_oto.show()
print(xe_oto.bien_so)



# khoi tao ra mot cai xe
car1 = Xe("A78-98")
# truy cap cac thuoc tinh cua cái xe số 1.
# print(car1.so_banh_xe)
# print(car1.so_cua_xe)
#car1.show()

car2 = Xe("A39-90", "DO")
# car2.show()
# for i in range(0,100):
#     xe = Car("A38-" + str(i), "XANH" )
#     xe.show()
