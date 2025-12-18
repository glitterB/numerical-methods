from num_methods.root_finding import bisection, newton_raphson

f = lambda x: x**3 - 5*x

root1 = bisection(f, 1.0, 2.0)
root2 = newton_raphson(f, lambda x: 3*x**2 - 5, 1.5)

print("Bisection root:", root1)
print("Newton-Raphson root:", root2)