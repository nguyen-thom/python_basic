class DiemSo:
    def __init__(self, mon_hoc, diem):
        self.mon_hoc = mon_hoc
        self.diem = diem

    def show(self):
        print("Mon:" + self.mon_hoc + " Diem: " + str(self.diem))

class Student(object):
    
    def __init__(self, name, age, class_id):
        self.mon_van = None
        self.mon_toan = None
        self.name = name
        self.age = age
        self.class_id = class_id
        
    def setDiemMonToan(self, mon_toan):
        self.mon_toan = mon_toan
    
    def setDiemMonVan(self, mon_van):
        self.mon_van = mon_van
    
    def show(self):
        print("Hoc Sinh:  " + self.name + " age: " + str(self.age) + " Class: " + self.class_id)
        print("Hoc Sinh Kha: " + self.kiemTraHocSinhKha())

    def kiemTraHocSinhKha(self):
        diem_trung_binh = (mon_van.diem + mon_toan.diem)/2
        if(diem_trung_binh > 7):
            return "True"
        else:
            return "False"



mon_van = DiemSo("van_hoc",9)
mon_toan = DiemSo("hinh hoc", 8)

An = Student("An", 18, "12A2")
An.setDiemMonVan(mon_van)
An.setDiemMonToan(mon_toan)
An.show()


mon_van = DiemSo("van_hoc",6)
mon_toan = DiemSo("hinh hoc", 5)
Tuan = Student("Tuan", 18, "12A2")
Tuan.setDiemMonVan(mon_van)
Tuan.setDiemMonToan(mon_toan)
Tuan.show()


        

