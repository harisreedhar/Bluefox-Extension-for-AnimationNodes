import cython
from animation_nodes.data_structures cimport DoubleList

def addOneList(DoubleList num):
    cdef DoubleList result = DoubleList(length = num.length)
    cdef int i
    for i in range(num.length):
        result.data[i] = num.data[i] + 1
    return result
