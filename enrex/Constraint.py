#-------------------------------------------------------------------------------
# Extra checks on certain types.
#-------------------------------------------------------------------------------
import array
import sys


# ValueError: The Python string must not contain embedded null code points.
def hasNullCodePoint(obj):
    if isinstance(obj, str):
        if '\0' in obj:
            return True
    elif isinstance(obj, (bytes, bytearray)):
        if b'\0' in obj:
            return True
    elif isinstance(obj, (array.array, memoryview)):
        if b'\0' in obj.tobytes():
            return True
    return False


# Integer overflow

# calculate (lower_bound, upper_bound) with given bit width and signed
def _bound(width, signed = False):
    if signed:
        upper_bound = 2 ** width - 1
        lower_bound = 0
    else:
        v = 2 ** (width - 1)
        upper_bound = v - 1
        lower_bound = -v
    return (lower_bound, upper_bound)

# char (tiny int): 1B
# short int: 2B
# int: 4B
# long int: 4B
# long long int: 8B
# TODO platform/compiler related: win/unix, 32/64, ...
def fitInteger(obj, width = 32, signed = False):
    if isinstance(obj, int):
        (lower_bound, upper_bound) = _bound(width = width, signed = signed)
        if obj >= lower_bound and obj <= upper_bound:
            return True
    return False


# Py_ssize_t
def fitPy_ssize_t(obj):
    if isinstance(obj, int):
        # sys.maxsize gives the maximum value a variable of 
        # type Py_ssize_t can take on diffierent platforms.
        upper_bound = sys.maxsize
        lower_bound = -upper_bound - 1
        if obj >= lower_bound and obj <= upper_bound:
            return True
    return False


if __name__ == "__main__":
    print(_bound(8, signed = True))
    print(_bound(16, signed = False))
    print(_bound(32, signed = True))
    print(_bound(64, signed = False))
    print(_bound(64, signed = True))
