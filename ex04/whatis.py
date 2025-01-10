import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
    try:
        int(sys.argv[1])
        if int(sys.argv[1]) % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")

    
    