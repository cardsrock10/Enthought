// Define the modules name
%module example3b

// Specify code that should
// be included at top of
// wrapper file.
%{
#define SWIG_FILE_WITH_INIT
#include "vect.h"
#include "numpy/arrayobject.h"
%}

%init %{
    import_array();
%}

%typemap(out) int *vect {
    npy_intp dims[1] = {3};
    PyObject *base = NULL;

    // Did the call to vect() return NULL?
    if ($1 == NULL) {
        PyErr_SetString(PyExc_MemoryError, "out of memory");
        SWIG_fail;
    }

    // Create a NumPy array to hold the result, using the memory
    // allocated by vect() as the array data.
    $result = PyArray_SimpleNewFromData(1, dims, NPY_INT, $1);

    if ($result == NULL) {
        PyErr_SetString(PyExc_MemoryError, "out of memory");
        free($1);
        SWIG_fail;
    }

    base = PyCObject_FromVoidPtr($1, free);
    if (base == NULL) {
        Py_DECREF($result);
        free($1);
        PyErr_SetString(PyExc_MemoryError, "out of memory");
        SWIG_fail;
    }

    // Point the 'base' of the numpy array to the object that
    // holds the memory point.  That object also holds a pointer to
    // the free() function that will be used to free the memory when
    // the array no longer has any references to it. 
    PyArray_BASE($result) = base;
}

%typemap(in) int *vector {
    // Ensure that the input arguments is actually
    // a NumPy array of integers.  It must be a contiguous
    // array of length 3.
    if (!PyArray_Check($input)) {
        PyErr_SetString(PyExc_ValueError, "argument must be a numpy array");
        SWIG_fail;
    }
    if (!PyArray_ISCONTIGUOUS($input)) {
        PyErr_SetString(PyExc_ValueError, "array is not contiguous");
        SWIG_fail;
    }
    if (PyArray_Size($input) != 3) {
        PyErr_SetString(PyExc_ValueError, "array length is not 3");
        SWIG_fail;
    }
    if (!(PyArray_ISINTEGER($input) && PyArray_ITEMSIZE($input) == sizeof(int))) {
        PyErr_SetString(PyExc_ValueError, "array type must be integer");
        SWIG_fail;
    }

    // Convert Python object pointer to data pointer.
    // The data point is retrieved from the NumPy object
    // using the PyArray_DATA macro.
    $1 = PyArray_DATA($input);
}

// Define interface. Easy way
// out - Simply include the
// header file and let SWIG 
// figure everything out.
%include "vect.h"
