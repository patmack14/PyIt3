from qs import quickSort
import numpy
import random

def rand_part(array,lo,hi):
    rand_piv=random.randint(lo,hi)
    array[rand_piv], array[hi]= array[hi], array[rand_piv]
    return partition(array,lo,hi)
    


def partition(array, lo, hi):
    """Where the magic in quick sort really happens"-Professor Steinmetz 
Args:
    array: The array to be sorted 
    lo: the current starting index 
    hi: The Current Ending index 

    Returns: 
        the index back to quicksort
        Assignment counter(num_assign)back to quicksort 
        Comparison Counter(num_comps) back to quicksort 
"""
    num_comps = 0
    num_assign=0
    i = (lo - 1)
    piv=array[hi]
    num_assign+=7 #this adds in assignments from
    
    for jay in range(lo, hi):
        
        num_comps+=1
        
        if array[jay]<=piv:
            
            
            i+=1

            array[i], array[jay]= array[jay], array[i]
            num_assign+=2
            
            

    array[i+1], array[hi] = array[hi], array [i+1]
    num_assign+=2
    
    return (i+1),num_comps,num_assign



def rand_quick_sort(array, lo, hi):
    """
Args:
    array: The array to be sorted 
    lo:the lowest starting index of the list (list[0])
    hi:the highest starting index of the list(list[len-1])

Returns:
    num_comps: The totalled statistic for the number of comparisons back to main.py 
    num_assign: The totalled statistic for he number of assignment statements back to main.py
"""
    num_comps=0
    num_assign=0
    num_comps+=1
    temp_num_comps=0
    temp_num_assign =0
    if lo < hi:
        
        

        py,temp_num_comps,temp_num_assign = rand_part(array, lo, hi)

        num_comps+=temp_num_comps

        num_assign+=temp_num_assign



        temp_num_comps,temp_num_comps=rand_quick_sort(array, lo, py-1)

        num_comps+=temp_num_comps

        num_assign+=temp_num_assign

        
        temp_num_comps,temp_num_assign=rand_quick_sort(array, py+1, hi)

        num_comps+=temp_num_comps

        num_assign+=temp_num_assign

        #print(num_comps,num_assign,"for qs(",lo,",",hi,")")

          
        
    return num_comps, num_assign





if __name__ == "__main__" :
    test_values=[]
    
    i=0
   
    while(i<500):
        #test_values.append(random.randint(0,100000))
        test_values.append(i)
        
        i+=1
    
    j,k=quickSort(test_values,0,len(test_values)-1)
    print(j, " ", k)
    
    """
    test_values = [ 5, 4, 17, -3, 12, 99, 1]

    print( "pre", test_values)

    c, a = rand_quick_sort( test_values, 0, len(test_values)-1)

    print( "post", test_values)

    print( "Total comps were", c)

    print( "Total assigns were", a)
"""