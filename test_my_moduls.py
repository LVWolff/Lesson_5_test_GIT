# fib_num = lambda n: fib_num(n-1) + fib_num(n-2) if n>2 else 1
#
# def test_1_fib_num():
#     assert fib_num(6) == 8
#
# def test_2_fib_num():
#     assert fib_num(5) == 8
#
# # f_{2n} = (f_{n+1})^2 - (f_{n-1})^2
#
# def test_3_fib_num():
#     n = 10
#     assert fib_num(n*2) == fib_num(n+1)**2 - fib_num(n-1)**2

from divisor_master import check_simple_num as is_Simple
import my_module_1
from my_module_2 import fun_upString as upString


def test_1_divisor_master_checkSimpleNum():
    assert is_Simple(4) == False


def test_2_divisor_master_checkSimpleNum():
    assert is_Simple(101) == True


def test_3_my_module_1_fun_max():
    assert my_module_1.fun_max(3, 10) == 10


def test_4_my_module_1_fun_min():
    assert my_module_1.fun_min(3, 10) == 3


def test_5_my_module_2_upString():
    assert upString('test') == 'TEST'
