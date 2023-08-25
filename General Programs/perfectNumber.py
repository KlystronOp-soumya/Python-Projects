def is_perfect(n):
    sum = 1  # start with 1 because it's a divisor of every number
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                sum = sum + i + n//i
            i += 1
    return sum == n and n!=1

# Take input from user
number = int(input("Enter a number to check if it's perfect: "))

# Use the function and print the result
if is_perfect(number):
    print(f"The number {number} is a perfect number.")
else:
    print(f"The number {number} is not a perfect number.")