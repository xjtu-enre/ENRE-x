#-------------------------------------------------------------------------------
# Format units.
#   - Str: Strings and buffers
#   - Num: Numbers
#   - Obj: Other objects
#-------------------------------------------------------------------------------
import array

from Constraint import *


# s
# str (Unicode) -> const char *
class Str_s():
    def __str__(self):
        return 'str'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, str):
                if hasNullCodePoint(arg):
                    print('ValueError: The Python string must not contain embedded null code points.')
                    return False
                # TODO UnicodeError: Unicode objects are converted to C strings using 'utf-8' encoding. If conversion fails, ...
                return True
        return False


# s* (s_star)
# str | bytes-like object -> Py_buffer
# bytes-like object ::= immutable bytes-like object | mutable bytes-like object
# immutable bytes-like object ::= bytes | array.array | memoryview
# mutable bytes-like object ::= bytearray
class Str_s_s():
    def __str__(self):
        return 'str | bytes-like object'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, 
            (str, bytes, bytearray, array.array, memoryview)):
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# s# (s_pound)
# str | immutable bytes-like object -> (const char *, int | Py_ssize_t)
class Str_s_p():
    def __str__(self):
        return 'str | immutable bytes-like object'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, (str, bytes, array.array, memoryview)):
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# z
# str | None -> const char *
class Str_z():
    def __str__(self):
        return 'str | None'

    def check(self, arg):
        if arg == None:
            return True
        else:
            if isinstance(arg, str):
                if hasNullCodePoint(arg):
                    print('ValueError: The Python string must not contain embedded null code points.')
                    return False
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# z*
# str | bytes-like object | None -> Py_buffer
class Str_z_s():
    def __str__(self):
        return 'str | bytes-like object | None'

    def check(self, arg):
        if arg == None:
            return True
        else:
            if isinstance(arg, 
            (str, bytes, bytearray, array.array, memoryview)):
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# z#
# str | immutable bytes-like object | None -> (const char *, int | Py_ssize_t)
class Str_z_p():
    def __str__(self):
        return 'str | immutable bytes-like object | None'

    def check(self, arg):
        if arg == None:
            return True
        else:
            if isinstance(arg, (str, bytes, array.array, memoryview)):
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# y
# immutable bytes-like object -> const char *
class Str_y():
    def __str__(self):
        return 'immutable bytes-like object'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, (bytes, array.array, memoryview)):
                if hasNullCodePoint(arg):
                    print('ValueError: The Python string must not contain embedded null code points.')
                    return False
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# y*
# bytes-like object -> Py_buffer
class Str_y_s():
    def __str__(self):
        return 'bytes-like object'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, (bytes, bytearray, array.array, memoryview)):
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# y#
# immutable bytes-like object -> (const char *, int | Py_ssize_t)
class Str_y_p():
    def __str__(self):
        return 'immutable bytes-like object'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, (bytes, array.array, memoryview)):
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# S
# bytes -> PyBytesObject * | PyObject*
class Str_S():
    def __str__(self):
        return 'bytes'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, bytes):
                # without attempting any conversion
                return True
        return False


# Y
# bytearray -> PyByteArrayObject * | PyObject*
class Str_Y():
    def __str__(self):
        return 'bytearray'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, bytearray):
                # without attempting any conversion
                return True
        return False


# u
# str -> const Py_UNICODE *
class Str_u():
    def __str__(self):
        return 'str'

    def check(self, arg):
        print('Deprecated since version 3.3, will be removed in version 4.0.')
        if arg == None:
            return False
        else:
            if isinstance(arg, str):
                if hasNullCodePoint(arg):
                    print('ValueError: The Python string must not contain embedded null code points.')
                    return False
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# u#
# str -> (const Py_UNICODE *, int | Py_ssize_t)
class Str_u_p():
    def __str__(self):
        return 'str'

    def check(self, arg):
        print('Deprecated since version 3.3, will be removed in version 4.0.')
        if arg == None:
            return False
        else:
            if isinstance(arg, str):
                # This variant on `u` allows null code points.
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# Z
# str | None -> const Py_UNICODE *
class Str_Z():
    def __str__(self):
        return 'str | None'

    def check(self, arg):
        print('Deprecated since version 3.3, will be removed in version 4.0.')
        if arg == None:
            return True
        else:
            if isinstance(arg, str):
                if hasNullCodePoint(arg):
                    print('ValueError: The Python string must not contain embedded null code points.')
                    return False
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# Z#
# str | None -> (const Py_UNICODE *, int | Py_ssize_t)
class Str_Z_p():
    def __str__(self):
        return 'str | None'

    def check(self, arg):
        print('Deprecated since version 3.3, will be removed in version 4.0.')
        if arg == None:
            return True
        else:
            if isinstance(arg, str):
                # TODO UnicodeError: utf8 conversion
                return True
        return False


