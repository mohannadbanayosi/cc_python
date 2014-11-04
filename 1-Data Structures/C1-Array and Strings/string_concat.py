from cStringIO import StringIO
from UserString import MutableString
from array import array

import sys, timeit

def method1():
    # 0.129138946533
    out_str = ''
    for num in xrange(loop_count):
        out_str += `num`
    return out_str

def method2():
    # 12.5030908585
    out_str = MutableString()
    for num in xrange(loop_count):
        out_str += `num`
    return out_str

def method3():
    # 0.325138092041
    char_array = array('c')
    for num in xrange(loop_count):
        char_array.fromstring(`num`)
    return char_array.tostring()

def method4():
    # 0.133127212524
    str_list = []
    for num in xrange(loop_count):
        str_list.append(`num`)
    out_str = ''.join(str_list)
    return out_str

def method5():
    # 0.361447811127
    file_str = StringIO()
    for num in xrange(loop_count):
        file_str.write(`num`)
    out_str = file_str.getvalue()
    return out_str

def method6():
    # 0.103055000305
    out_str = ''.join([`num` for num in xrange(loop_count)])
    return out_str

def method7():
    # 0.107057094574
    out_str = ''.join(`num` for num in xrange(loop_count))
    return out_str


loop_count = 80000

print sys.version

print 'method1=', timeit.timeit(method1, number=10)
print 'method2=', timeit.timeit(method2, number=10)
print 'method3=', timeit.timeit(method3, number=10)
print 'method4=', timeit.timeit(method4, number=10)
print 'method5=', timeit.timeit(method5, number=10)
print 'method6=', timeit.timeit(method6, number=10)
print 'method7=', timeit.timeit(method7, number=10)