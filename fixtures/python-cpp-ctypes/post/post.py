import ctypes as c

dll = c.cdll.LoadLibrary(input())
cin = input()
while cin != "exit":
    dll.post(c.c_char_p(cin.encode()))
    cin = input()
