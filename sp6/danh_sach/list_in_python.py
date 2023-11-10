import sp6.oop.student as Student
#Phan 1: khoi tao
#Phần 2: Xem các phần tử trong list
#Phần 3: Thêm phân tu vao
#Phần 4: xoa phan tu di
#Phân 5: sap xep cac phan tu

#khoi tao mot list
list_students = ["Jimmy", "Kane", "Tony"] #str
list_random_number = [1, 9, 3, 5, 6, 6] #int
list_mix_data_type = ["Jimmy", 20, 89.9, True] #int #double #boolen #str
#
list_empty =  []

#student1 = Student(123,"An","2012-12-21", "2333-998-9888")
#student2 = Student(124,"Binh","2012-09-21", "2333-998-9888")
#list_students = [student1, student2] # list objects

#Phần 2: Xem các phần tử trong list

# get so phan tu trong list #lenght
so_phan_tu = len(list_random_number)
print(so_phan_tu) # 6

# lap cac phan tu [1, 9, 3, 5, 6, 6]
for i in list_random_number:
    a = i**2
    print("phan tu: " + str(a))

# index
list_moi = [1, 9, 3, 5, 6, 7, 12, 23, "T", "H"]
          # 0, 1, 2, 3, 4, 5
print(list_moi[0]) #1
print(list_moi[5]) #7

# len(list_moi) = 6
# last item (cuoi cung) = 5
print(list_moi[len(list_moi)-1])

# Phan 3: Them phan tu vao list
list_a = []
#list_a.append(6))
#list_a.append(4)
print(list_a) # [6, 4]

for i in range(1,11):
    list_a.append(i*2)

print(list_a)

list_c = [1, 3, 5]

index = 1
list_c.insert(index,2) # [1,2,3,5]
print(list_c)
list_c.insert(3,4)
print(list_c)
# [1,2,3,5,6]
#list_c.insert(5,6)
list_c.append(6)
print(list_c)

#phan 4 xoa phan tu va xoa list
list_c.remove(6)
print(list_c)
list_danh_sach = ["T", "H", "K"]
list_danh_sach.remove("K")
print(list_danh_sach)
# lay ra va xoa luon
h = list_danh_sach.pop()
print(h) #H
print(list_danh_sach)
# clear
list_g = [4,6,78,9,3]
list_g.clear()
print(list_g)









#print("List Student co " + str(len(list_random_number)) + " phan tu")
#print("List Student co " + str(len(list_mix_data_type)) + " phan tu")

#Phan 2: lay gia tri trong list

#1. lay jimmy tu list student
student_jimmy = list_students[0] # 0 la vi tri bat dau
#print(student_jimmy)
student_kane = list_students[1]# 1 la vi tri tiep theo
#print(student_kane)
#2. lay vi tri cuoi cung
last_student = list_students[len(list_students)-1]
#print(last_student)

#lay 2 student trong list (0,1)
top_2_student = list_students[0:2]
#print(top_2_student)
#print(list_students)

#Phan 3: them phan tu vao trong list
# them vao cuoi list
list_students.append("Henry")
#print("List Student (sau khi them henry):  " + str(len(list_students)) + " phan tu")
#print(list_students)

#them vao 1 vi tri nao do. Vi tri thuong bat dau = 0

#Phan 4: remove phan tu


