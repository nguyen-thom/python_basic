"""

my_dict = {
    "Hello": "Xin Chao",
    "Book": "Sach",
    "Table": "Ban"
    "Student": "Hoc Sinh"
}
# viet mot ham tra_tu_dien(chu_tieng_anh). tra ve la chu tieng viet
# neu khong co thi la khong tim thay
"""

my_dict = {
    "Hello": "Xin Chao",
    "Book": "Sach",
    "Table": "Ban",
    "Student": "Hoc Sinh"
}

def tra_tu_dien(chu_tieng_anh):
    # lap trong tat cac key
    for key in my_dict:
        # neu ma key = chu tieng anh
        # return dic[key]
        #print(key.lower())
        if(key.lower() == chu_tieng_anh.lower()):
            return my_dict[key]
    #end for
    # return "Khong tim thay"
    return "KHONG TIM THAY"


ketqua_book = tra_tu_dien("Book") #Book
print(ketqua_book)
ketqua_book2 = tra_tu_dien("book")
print(ketqua_book2)


