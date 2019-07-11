single_digits = range(10)
squares = []

for digit in single_digits:
  print(digit)
  squares.append(digit**2)
  
cubes = [digit**3 for digit in single_digits]

print(squares)
print(cubes)
