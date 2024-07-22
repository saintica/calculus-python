def int_sqrt(x):
    """Compute the integer square root of a number using binary search."""
    if x < 0:
        raise ValueError('Square root is not defined for negative numbers')
    if x == 0:
        return 0
    a, b = divmod(x.bit_length(), 2)
    n = 2**(a+b)
    while True:
        y = (n + x // n) // 2
        if y >= n:
            return n
        n = y

def pi_bbp(digits):
    """Calculate pi to the specified number of digits using BBP formula."""
    # Multiply by a large constant to handle integer arithmetic
    one = 10**digits
    pi = 0
    k = 0

    while True:
        # Using integer arithmetic to avoid precision issues
        term = (one // (16 ** k)) * (
            4 * one // (8 * k + 1) - 2 * one // (8 * k + 4) - 
            one // (8 * k + 5) - one // (8 * k + 6)
        )
        if term == 0:
            break
        pi += term
        k += 1

    return pi // one

# Input the number of digits
n = int(input("Enter the number of digits of pi to calculate: "))
# Calculate pi to n digits
pi = pi_bbp(n+1)

# Convert to string and format the output
pi_str = str(pi)
pi_str = pi_str[0] + '.' + pi_str[1:-1]

# Reference pi
pi_ = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
if pi_[:n+2] == pi_str:
    print(f"Pi to {n} digits:\n {pi_str}")
else:
    print(f"The result is wrong\n")
