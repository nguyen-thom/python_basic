from sp6.oop.student import Student

st1 = Student(13, "Tuan")
st2 = Student(14, "Hoang")

dict_hs = {
    "12a1": st1,
    "12a2": st2
}

print("lop 12a1: ")
dict_hs.get("12a1").show()

print("so phan tu: " + str(len(dict_hs)))

