celsius = float(input("Temperature in C? "))

def c_to_f(c_temp):
    f_temp = (c_temp * 1.8) + 32
    return f_temp

print(c_to_f(celsius))