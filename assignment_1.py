import math
 
x0 = 1.5
tol = 0.000001

iter = 0
diff = x0
x = x0

print(f"{iter} : {x}")

while diff >= tol:
    iter += 1
    y = x
    x = (x / 2) + (1 / x)
    print(f"{iter} : {x}")
    diff = abs(x - y)

print(f"\nConvergence after {iter} iterations")






def bisection_method(f, a, b, tol=0.000001, max_iter=50):
    
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    left = a
    right = b
    i = 0

    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2
        
        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p
    
    print(f"Success after {i} iterations")
    return p



def f(x):
    return x**3 + 4*x**2 - 10

a = 1.0
b = 2.0
tol = 0.001  
root = bisection_method(f, a, b, tol=tol)

if root is not None:
    print(f"The approximate root is: {root}")
    
    






def fixed_point_iteration_1(p0, tol=0.000001, N0=50):
  
    if not isinstance(p0, (int, float)):
        raise ValueError("Invalid input value p0")
    if tol <= 0:
        raise ValueError("Invalid tolerance value")
    if N0 <= 0:
        raise ValueError("Invalid maximum number of iterations")

    output_values = []
    i = 1
    while i <= N0:
        try:
            p = p0 - p0**3 - 4 * p0**2 + 10
        except OverflowError:
            print("\nResult diverges")
            print(f"Failure after {i} iterations\n")
            return output_values
        
        output_values.append(p)
        
        if math.isnan(p) or math.isinf(p):
            print("\nResult diverges")
            print(f"Failure after {i} iterations\n")
            return output_values
        
        if abs(p - p0) < tol:
            print("\nSuccess")
            print(f"Success after {i} iterations\n")
            return output_values
        
        p0 = p
        i += 1
    
    print("\nResult diverges")
    print(f"Failure after {i} iterations\n")
    return output_values

# Running the function
i_p0 = 1.5
print("Output for (a):")
output_values_1 = fixed_point_iteration_1(i_p0)
print("Output values:", output_values_1)








def newtons_method(f, f_prime, initial_approximation, tolerance=0.000001, max_iterations=50):
    
    p_prev = initial_approximation
    i = 1

    while i <= max_iterations:
        if f_prime(p_prev) != 0:
            p_next = p_prev - f(p_prev) / f_prime(p_prev)
            
            if abs(p_next - p_prev) < tolerance:
                print(f"Success after {i} iterations")
                return p_next
            
            i += 1
            p_prev = p_next
        else:
            print("Unsuccessful: Derivative is zero")
            return None
    
    print("Unsuccessful: Maximum iterations performed")
    return None



def f(x):
    return math.cos(x) - x

def f_prime(x):
    return -math.sin(x) - 1

initial_approximation = 0.5  # Initial guess within the interval [0, pi/2]
root = newtons_method(f, f_prime, initial_approximation)

if root is not None:
    print(f"The approximate root is: {root}")
