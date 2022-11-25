import ctypes

dll = ctypes.cdll.LoadLibrary(input())
dll.hello()
