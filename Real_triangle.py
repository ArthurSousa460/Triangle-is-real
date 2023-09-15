def verify_triangle(a, b, c):
    if (a + b) > c:
        if (a + c) > b:
            if (c + b) > a:
                return True
    return False


def verify_equilateral(a, b, c):
    if verify_triangle(a, b, c) == True:
        if a == b and a == c and c == b:
            return True
    return False
        

def verify_isosceles(a, b, c ):
    if verify_triangle(a, b, c) == True:
        if a == b and c != a:
            return True
        elif a == c and b != a:
            return True
        elif b == c and a != b:
            return True
    return False


def verify_escaleno(a, b, c):
    if verify_triangle(a, b, c) == True:
        if a != b and a != c and c != b:
            return True
    return False


print("-----------Triangle------------")
print("Digite o valores dos lados para saber se o triângulo pode ser um e seu tipo")
a = float(input("Lado A:"))
b = float(input("Lado B:"))
c = float(input("Lado C:"))
equilateral = verify_equilateral(a, b, c)
escaleno = verify_escaleno(a, b, c)
isoceles = verify_isosceles(a, b, c)
if equilateral == True:
    print('O trângulo digitado é equilátero')
elif escaleno == True:
    print('O trângulo digitado é escaleno')
elif isoceles == True:
    print('O trângulo digitado é isoceles')
else: 
    print('dados inválidos')

