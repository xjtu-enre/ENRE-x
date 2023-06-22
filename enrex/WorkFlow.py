import os
import time
from pathlib import Path

import PTypes
import PyFormat
import PyStructure
from Entity import PyMethodDef, PyMethodImpl, Summary
from Query import Query
from tree_sitter import Language, Parser


def work_flow(root_path):
    C_LANGUAGE = Language('build/my-languages.so', 'c')
    parser = Parser()
    parser.set_language(C_LANGUAGE)
    q = Query(C_LANGUAGE)
    summary = Summary()

    start_time = time.time()
    handle_files(root_path, parser, q, summary)
    end_time = time.time()

    print("========== statistics ==========")

    print("time elapse: {:.3f}s".format(end_time - start_time))
    print("file analyzed directly and compilable: {}".format(summary.count_compilable))
    print("wrapper function (WP): {}".format(summary.count_wrapper))
    print("WP has format string(s): {}".format(summary.count_wrapper_has_fmtstr))
    print("WP with METH_NOARGS: {}".format(summary.count_wrapper_marked_noarg))
    print("WP with No use ARG: {}".format(summary.count_wrapper_no_use_arg_bug))


def handle_files(path: Path, parser, q: Query, summary):
    if path.is_dir():
        for sub_file in path.iterdir():
            handle_files(sub_file, parser, q, summary)
    else:
        if path.is_file() and path.name.endswith(".c"):
            handle_file(path, parser, q, summary)


def handle_file(file_path, parser, q: Query, summary):
    print(f"{file_path}")
    with open(file_path, encoding="UTF-8") as f:
        code = f.read()
        tree = parser.parse(bytes(code, "utf-8"))
        summary.count_compilable = summary.count_compilable + 1
        root_node = tree.root_node
        py_methods = []
        q.PyMethodDef_Query(root_node, py_methods)
        if not py_methods:
            return
        for md in py_methods:
            print(md)

        for method in py_methods:
            assert isinstance(method, PyMethodDef)
            method_impl = q.PyMethodImpl_Query(root_node, method.method_imp_name)

            if not method_impl:
                continue
            print("------------------------------------------------------------")
            method.method_impl = method_impl
            print(f"{method.method_name} -> {method.method_imp_name}{method_impl.impl_func_args.text.decode('utf-8')}")
            summary.count_wrapper = summary.count_wrapper + 1

            # find Python/C API argument parsing function call in wrapper function
            PyArgParseCalls = q.PyArgParseCall_Query(method.method_impl.impl_func_body)

            BUG_MSG = "[BUG] function declared without param or with unused param but ml_flag is not METH_NOARGS"

            if method.method_imp_name == "_encode_cleanup":
                print("_encode_cleanup")

            if method.method_flag not in PyStructure.PCFLAG_NOARGS:  # METH_NOARGS, * | METH_CLASS
                method.method_para_unused = q.CheckUnusedParameter_Query(method.method_impl.impl_func_body, method.method_impl.impl_func_args)
                if method.method_para_unused:
                    summary.count_wrapper_no_use_arg_bug = summary.count_wrapper_no_use_arg_bug + 1
                    print(BUG_MSG)

            if PyArgParseCalls:
                summary.count_wrapper_has_fmtstr = summary.count_wrapper_has_fmtstr + 1

            for PyArgParseCall in PyArgParseCalls:
                api_name = PyArgParseCall["name"]
                api_args = PyArgParseCall["args"]

                fmt_str = None
                type_signature = None
                if api_name in PyStructure.PCAPI_AP_KWD:
                    if len(api_args.named_children) > 2 and api_args.named_children[2].type == 'string_literal':
                        fmt_str = api_args.named_children[2].text.decode("utf-8")
                    else:
                        pass
                elif api_name in PyStructure.PCAPI_AP_POS:
                    if len(api_args.named_children) > 1 and api_args.named_children[1].type == 'string_literal':
                        fmt_str = api_args.named_children[1].text.decode("utf-8")
                    else:
                        pass
                elif api_name in PyStructure.PCAPI_AP_TYPE:
                    obj = PTypes.getPTypeFromTypeName(api_name)
                    # print(f"getPTypeFromTypeName:{obj.__str__()}")
                    type_signature = [obj.__str__()]
                else:
                    pass

                if fmt_str:
                    # print(fmt_str)
                    type_signature = PyFormat.parse(fmt_str)

                if type_signature:
                    PyFormat.print_signature(type_signature, is_para=True)
            else:
                if method.method_flag == 'METH_NOARGS':
                    print("[]")
                    summary.count_wrapper_marked_noarg = summary.count_wrapper_marked_noarg + 1
                elif method.method_para_unused:
                    print("[]")

            if method.method_imp_name == "_encode_cleanup":
                print("_encode_cleanup")


            print('--->>>')
            return_types = q.FunctionBodyReturn_Query(method.method_impl.impl_func_body)
            PyFormat.print_signature(return_types, is_para=False)


