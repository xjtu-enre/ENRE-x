import PTypes
from tree_sitter import Language, Parser

import PyFormat
import PyStructure
from Entity import PyMethodDef, PyMethodImpl
from PyStructure import PCAPI_AP_POS, PCAPI_AP_KWD


class Query:
    def __init__(self, C_LANGUAGE):
        self.C_LANGUAGE = C_LANGUAGE

    def PyMethodDef_Query(self, root_node, py_methods):
        # struct or id
        PyMethodDef_query0 = '''
                (declaration
                     type:(struct_specifier
                        name: (type_identifier)
                     )
                     declarator: (init_declarator
                        declarator: (array_declarator)
                        value: (initializer_list)@lists
                     )
                )
                '''
        PyMethodDef_query1 = '''
                (declaration
                     type: (type_identifier)
                     declarator: (init_declarator
                        declarator: (array_declarator)
                        value: (initializer_list)@lists
                     )
                )
                '''
        query0 = self.C_LANGUAGE.query(PyMethodDef_query0)
        query1 = self.C_LANGUAGE.query(PyMethodDef_query1)
        captures0 = query0.captures(root_node)
        captures1 = query1.captures(root_node)
        captures = captures0 + captures1
        if not captures:
            py_methods = []
            return
        for capture in captures:
            lists = capture[0]
            for node in lists.children:
                if node.type == 'initializer_list':
                    self.HandlePyMethodInit(node, py_methods)

    def HandlePyMethodInit(self, initializer_list, py_methods):
        method_name = None
        imp_name = None
        flag = None
        named_children = initializer_list.named_children
        if len(named_children) < 3:
            return
        if named_children[0] and named_children[0].type == 'string_literal':
            t = str(named_children[0].text.decode('utf-8'))
            t = t.removeprefix('"')
            t = t.removesuffix('"')
            method_name = t
        if named_children[1] and named_children[1].type == 'cast_expression':
            for sub_child in named_children[1].children:
                if sub_child.type == 'identifier':
                    imp_name = sub_child.text.decode('utf-8')
        if named_children[2]:
            if named_children[2].type == 'number_literal':
                flag = named_children[2].text.decode('utf-8')
            elif named_children[2].type == 'identifier':
                flag = named_children[2].text.decode('utf-8')
            elif named_children[2].type == 'binary_expression': # METH_VARARGS | METH_KEYWORDS --> PyArg_ParseTupleAndKeywords()
                binary_expression = named_children[2]
                flag0 = binary_expression.named_children[0].text.decode("utf-8")
                flag1 = binary_expression.named_children[1].text.decode("utf-8")
                flag = flag0 + " | " + flag1
            elif named_children[2].type == 'null':
                flag = None
            else:
                ...
                # print("mis catch Flag " + named_children[2].type)

        if method_name and imp_name and flag:
            py_method = PyMethodDef(method_name, imp_name, flag)
            py_methods.append(py_method)

    def PyMethodImpl_Query(self, root_node, method_imp_name):
        PyMethodImpl_query = '''
        (function_definition
             type: (type_identifier)
             declarator: (pointer_declarator
                declarator: (function_declarator
                    declarator: (identifier)
                    parameters: (parameter_list)
                )
             )
             body: (compound_statement)
        )@impl_func
        '''
        PyMethodImplID_query = '''
            declarator: (pointer_declarator
                declarator: (function_declarator
                    declarator: (identifier)@id
                    parameters: (parameter_list)
                )
             )
        '''
        PyMethodImplParams_query = '''
            parameters: (parameter_list)@params    
        '''
        PyMethodImplBody_query = '''    
            body: (compound_statement)@impl_body
        '''
        query = self.C_LANGUAGE.query(PyMethodImpl_query)
        captures = query.captures(root_node)
        id_query = self.C_LANGUAGE.query(PyMethodImplID_query)
        params_query = self.C_LANGUAGE.query(PyMethodImplParams_query)
        body_query = self.C_LANGUAGE.query(PyMethodImplBody_query)

        for node, alias in captures:  # all impl funcs
            id_captures = id_query.captures(node)
            for id_node, id_alias in id_captures:
                id_name = id_node.text.decode("utf-8")
                if id_name == method_imp_name:  # extract 2nd param
                    params = None
                    body = None
                    params_captures = params_query.captures(node)
                    if params_captures:
                        params = params_captures[0][0]
                    for child in node.children:
                        if child.type == 'compound_statement':
                            body = child
                            break
                    method_impl = PyMethodImpl(body, params)
                    return method_impl
        return None

    def PyArgParseCall_Query(self, root_node):
        PyArgParseCall_query = '''
        (call_expression
            function: (identifier)
            arguments: (argument_list)
        )@py_arg_call
        '''
        PyArgParseCalls = []
        query = self.C_LANGUAGE.query(PyArgParseCall_query)
        captures = query.captures(root_node)
        for node, alias in captures:
            if node.children:
                name = node.children[0].text.decode("utf-8")
                assert isinstance(name, str)
                if name in PCAPI_AP_POS or name in PCAPI_AP_KWD:
                    PyArgParseCall = {}
                    PyArgParseCall['name'] = name
                    PyArgParseCall['args'] = node.children[1]
                    PyArgParseCalls.append(PyArgParseCall)
                elif name in PyStructure.PCAPI_AP_TYPE:
                    PyArgParseCall = {}
                    PyArgParseCall['name'] = name
                    PyArgParseCall['args'] = node.children[1]
                    PyArgParseCalls.append(PyArgParseCall)
                else:
                    # print(f"not match Python C API: {name}")
                    ...
        return PyArgParseCalls

    def CheckUnusedParameter_Query(self, root_node, para_list):
        CheckUnusedParameter_query = '''
            (identifier)@id_id
        '''
        ParameterParse_query = """
            parameter_declaration
                type: (type_identifier)
                declarator: (pointer_declarator
                    declarator: (identifier)@id
                ) 
        """
        unused = True
        para_query = self.C_LANGUAGE.query(CheckUnusedParameter_query)
        id_query = self.C_LANGUAGE.query(CheckUnusedParameter_query)
        if len(para_list.named_children) < 2:
            return False
        captures = para_query.captures(para_list.named_children[1])
        para_name = None
        for para, para_alias in captures:
            para_name = para.text.decode("utf-8")

        if not para_name:
            return False

        captures = id_query.captures(root_node)
        for node, alias in captures:
            if node.text.decode("utf-8") == para_name:
                unused = False

        return unused

    def FunctionBodyReturn_Query(self, root_node):
        FunctionBodyReturn_query = '''
            (return_statement)@return
        '''
        return_types = []
        return_query = self.C_LANGUAGE.query(FunctionBodyReturn_query)
        captures = return_query.captures(root_node)
        for node, _ in captures:
            named_child = node.named_children[0]
            return_type = self.ResolveRightVal(named_child, root_node)
            return_types.append(return_type)
        return return_types

    def ResolveVariable_Query(self, var_name, func_body, start_point):
        IDAssignment_query = '''
        (assignment_expression
            left: (identifier)
        )@assignment
        '''
        # 1. find Assignments
        assignments = []
        assignment_query = self.C_LANGUAGE.query(IDAssignment_query)
        captures = assignment_query.captures(func_body)
        for node, alias in captures:
            left_id = node.named_children[0].text.decode("utf-8")
            if left_id == var_name:
                assignments.append(node.named_children[1])
            # TODO: pointer case
        if not assignments:
            return []

        # 2. find last Assignment before variable start_point
        last_assignment = None
        for assignment in assignments:
            if assignment.start_point[0] < start_point[0]:
                last_assignment = assignment
        if not last_assignment:
            return PTypes.pNone()
        assert last_assignment
        return_type = self.ResolveRightVal(last_assignment, func_body)
        return return_type

    def ResolveRightVal(self, r_node, func_body):
        if r_node.type == 'null':
            return PTypes.pNone()
        elif r_node.type == 'call_expression':
            function = r_node.named_children[0]
            arguments = r_node.named_children[1]
            if function.type == 'identifier':
                function_name = function.text.decode("utf-8")
            elif function.named_children and function.named_children[0].type == "identifier":
                function_name = function.named_children[0].text.decode("utf-8")
            else:
                return PTypes.pObject()
            if function_name.startswith('_Py') or function_name.startswith('Py'):
                if function_name in PyStructure.PCAPI_BV:
                    if len(arguments.named_children) > 1 and arguments.named_children[0].type == 'string_literal':
                        fmt_str = arguments.named_children[0].text.decode("utf-8")
                        try:
                            type_signature = PyFormat.parse(fmt_str)
                        except:
                            print("[BUG] Illegal format string: {}".format(fmt_str))
                            type_signature = [[]]
                        return type_signature  # always a product type
                elif function_name.find('_From') != -1 or function_name.find('_New') != -1:
                    # return Py*_From*, Py*_New
                    return PTypes.getPTypeFromTrans(function_name)()
                else:
                    # Unknown Python/C API
                    return PTypes.pObject()
        elif r_node.type == 'identifier':
            """Unresolved Attr: 
            ...
            Resolved Attr:
            Py_None, _Py_NoneStruct, _Py_TrueStruct, _Py_FalseStruct
            """
            named_id = r_node.text.decode("utf-8")
            if named_id == "Py_None" or named_id == "_Py_NoneStruct":
                return PTypes.pNone()
            elif named_id == "_Py_TrueStruct" or named_id == "_Py_FalseStruct":
                return PTypes.pBool()
            else:
                return self.ResolveVariable_Query(named_id, func_body, r_node.start_point)
        elif r_node.type == 'cast_expression':
            for child in r_node.named_children:
                if child.type == 'value':
                    casted_id = child.text.decode("utf-8")
                    # print(f"casted_id: {casted_id}")
                    return self.ResolveVariable_Query(casted_id, func_body, child.start_point)
                elif child.type == 'identifier':
                    return self.ResolveVariable_Query(child.text.decode("utf-8"), func_body, child.start_point)
                elif child.type == 'call_expression':
                    return self.ResolveRightVal(child, func_body)
            print("not match:" + r_node.type)
        else:
            print("not match:" + r_node.type)


