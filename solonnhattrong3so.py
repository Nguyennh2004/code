a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))

#Cách 1

# max = a

# if (b > a) :
#     max == b
#     print("Số lớn nhất là: ",b)
# elif (c > a) :
#     max == c
#     print("Số lớn nhất là: ",c)
# else:
#     print("Số lớn nhất là:",a)

#Cách 2

if (a == b and a == c):
    print("Cả 3 số a, b, c bằng nhau và bằng {a}".format(a = a))
elif (a > b):
    if (a > c):
        print("Số lớn nhất là: ",a)
    else:
        print("Số lớn nhất là: ",c)
elif (b > a) :
    if(b > c):
        print("Số lớn nhất là: ",b)
    else:
        print("Số lớn nhất là: ",c)
else :
    print("Số lớn nhất là: ",c)

