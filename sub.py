var = input("Type: ")

var_check = var.isdigit()

if var_check is True:
    var = int(var)
    result = var + 1
    print(result)
else:
    print(f"This is a {var}")
