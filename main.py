from qs import quickSort
from rand_qs import rand_quick_sort
import sys
import copy

def runMain():
    """
    run main does several things:(It does not take in any parameters nor return anything)
    asks user to enter name of file to be sorted 
    Reads in the file line by line and appends each line to a list
    Then writes the sorted array back to a new txt file with '-sorted' appended to the name of the file
    e"""
    rando_Array = []
    print("Please enter the name of the file you would like to read in to be sorted: \n")

    """takes input from the command line """
    file_name = input()

    """Reads the user defined text file and adds each line into the randoArray list"""
    with open(file_name, 'r', encoding='utf-8')as theFile:
        # casting the read in string to an int
        rando_Array = [int(i) for i in theFile]

    

    def run_3():
        print("inside run3")
        """
        Run 3 does does not take any parameters in nor return anything
        It does do several things however that are required per the spec:
    
        Determines 1/4, 1/2 size of the list read in from txt file

        While loop makes a copy of the original list and runs Quicksort 3x for each list size(1/4,1/2, and full lengths) recording the results in the 'results' list
        then prints the results

        NOTE: The printout and recording systems for recording the results needs some tweaking most likely for aesthetics and efficency.
        """
       #List sizes determined in next two lines 
        quarter=(len(rando_Array)-1)//4
        half=(len(rando_Array)-1)//2
        i = 0
        results = []
        f=[]
        while(i <= 17):
            print("inside while")
            if i <= 2:
               f=copy.deepcopy(rando_Array)
               comps, assigns = quickSort(f, 0, quarter)
               results.append("run: "+str(i+1) +" had:"+str(comps)+" comparisons and"+str(assigns) +" variable asssignments after sorting 25 percent of the elements \n")
               #running the random quicksort
               if i>2 & i<=5:
                   f=copy.deepcopy(rando_Array)
                   comps, assigns = rand_quick_sort(f,0,quarter)
                   results.append("RANDOM quick sort run #: "+str(i+1) +" had:"+str(comps)+" comparisons and"+str(assigns) +" variable asssignments after sorting 25 percent of the elements \n")


            elif i>5&i<=11:
                if i>5 & i<=8:
                    f=copy.deepcopy(rando_Array)
                    comps,assigns=quickSort(f,0,half)
                    results.append("run: "+str(i+1) +" had: "+str(comps)+"comparisons and "+str(assigns) +"variable asssignments after sorting 50 percent of the elements \n")
                else:
                    f=copy.deepcopy(rando_Array)
                    comps,assigns=rand_quick_sort(f,0,half)
                    results.append("RANDOM quick sort run #: "+str(i+1) +" had:"+str(comps)+" comparisons and"+str(assigns) +" variable asssignments after sorting 25 percent of the elements \n")
            else:
                if i>11 & i<14:
                    f=copy.deepcopy(rando_Array)
                    comps,assigns=quickSort(f,0,len(rando_Array)-1)
                    results.append("run: "+str(i+1) +" had: "+str(comps)+" comparisons and "+str(assigns) +" variable asssignments after sorting all percent of the elements \n")
                else:
                    results.append("RANDOM quick sort run #: "+str(i+1) +" had:"+str(comps)+" comparisons and"+str(assigns) +" variable asssignments after sorting 25 percent of the elements \n")    
            i+=1  
        print("HELLO",results)
    
    run_3()
    
    
    """
    This opens a new file and appends '-sorted' to the file's name per spec
    then writes the sorted array to a new txt file.
    """
    
    output_file = open (file_name + "-sorted", 'w')
    for i in rando_Array :
        line = str(i) + "\n"
        output_file.write(line)
    output_file.close()
    
    # displays how many values were sorted to the user.
    print("I just sorted "+str(len(rando_Array))+" numbers for you.")
    
print("im about to run main")
runMain()

    
