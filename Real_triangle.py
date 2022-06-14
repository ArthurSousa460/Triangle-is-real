def is_triangle(a, b, c):
    if a > b + c:
        print('No')
    elif b > a + c:
        print('No')
    elif c > b + a:
        print('No')
    else:
        print('Yes')


def input_triangle():
    print('-' * 20, end=' ')
    print('Real triangle', end=' ')
    print('-' * 20)
    a = int(input('Enter the size of side a:'))
    b = int(input('Enter the size of side b:'))
    c = int(input('Enter the size of side c:'))
    is_triangle(a, b, c)


input_triangle()
