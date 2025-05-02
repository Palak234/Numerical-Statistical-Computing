def jacobi(a, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    x = [0 for _ in range(n)] if x0 is None else x0.copy()
    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            sum_ = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / a[i][i]
        # Check for convergence
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new
        x = x_new
    raise Exception("Jacobi method did not converge")
# Example usage
a = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]
b = [4, 7, 3]
initial_guess = [0, 0, 0]
solution = jacobi(a, b, initial_guess)
print("Solution:", solution)