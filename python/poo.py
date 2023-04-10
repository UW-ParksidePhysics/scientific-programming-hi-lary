def operation(val):
    out = val**val
    return out


try:
    x = int(input("x="))
except ValueError:
    x=0