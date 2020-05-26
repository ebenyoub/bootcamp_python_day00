import sys

if len(sys.argv) < 3:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n    python operations.py 10 3\n")
elif sys.argv[1].isdigit() is False or sys.argv[2].isdigit() is False:
    print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n    python operations.py 10 3\n")
elif len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:\n    python operations.py 10 3\n")
else:
    print("Sum:\t\t", int(sys.argv[1]) + int(sys.argv[2]))
    print("Difference:\t", int(sys.argv[1]) - int(sys.argv[2]))
    print("Product:\t", int(sys.argv[1]) * int(sys.argv[2]))
    if int(sys.argv[2]) == 0:
        print("Quotient:\t ERROR (div by zero)")
    else:
        print("Quotent:\t", int(sys.argv[1]) / int(sys.argv[2]))
    if int(sys.argv[2]) == 0:
        print("Remainder:\t ERROR (div by zero)")
    else:
        print("Remainder:\t", int(sys.argv[1]) % int(sys.argv[2]))
    print("\n")
