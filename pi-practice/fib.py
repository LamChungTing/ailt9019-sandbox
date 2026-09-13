"""Print the first five Fibonacci numbers."""

def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    fibs = [0, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:n]

if __name__ == "__main__":
    numbers = fibonacci(5)
    print(numbers)
