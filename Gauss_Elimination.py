def gauss_elimination(a, b):
    n = len(b)
    for i in range(n):
        for j in range(i+1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
            b[j] -= factor * b[i]
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i+1, n))) / a[i][i]
    return x

# Example usage
a = [[1,1,1],
     [2,3,1],
     [1,2,3]]
b = [4,7,9]

solution = gauss_elimination(a, b)
print("Solution:", solution)