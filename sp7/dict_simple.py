"""
hoc ve dictionary
["1","3","."]

A -> 1
B -> 2
C -> 3

12 -> {"Nam","18","12A1"}
13 -> {"Binh","18","12A1"}
"""

list_ky_tu = ["A", "C", "A", "B", "G"]
# liet ke so phan tu trong list_ky_tu
# "A" -> 2
# "B" -> 1
# "C" -> 1
# "G" -> 1
dict_ky_tu = dict()
dict_ky_tu["A"] = 0
dict_ky_tu["B"] = 0
dict_ky_tu["C"] = 0
for i in list_ky_tu:
    danh_sach_key = dict_ky_tu.keys()  # [A,B,C]
    for key in danh_sach_key:
        if(key == i):
            dict_ky_tu[key] = dict_ky_tu[key] + 1
    # ket thuc for 1
#ket thuc for 2
print(dict_ky_tu)

# danh sach diem 3 mon (toan, ly, hoa) cua hoc sinh lop 12a1
dict_hoc_sinh_12a1 = {
    "Nam": [7,8,8],
    "Binh": [5,7,8],
    "Hoai": [1,2,4]
}

print(dict_ky_tu)
#diem trung binh = diem 3 mon cong lai roi chia cho 3
#tim xem nguoi nao co diem trung binh cao nhat
# dtr = tong tat ca cac phan tu / so phan tu
def tinh_diem_trung_binh(list_):
    so_phan_tu_trong_list = len(list_)  # lenght
    tong = 0
    for i in list_:
        tong = tong + i

    return tong / so_phan_tu_trong_list


hoc_sinh_dtr=dict()
ds_hs_key = dict_hoc_sinh_12a1.keys();
print(ds_hs_key)
for ten_hs in dict_hoc_sinh_12a1:
    dtr_list = dict_hoc_sinh_12a1[ten_hs]
    hoc_sinh_dtr[ten_hs] = tinh_diem_trung_binh(dtr_list)

print(hoc_sinh_dtr)

dict1 = dict(name = "John", age = 36, country = "Norway")
dict2 = dict(a = "3", b = "6", c = "9")

# key number
dict3 = {
    12: "A",
    13: "B"
}
print(dict3)


thisdict = {
  "brand": "Ford", # value (String,Number,List, Object)
  "model": "Mustang",
  "year": 1964,
   12345: "AGEFC"
}


print(thisdict)








