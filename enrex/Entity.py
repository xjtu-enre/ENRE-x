class PyMethodDef:
    def __init__(self, method_name, imp_name, flag):
        self.method_name = method_name
        self.method_imp_name = imp_name
        self.method_flag = flag
        self.method_impl = None
        self.method_para_unused = True

    def __str__(self):
        return f"({self.method_name}, (PyCFunction){self.method_imp_name}, {self.method_flag})"


class PyMethodImpl:
    def __init__(self, impl_func_body, impl_func_args):
        self.impl_func_body = impl_func_body
        self.impl_func_args = impl_func_args


class Summary:
    def __init__(self):
        self.count_compilable = 0
        self.count_wrapper = 0
        self.count_wrapper_has_fmtstr = 0
        self.count_wrapper_marked_noarg = 0
        self.count_wrapper_no_use_arg_bug = 0

