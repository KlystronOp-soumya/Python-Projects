def is_perfect(n, x=1, sum=0):
    if x >= n:
        return sum == n
    else:
        if n % x == 0:
            sum += x
        return is_perfect(n, x + 1, sum)

# Take input from user
number = int(input("Enter a number to check if it's perfect: "))

# Use the function and print the result
if is_perfect(number):
    print(f"The number {number} is a perfect number.")
else:
    print(f"The number {number} is not a perfect number.")