# U
# str -> Py_UNICODE * | PyObject*
# TODO report typo in reference manual
class Str_U():
    def __str__(self):
        return 'str'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, str):
                # without attempting any conversion
                return True
        return False


# w*
# mutable bytes-like object -> Py_buffer
class Str_w_s():
    def __str__(self):
        return 'mutable bytes-like object'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, bytearray):
                # TODO PyBuffer_Release() MUST be called when the buffer is no 
                # longer being used, otherwise reference leaks may occur.
                return True
        return False


# es
# str -> (const char *, char **)
class Str_es():
    def __str__(self):
        return 'str'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, str):
                if hasNullCodePoint(arg):
                    print('ValueError: The Python string must not contain embedded null code points.')
                    return False
                # TODO An exception is raised if the named encoding is not 
                # known to Python.
                # TODO Calling PyMem_Free() to free the buffer after use.
                return True
        return False


# et
# str | bytes | bytearray -> (const char *, char **)
class Str_et():
    def __str__(self):
        return 'str | bytes | bytearray'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, (str, bytes, bytearray)):
                if hasNullCodePoint(arg):
                    print('ValueError: The Python string must not contain embedded null code points.')
                    return False
                # TODO An exception is raised if the named encoding is not 
                # known to Python.
                # TODO Calling PyMem_Free() to free the buffer after use.
                return True
        return False


# es#
# str -> (const char *, char **, int * | Py_ssize_t *)
class Str_es_p():
    def __str__(self):
        return 'str'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, str):
                # TODO An exception is raised if the named encoding is not 
                # known to Python.
                # TODO Calling PyMem_Free() to free the buffer after use.
                # TODO If the buffer is not large enough, 
                # a ValueError will be set.
                return True
        return False


# et#
# str | bytes | bytearray -> (const char *, char **, int * | Py_ssize_t *)
class Str_et_p():
    def __str__(self):
        return 'str | bytes | bytearray'

    def check(self, arg):
        if arg == None:
            return False
        else:
            if isinstance(arg, (str, bytes, bytearray)):
                # TODO An exception is raised if the named encoding is not 
                # known to Python.
                # TODO Calling PyMem_Free() to free the buffer after use.
                # TODO If the buffer is not large enough, 
                # a ValueError will be set.
                return True
        return False


# b
# integer [0, 255] -> unsigned char (unsigned tiny int)
class Num_b():
    def __str__(self):
        return 'unsigned char'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 8, signed = True):
                return True
        return False


# B
# integer [0, 255] -> unsigned char
class Num_B():
    def __str__(self):
        return 'unsigned char'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 8, signed = True):
                return True
        return False


# h
# integer [-32768, 32767] -> short int
class Num_h():
    def __str__(self):
        return 'short'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 16, signed = False):
                return True
        return False


# H
# integer [0, 65535] -> unsigned short int
class Num_H():
    def __str__(self):
        return 'unsigned short'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 16, signed = True):
                return True
        return False


# i
# integer [-2147483648, 2147483647] -> int
class Num_i():
    def __str__(self):
        return 'int'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 32, signed = False):
                return True
        return False


# I
# integer [0, 4294967295] -> unsigned int
class Num_I():
    def __str__(self):
        return 'unsigned int'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 32, signed = True):
                return True
        return False


# l
# integer [-2147483648, 2147483647] -> long int
class Num_l():
    def __str__(self):
        return 'long'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 32, signed = False):
                return True
        return False


# k
# integer [0, 4294967295] -> unsigned long
class Num_k():
    def __str__(self):
        return 'unsigned long'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 32, signed = True):
                return True
        return False


# L
# integer [-9223372036854775808, 9223372036854775807] -> long long
class Num_L():
    def __str__(self):
        return 'long long'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 64, signed = False):
                return True
        return False


