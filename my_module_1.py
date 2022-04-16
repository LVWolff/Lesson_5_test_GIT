def fun_max(a,b):
    if a>=b: return a
    else: return b

fun_min = lambda a,b: a if a<=b else b

if __name__ == '__main__':
    x = fun_min(2,3)
    y = fun_max(3,8)
    print(x, y)

