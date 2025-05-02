def gauss_seidel(a, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    x = [0 for _ in range(n)] if x0 is None else x0.copy()
    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            sum1 = sum(a[i][j] * x_new[j] for j in range(i))
            sum2 = sum(a[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / a[i][i]
        # Check for convergence
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new
        x = x_new
    raise Exception("Gauss-Seidel method did not converge")
# Example usage
a = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]
b = [4, 7, 3]
initial_guess = [0, 0, 0]
solution = gauss_seidel(a, b, initial_guess)
print("Solution:", solution)