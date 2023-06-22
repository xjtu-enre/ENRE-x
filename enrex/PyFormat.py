#-------------------------------------------------------------------------------
# Format string syntax parser.
# 
# In these Python/C APIs for argument parsing between Python and C/C++,
# format strings are used to tell the foreign function about the expected 
# arguments.
#
# A format string consists of zero or more format units. 
# A format unit describes one Python object; 
# it is usually a single character or a parenthesized sequence of format units.
#-------------------------------------------------------------------------------
import PTypes
import PyFormatUnit


def parse(fmtstr):
    type_signature = []
    is_optional = False
    optional_args = []

    def add_type(type_instance):
        if is_optional:
            optional_args.append(type_instance)
        else:
            type_signature.append(type_instance)

    stack = []

    def stack_to_str(stack):
        s = ''
        for c in stack:
            s += c
        return s

    def clear_stack(stack):
        while stack:
            stack.pop()

    def read_stack():
        if stack_to_str(stack) == 's':
            add_type(PyFormatUnit.Str_s())
            clear_stack(stack)
        elif stack_to_str(stack) == 's*':
            add_type(PyFormatUnit.Str_s_s())
            clear_stack(stack)
        elif stack_to_str(stack) == 's#':
            add_type(PyFormatUnit.Str_s_p())
            clear_stack(stack)
        elif stack_to_str(stack) == 'z':
            add_type(PyFormatUnit.Str_z())
            clear_stack(stack)
        elif stack_to_str(stack) == 'z*':
            add_type(PyFormatUnit.Str_z_s())
            clear_stack(stack)
        elif stack_to_str(stack) == 'z#':
            add_type(PyFormatUnit.Str_z_p())
            clear_stack(stack)
        elif stack_to_str(stack) == 'y':
            add_type(PyFormatUnit.Str_y())
            clear_stack(stack)
        elif stack_to_str(stack) == 'y*':
            add_type(PyFormatUnit.Str_y_s())
            clear_stack(stack)
        elif stack_to_str(stack) == 'y#':
            add_type(PyFormatUnit.Str_y_p())
            clear_stack(stack)
        elif stack_to_str(stack) == 'u':
            add_type(PyFormatUnit.Str_u())
            clear_stack(stack)
        elif stack_to_str(stack) == 'u#':
            add_type(PyFormatUnit.Str_u_p())
            clear_stack(stack)
        elif stack_to_str(stack) == 'Z':
            add_type(PyFormatUnit.Str_Z())
            clear_stack(stack)
        elif stack_to_str(stack) == 'Z#':
            add_type(PyFormatUnit.Str_Z_p())
            clear_stack(stack)
        elif stack_to_str(stack) == 'w*':
            add_type(PyFormatUnit.Str_w_s())
            clear_stack(stack)
        elif stack_to_str(stack) == 'es':
            add_type(PyFormatUnit.Str_es())
            clear_stack(stack)
        elif stack_to_str(stack) == 'et':
            add_type(PyFormatUnit.Str_et())
            clear_stack(stack)
        elif stack_to_str(stack) == 'es#':
            add_type(PyFormatUnit.Str_es_p())
            clear_stack(stack)
        elif stack_to_str(stack) == 'et#':
            add_type(PyFormatUnit.Str_et_p())
            clear_stack(stack)
        elif stack_to_str(stack) == 'O!':
            add_type(PyFormatUnit.Obj_O_e())
            clear_stack(stack)
        elif stack_to_str(stack) == 'O&':
            add_type(PyFormatUnit.Obj_O_a())
            clear_stack(stack)

    tuple_stack = []
    tuple_depth = 0
    tuple_type = []

    def tuple_pointer(tuple_depth):
        p = tuple_type[-1]
        tuple_depth -= 1
        while tuple_depth:
            p = p[-1]
            tuple_depth -= 1
        return p

    for c in fmtstr:
        # characters
        if c == ':' or c == ';':
            read_stack()
            break
        elif c == '|':
            read_stack()
            is_optional = True
        elif c == '$':
            read_stack()
            # Currently (CPython 3.3-3.8), 
            # all keyword-only arguments must also be optional arguments, 
            # so | must always be specified before $ in the format string.
            continue
        else:
            # nested tuple object
            if tuple_depth:
                if c == '(':
                    if tuple_stack:
                        if tuple_depth == 1:
                            for typ in parse(stack_to_str(tuple_stack))[:-1]:
                                tuple_type.append(typ)
                            tuple_type.append([])
                        else:
                            for typ in parse(stack_to_str(tuple_stack))[:-1]:
                                tuple_type[-1].append(typ)
                            tuple_type[-1].append([])
                        clear_stack(tuple_stack)
                    else:
                        tuple_pointer(tuple_depth - 1).append([])
                    tuple_depth += 1
                elif c == ')':
                    tuple_depth -= 1
                    if tuple_depth == 0:
                        for typ in parse(stack_to_str(tuple_stack))[:-1]:
                            tuple_type.append(typ)
                        add_type(PyFormatUnit.Obj_t(tuple_type))
                    else:
                        for typ in parse(stack_to_str(tuple_stack))[:-1]:
                            tuple_pointer(tuple_depth).append(typ)
                    clear_stack(tuple_stack)
                else:
                    tuple_stack.append(c)
            else:
                # strings and buffers
                if c == 's':
                    read_stack()
                    stack.append(c)
                elif c == '*' or c == '#':
                    stack.append(c)
                elif c == 'z':
                    read_stack()
                    stack.append(c)
                elif c == 'y':
                    read_stack()
                    stack.append(c)
                elif c == 'S':
                    read_stack()
                    add_type(PyFormatUnit.Str_S())
                elif c == 'Y':
                    read_stack()
                    add_type(PyFormatUnit.Str_Y())
                elif c == 'u':
                    read_stack()
                    stack.append(c)
                elif c == 'Z':
                    read_stack()
                    stack.append(c)
                elif c == 'U':
                    read_stack()
                    add_type(PyFormatUnit.Str_U())
                elif c == 'w':
                    read_stack()
                    stack.append(c)
                elif c == 'e':
                    read_stack()
                    stack.append(c)
                elif c == 't':
                    read_stack()
                    stack.append(c)
                # numbers
                elif c == 'b':
                    read_stack()
                    add_type(PyFormatUnit.Num_b())
                elif c == 'B':
                    read_stack()
                    add_type(PyFormatUnit.Num_B())
                elif c == 'h':
                    read_stack()
                    add_type(PyFormatUnit.Num_h())
                elif c == 'H':
                    read_stack()
                    add_type(PyFormatUnit.Num_H())
                elif c == 'i':
                    read_stack()
                    add_type(PyFormatUnit.Num_i())
                elif c == 'I':
                    read_stack()
                    add_type(PyFormatUnit.Num_I())
                elif c == 'l':
                    read_stack()
                    add_type(PyFormatUnit.Num_l())
                elif c == 'k':
                    read_stack()
                    add_type(PyFormatUnit.Num_k())
                elif c == 'L':
                    read_stack()
                    add_type(PyFormatUnit.Num_L())
                elif c == 'K':
                    read_stack()
                    add_type(PyFormatUnit.Num_K())
                elif c == 'n':
                    read_stack()
                    add_type(PyFormatUnit.Num_n())
                elif c == 'c':
                    read_stack()
                    add_type(PyFormatUnit.Num_c())
                elif c == 'C':
                    read_stack()
                    add_type(PyFormatUnit.Num_C())
                elif c == 'f':
                    read_stack()
                    add_type(PyFormatUnit.Num_f())
                elif c == 'd':
                    read_stack()
                    add_type(PyFormatUnit.Num_d())
                elif c == 'D':
                    read_stack()
                    add_type(PyFormatUnit.Num_D())
                # objects
                elif c == 'O':
                    read_stack()
                    add_type(PyFormatUnit.Obj_O())
                elif c == '!' or c == '&':
                    stack.append(c)
                elif c == 'p':
                    read_stack()
                    add_type(PyFormatUnit.Obj_p())
                elif c == '(':
                    read_stack()
                    tuple_depth += 1
    
    read_stack()
    if optional_args:
        type_signature.append(optional_args)
    return type_signature


