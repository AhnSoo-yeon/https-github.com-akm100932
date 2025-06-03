import argparse


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a ** b


def main():
    parser = argparse.ArgumentParser(description="Simple command-line calculator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", type=float, help="First operand")
    add_parser.add_argument("b", type=float, help="Second operand")

    sub_parser = subparsers.add_parser("subtract", help="Subtract two numbers")
    sub_parser.add_argument("a", type=float, help="First operand")
    sub_parser.add_argument("b", type=float, help="Second operand")

    mul_parser = subparsers.add_parser("multiply", help="Multiply two numbers")
    mul_parser.add_argument("a", type=float, help="First operand")
    mul_parser.add_argument("b", type=float, help="Second operand")

    div_parser = subparsers.add_parser("divide", help="Divide two numbers")
    div_parser.add_argument("a", type=float, help="First operand")
    div_parser.add_argument("b", type=float, help="Second operand")

    pow_parser = subparsers.add_parser("power", help="Raise a to the power of b")
    pow_parser.add_argument("a", type=float, help="Base value")
    pow_parser.add_argument("b", type=float, help="Exponent value")

    args = parser.parse_args()

    if args.command == "add":
        result = add(args.a, args.b)
    elif args.command == "subtract":
        result = subtract(args.a, args.b)
    elif args.command == "multiply":
        result = multiply(args.a, args.b)
    elif args.command == "divide":
        result = divide(args.a, args.b)
    elif args.command == "power":
        result = power(args.a, args.b)
    else:
        parser.error("Unknown command")

    print(result)


if __name__ == "__main__":
    main()
