import ctypes

dll = ctypes.cdll.LoadLibrary("./hellopy.dll")
cin = ctypes.c_char_p("My name is JJ".encode())
dll.hello(cin)
