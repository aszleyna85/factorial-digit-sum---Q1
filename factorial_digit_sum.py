def multiply(number, multiplier):
    carry = 0
    result = []

    for digit in number:
        product = digit * multiplier + carry
        result.append(product % 10)
        carry = product // 10

    while carry > 0:
        result.append(carry % 10)
        carry //= 10

    return result

def factorial_digit_sum(n):
    result = [1]

    for i in range(2, n + 1):
        result = multiply(result, i)

    return sum(result)

# Calculate and print the sum of digits of 100!
answer = factorial_digit_sum(100)
print("Sum of digits in 100! is:", answer)
