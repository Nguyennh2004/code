import math
#input a,b
a = float(input("Nhap chieu rong la: "))
b = float(input("Nhap chieu dai la: "))

#process c,s
c = (a + b) * 2
s = a * b

#display
print("Chu vi hinh chu nhat co chieu rong la {a} va chieu dai la {b} la {c}".format(a = a,b = b,c = c))
print("Chu vi hinh chu nhat co chieu rong la {a} va chieu dai la {b} la {s}".format(a = a,b = b,s = s))

import turtle
turtle.Turtle()

#đổ màu hình
turtle.fillcolor("black")
turtle.color("red")
turtle.begin_fill()

#bắt đầu vẽ hcn
turtle.forward(b)
turtle.right(90)
turtle.forward(a)
turtle.right(90)
turtle.forward(b)
turtle.right(90)
turtle.forward(a)
turtle.right(90)
turtle.end_fill()

turtle.done()