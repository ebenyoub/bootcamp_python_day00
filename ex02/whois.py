import sys

if len(sys.argv) != 2 or sys.argv[1].isdigit() is False:
    print("ERROR")
elif int(sys.argv[1]) == 0:
    print("I'm Zero.")
elif int(sys.argv[1]) % 2 == 0:
    print("I'm Odd.")
else:
    print("I'm Even.")