# K
# integer [0, 18446744073709551615] -> unsigned long long
class Num_K():
    def __str__(self):
        return 'unsigned long long'

    def check(self, arg):
        if isinstance(arg, int):
            if fitInteger(arg, width = 64, signed = True):
                return True
        return False


# n
# int -> Py_ssize_t
class Num_n():
    def __str__(self):
        return 'int'

    def check(self, arg):
        if isinstance(arg, int):
            if fitPy_ssize_t(arg):
                return True
        return False


# c
# bytes | bytearray -> char
class Num_c():
    def __str__(self):
        return 'bytes or bytearray of length 1'

    def check(self, arg):
        if isinstance(arg, (bytes, bytearray)):
            if len(arg) == 1:
                return True
        return False


# C
# str -> int
class Num_C():
    def __str__(self):
        return 'str of length 1'

    def check(self, arg):
        if isinstance(arg, str):
            if len(arg) == 1:
                return True
        return False


# f
# float -> float
class Num_f():
    def __str__(self):
        return 'float'

    def check(self, arg):
        if isinstance(arg, float):
            return True
        return False


# d
# float -> double
class Num_d():
    def __str__(self):
        return 'float'

    def check(self, arg):
        if isinstance(arg, float):
            return True
        return False


# D
# complex -> Py_complex
class Num_D():
    def __str__(self):
        return 'complex'

    def check(self, arg):
        if isinstance(arg, complex):
            return True
        return False


# O
# object -> PyObject *
class Obj_O():
    def __str__(self):
        return 'object'

    def check(self, arg):
        # The pointer stored is not NULL.
        return True


# O! (O_exclamation)
# object -> (typeobject, PyObject *)
class Obj_O_e():
    def __str__(self):
        return 'object'

    def check(self, arg):
        # TODO TypeError: If the Python object does not have the required type, ...
        return True


# O& (O_ampersand)
# object -> (converter, anything)
class Obj_O_a():
    def __str__(self):
        return 'object'

    def check(self, arg):
        # TODO status = converter(object, address);
        # 1 for a successful conversion and 0 if the conversion has failed
        return True


# p
# bool -> int
class Obj_p():
    def __str__(self):
        return 'bool-object'

    def check(self, arg):
        # valid Python value for truth value testing
        try:
            if arg.__getattribute__('__bool__'):
                return True
        except:
            pass
        try:
            if arg.__getattribute__('__len__'):
                return True
        except:
            pass
        return False


def list_to_tuple(l):
    lcopy = l.copy()
    for i in range(len(lcopy)):
        if type(lcopy[i]) == list:
            lcopy[i] = list_to_tuple(lcopy[i])
    return tuple(lcopy)

def list_to_string_tuple(l):
    lcopy = l.copy()
    for i in range(len(lcopy)):
        if type(lcopy[i]) == list:
            lcopy[i] = list_to_string_tuple(lcopy[i])
        else:
            lcopy[i] = str(lcopy[i])
    return tuple(lcopy)

def check_tuple_type(t, type_signature):
    valid = True
    for i in range(len(t)):
        if type(t[i]) == tuple:
            valid = check_tuple_type(t[i], type_signature[i])
        else:
            if not type_signature[i].check(t[i]):
                valid = False
    return valid

# (items)
# tuple -> (matching-items)
class Obj_t():
    def __init__(self, types):
        self.types = types
        self.tuple_types = list_to_tuple(types)

    def __str__(self):
        return str(list_to_string_tuple(self.types))

    def check(self, arg):
        if type(arg) == tuple:
            return check_tuple_type(arg, self.types)
        return False


if __name__ == '__main__':
    def test(Cls, arg):
        print('----------')
        u = Cls()
        print("Is {} valid for {}".format(arg, u))
        print(u.check(arg))

    test(Str_s, 'asd\0')
    test(Str_s_s, b'asd')
    test(Str_y, b'asd\0')
    test(Str_y, array.array('b', [65, 97, 0]))
    test(Str_y, memoryview(b'asd\0'))
    test(Str_u, 'asd\0')
    test(Str_et, bytearray('asd\0', 'utf8'))
    test(Num_B, -1)
    test(Num_h, 123)
    test(Num_H, -12345)
