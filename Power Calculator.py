base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (n): "))

result = 1

for _ in range(abs(exponent)):
    result *= base

if exponent < 0:
    result = 1 / result

print(base,"raised to the power of",exponent,"is",result)