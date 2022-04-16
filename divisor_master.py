def check_simple_num(n):
    """
    проверяет число на простоту
    :param n: натуральные числа в диапозоне от 1 до 1000
    :return: True - если число простое, False в противном случае
    """
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
    return result

def get_div_simple(n, printResult = True):
    """
    получает и выводит(опционально) список всех делителей числа
    :param n: натуральные числа в диапозоне от 1 до 1000
    :param printResult: признак вывводить список или нет.
    :return: возвращает список всех делителей числа
    """
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    if printResult:
        print(f'Делители числа {n}: {result}'.format(n, result))
    return result

def print_max_simple_dev(n):
    """
    выводит самый большой простой делитель числа
    :param n: натуральные числа в диапозоне от 1 до 1000
    :return: ничего не возвращает - только выводит
    """
    result = get_div_simple(n, False)
    if len(result) == 2: #всего два делителя: единица и само число
        max_div = result[-1]
    else:
        max_div = result[0]
        for num_div in result:
            if check_simple_num(num_div) & (max_div <= num_div) & (num_div != n):
                max_div = num_div
        if max_div == 1: max_div = n

    print('Максимальный делитель:', max_div)
