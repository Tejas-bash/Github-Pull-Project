# Parameterized Python script for Jenkins

import sys

def main(name, age):
    print("Hello, {}! You are {} years old.".format(name, age))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <name> <age>")
        sys.exit(1)
    
    name = sys.argv[1]
    age = sys.argv[2]
    main(name, age)
