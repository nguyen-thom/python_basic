# Person
class Person:

    # Constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        print(self.name, self.id)


emp = Person( 102,"Dat")
emp.show()


class GiamDoc(Person):
    def print(self):
        print("class GiamDoc duoc goi")

giam_doc_nhan_su = GiamDoc(103,"Tuan") # Dang dung ham khoi tao cua lop cha
giam_doc_nhan_su.show() # Dang goi toi lop cha
giam_doc_nhan_su.print()
