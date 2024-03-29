import math

def solve_quadratic_equation(a, b, c):
  discriminant = b**2 - 4*a*с if
  discriminant > 0:
    x1 = (-b +
math.sqrt(discriminant)) / (2*a)
    x2 = (-b -
math.sqrt(discriminant)) / (2*a)
    return x1, X2
  elif discriminant == 0:
    x = -b/(2*a)  
    return x 
else:
    return None
def count_real_roots(a, b, c):
  equation1 =
solve_quadratic_equation(a, b, c)
  equation2 =
solve_quadratic_equation(b, a, c)
  equation3 =
solve_quadratic_equation(c, a, b)
  count = sum([1 for eq in
[equation1, equation2, equation3] if eq is not None]) 
  return count
a1, b1, c1 = 1, -5, 6
a2, b2, c2 = 2, -5, 2
a3, b3, c3 = 3, -4, 1
result = count_real_roots(a1, b1, c1)
print("Уравнение 1 имеет вещественные корни:", result)

result = count_real_roots(a2, b2, c2)
print("Уравнение 2 имеет вещественные корни:", result)

result = count_real_roots (a3, b3, 3)
print("Уравнение 3 имеет вещественные корни:", result)
