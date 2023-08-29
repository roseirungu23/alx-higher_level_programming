#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        return (None)
    finally:
        print("Inside result: {}".format(result) if 'result' in locals() else "Inside result: None")
        return (result)