def check(args, type_signature):
    signature = type_signature.copy()
    optional = signature.pop()

    if len(args) > len(signature) + len(optional) or len(args) < len(signature):
        print("[WARNING] Wrong arguments number.")
    else:
        for i in range(len(args)):
            if i <= len(signature) - 1:
                if not signature[i].check(args[i]):
                    print("[WARNING] The {}-th argument should be {}.".format(i, signature[i]))
            else:
                if not optional[i - len(signature)].check(args[i]):
                    print("[WARNING] The {}-th argument should be {}.".format(i, optional[i - len(signature)]))


def print_signature(types, is_para):
    if is_para:
        temp_str = "Parameter: { "
    else:
        temp_str = "Return: { "
    res = set()

    for typ in types:
        if not isinstance(typ, list):
            res.add(str(typ))
        elif isinstance(typ, (PTypes.pList, PTypes.pTuple)):
            res.add(typ.__str__())
        else:
            temp = set()
            for item in typ:
                if not item:
                    continue
                temp.add(str(item))
            temp = list(temp)
            temp = str(temp)
            res.add(temp)
    for i, typ in enumerate(res):
        if i != 0:
            temp_str = temp_str + " | "
        temp_str = temp_str + typ
    if not res:
        temp_str = temp_str + "None }"
    else:
        temp_str = temp_str + " }"
    print(temp_str)


if __name__ == '__main__':
    format_string = 'si(y*b(s*z))|nO!:name'
    print(format_string)

    type_signature = parse(format_string)
    # print(type_signature[2].tuple_types)
    print_signature(type_signature)

    # TODO
    # type_signature = parse('O(())')
    # print_signature(type_signature)

    args = ['hmz', -1]
    print(args)
    check(args, type_signature)

    args = [b'hmz', '-1', (b'abc', -1, ('zxc', 1)), '1', 1]
    print(args)
    check(args, type_signature)

    args = ['hmz', -1, (b'abc', 0, ('qwer', None)), 1, 'asd']
    print(args)
    check(args, type_signature)
