import math
y=lambda x:x**4-x-10
#Starting points
x1=1
x2=2
y1=y(x1)
y2=y(x2)
for i in range(10):
    point=x1-(((x2-x1)*y1)/(y2-y1))
    x1=x2
    x2=point
print(f'Root of the equation is {point}')