import argparse
import sys

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first")
    parser.add_argument("--number2",help="second")
    parser.add_argument("--operation", help="operation")



    args = parser.parse_args()

    n1= int(args.number1)
    n2 = int(args.number2)
    op = args.operation
    result=None
    if op == 'add':
        result = n1+n2
    elif op == 'subtract':
        result = n1-n2
    elif op == 'multiply':
        result = n1*n2
    elif op == 'division':
        result = n1/n2
    else:
        print("unsupported opeartion")

    print("Result:", result)



