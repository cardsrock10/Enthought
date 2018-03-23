// Define the modules name
%module example3

// Specify code that should be included at top of wrapper file.
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

    // Did the call to vect() return NULL?
    if ($1 == NULL) {
        PyErr_SetString(PyExc_MemoryError, "out of memory");
        SWIG_fail;
    }

    // Create a NumPy array to hold the result.
    $result = PyArray_SimpleNew(1, dims, NPY_INT);

    if ($result == NULL) {
        PyErr_SetString(PyExc_MemoryError, "out of memory");
        free($1);
        SWIG_fail;
    }

    // Copy the data from the memory created by vect() into 
    // the NumPy array's memory.
    memcpy(PyArray_DATA($result), $1, 3 * sizeof(int));

    // Free the memory that was allocated by vect().
    free($1);
}

%typemap(in) int *vector {
    // Ensure that the input arguments is actually a NumPy
    // array of integers.  It must be a contiguous array of
    // length 3.
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

    // Convert Python object pointer to data pointer.  The data
    // point is retrieved from the NumPy object using the
    // PyArray_DATA macro.
    $1 = PyArray_DATA($input);
}

// Define interface. Easy way out - Simply include the header
// file and let SWIG figure everything out.
%include "vect.h"
