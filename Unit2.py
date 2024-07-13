def addtogether(a, b):
    try:
        a = int(input("Please enter first number:"))
        b = int(input("Please enter second number"))
        add = a + b
    except ValueError:
          raise ValueError("Both inputs must be convertable to integers")
    print(add)
addtogether(None, None)
