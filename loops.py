import argparse


def factorial(num: int) -> int:
    """Return n! for non-negative integer num"""
    if not isinstance(num, int):
        raise TypeError("factorial() only accepts integers!")
    if num < 0:
        raise TypeError("factorial() undefined for negative numbers")
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Even numbers, Factorial, and squares demo."
    )
    p.add_argument(
        "-n", "--num", type=int, default=4, help="Number for factorial (default is 4)"
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # Even numbers 1-50
    print(f"Even numbers 1-50: {[num for num in range(1, 51) if num % 2 == 0]}")

    # Factorial
    print(f"Factorial of {args.num}: {factorial(args.num)}")

    # list comprehension
    print(f"Squares 1-10: {[num ** 2 for num in range(11)]}")


if __name__ == "__main__":
    main()
