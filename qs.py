
import numpy
"""Where the magic in quick sort really happens 
Args:
    array: The array to be sorted 
    lo: the current starting index 
    hi: The Current Ending index 

    Returns: 
        the index back to quicksort
        Assignment counter(num_assign)back to quicksort 
        Comparison Counter(num_comps) back to quicksort 
"""
def partition(array, lo, hi):
    num_comps = 0
    num_assign=0
    i = (lo - 1)
    piv = array[hi]
    
    num_assign+=2

    for jay in range(lo, hi):
        
        num_comps+=1
        
        if array[jay]<=piv:
            
            
            i+=1

            array[i], array[jay]= array[jay], array[i]
            num_assign+=2
            
            

    array[i+1], array[hi] = array[hi], array [i+1]
    num_assign+=2
    
    return (i+1),num_comps,num_assign


"""
Args:
    array: The array to be sorted 
    lo:the lowest starting index of the list (list[0])
    hi:the highest starting index of the list(list[len-1])

Returns:
    num_comps: The totalled statistic for the number of comparisons back to main.py 
    num_assign: The totalled statistic for he number of assignment statements back to main.py
"""
def quickSort(array, lo, hi):
    num_comps=0
    num_assign=0
    num_comps+=1
    temp_num_comps=0
    temp_num_assign =0
    if lo < hi:
        
        num_comps+=1

        py,temp_num_comps,temp_num_assign = partition(array, lo, hi)

        num_comps+=temp_num_comps

        num_assign+=temp_num_assign



        temp_num_comps,temp_num_comps=quickSort(array, lo, py-1)

        num_comps+=temp_num_comps

        num_assign+=temp_num_assign

        
        temp_num_comps,temp_num_assign=quickSort(array, py+1, hi)

        num_comps+=temp_num_comps

        num_assign+=temp_num_assign

        print(num_comps,num_assign,"for qs(",lo,",",hi,")")


    return num_comps, num_assign

if __name__ == "__main__" :

    test_values = [ 5, 4, 17, -3, 12, 99, 1]

    print( "pre", test_values)

    c, a = quickSort( test_values, 0, len(test_values)-1)

    print( "post", test_values)

    print( "Total comps were", c)

    print( "Total assigns were", a)
    