import numgen
import numpy

def partition(array, lo, hi):
    i = (lo - 1)
    piv = array[hi]
    
    for jay in range(lo, hi):

        if array[jay]<=piv:

            i+=1
            array[i], array[jay]= array[jay], array[i]

    array[i+1], array[hi] = array[hi], array [i+1]

    return (i+1)


def quickSort(array, lo, hi):

#if there's only 1 element, the array is sorted by default
    if len(array) ==1:
        return array
    
    if lo < hi:
        py = partition(array, lo, hi)

        quickSort(array, lo, py-1)
        quickSort(array, py+1, hi)

