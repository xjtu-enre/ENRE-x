import ctypes as c
from ctypes import *


class algStruct(Structure):
    _fields_ = [
        ('isnull', c_bool),
        ('add', c_double),
        ('minus', c_double),
        ('multi', c_double),
        ('div', c_double)
    ]


my_dll = c.cdll.LoadLibrary(input())
my_dll.algStructest.argtypes = [c_double, c_double]
my_dll.algStructest.restype = POINTER(algStruct)
p = my_dll.algStructest(input(), input())
