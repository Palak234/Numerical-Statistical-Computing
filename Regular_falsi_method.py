import math
y=lambda x:(x*math.log10(x))-1.2
#Starting points
x1=2
x2=3
y1=y(x1)
y2=y(x2)
for i in range(5):
    point=x1-(((x2-x1)*y1)/(y2-y1))
    y_point=point*math.log10(point)-1.2
    if y_point>0:
        x2=point
        y2=y_point
    else:
        x1=point
        y1=y_point
print(f'Root of the equation is {point}')