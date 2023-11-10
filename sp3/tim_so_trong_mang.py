## Bài tập 1
## List - danh sach
array_x = [2, 4, 6, 2, 8, 4, 5, 2]
# tìm xem có bao nhiêu sô 2 trong mảng array_x
so_can_dem = 2
count = 0
for x in array_x:
    if (x == so_can_dem):
        count = count + 1

print(" so 2 xuat hien {0} lan ".format(count))


## Bài tập 2 về vòng lặp.
## Cho mảng a có 5 phần tử 1,5,7,9,2
## Tính tổng các phần tử trong mảng

array_y = [1,5,7,9,2]
total = 0
for y in array_y:
    total = total + y

print(total)

## Bai so 3
##Cho một mảng 10 phần tử 1,2,4,5,12,34,34,78,62,56
## Tìm phần tử lớn nhất trong mảng.


#Bai so 4
# cho mang a[1,3]
# cho mang b[4,3,3,1,1,4]
# yeu cau: in ra man hinh 1 xuat hien 2 lan, 3 xuat hien 2 lan
# 2
# 2
array_a = [1,3]
array_b = [4,3,3,1,1,4]
for a in array_a:
    count = 0
    for b in array_b:
        if(a == b):
            count = count + 1
    print("count:", count)


