# Python/C API for argument parsing
# If PY_SSIZE_T_CLEAN is defined, treats #-specifier to mean Py_ssize_t,
# then `api` will be resolved as `_api_SizeT`.

# (PyObject *args, const char *format, ...) or
# (PyObject *args, const char *format, va_list vargs)
PCAPI_AP_POS = [
    'PyArg_Parse',
    'PyArg_ParseTuple',
    'PyArg_VaParse',
    '_PyArg_Parse_SizeT',
    '_PyArg_ParseTuple_SizeT',
    '_PyArg_VaParse_SizeT',
]

# (PyObject *args, PyObject *kw, const char *format, char *keywords[], ...) or
# (PyObject *args, PyObject *kw, const char *format, char *keywords[],
#   va_list vargs)
# Since version 3.6: Empty names denote positional-only parameters.
PCAPI_AP_KWD = [
    'PyArg_ParseTupleAndKeywords',
    'PyArg_VaParseTupleAndKeywords',
    '_PyArg_ParseTupleAndKeywords_SizeT',
    '_PyArg_VaParseTupleAndKeywords_SizeT',
]

# we can get type from api name
PCAPI_AP_TYPE = [
    'PyList_New',
    'PyList_GetSlice',
    'PyTuple_New',
    'PyTuple_GetSlice',
    'PyDict_New',
    'PyDict_Copy'
]

PCAPI_AP_AS = [
    'PyList_AsTuple',  # List -> Tuple
]

# Python/C API for building value
PCAPI_BV = [
    'Py_BuildValue',
    'Py_VaBuildValue',
    '_Py_VaBuildValue_SizeT',
    '_Py_BuildValue_SizeT'
]

PCFLAG_NOARGS = [
    'METH_NOARGS',
    'METH_CLASS',
]
