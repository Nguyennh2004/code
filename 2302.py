

def cong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia (a,b):
    return a/b

phep_tinh = input("Nhập vào phép cần tính : ")
a = int(input("Nhập vào số a : "))
b = int(input("Nhập vào số b : "))

if phep_tinh == "+":
    print(cong(a,b))
if phep_tinh == "-":
    print(cong(a,b))
if phep_tinh == "*":
    print(cong(a,b))
if phep_tinh == "/":
    print(cong(a,b))

