def f(x):
    return x**4-x-10
def df(x,h=1e-6):
    return (f(x + h)-f(x))/h
x = 2
for _ in range(10):
    x = x - f(x)/df(x)
print("Root:", round(x, 4))