def factorial(num: int) -> int:
    """Calculate the factorial of a number."""
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def binomial_coefficient(n: int,k: int) -> int:
    if k>0 and k<n:
        return factorial(n)/(factorial(k)*factorial(n-k))
    elif k == 0:
        return 1
    elif k<0:
        raise ValueError("k must be a non-negative integer.")
    else:
        raise ValueError("k must be less than n.")
