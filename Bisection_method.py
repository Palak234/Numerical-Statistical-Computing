y=lambda x:(x**3)-2*x-5
#Starting points
x1=2
x2=3
for i in range(21):
    Mid_point=(x1+x2)/2
    y_mid=y(Mid_point)
    if y_mid>0:
        x2=Mid_point
    else:
        x1=Mid_point
print(f'Root of the equation is {Mid_point}')