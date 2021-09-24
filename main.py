from qs import quickSort
import sys
import copy

def runMain():
    rando_Array = []
    print("Please enter the name of the file you would like to read in to be sorted: \n")

    """takes input from the command line """
    fileName = input()

    """Reads the user defined text file and adds each line into the randoArray list"""
    with open(fileName, 'r', encoding='utf-8')as theFile:
        # casting the read in string to an int
        rando_Array = [int(i) for i in theFile]


    def run_3():
       
       quarter=(len(rando_Array)-1)//4
       half=(len(rando_Array)-1)//2
       i = 0
       results = []
       f=[]
       while(i <= 8):
            if i <= 2:
               f=copy.deepcopy(rando_Array)
               comps, assigns = quickSort(f, 0, quarter)
               results.append("run: "+str(i+1) +" had: "+str(comps)+"comparisons and "+str(assigns) +"variable asssignments after sorting 25 percent of the elements \n")

            elif i<=5:
                f=copy.deepcopy(rando_Array)
                comps,assigns=quickSort(f,0,half)
                results.append("run: "+str(i+1) +" had: "+str(comps)+"comparisons and "+str(assigns) +"variable asssignments after sorting 50 percent of the elements \n")
            else:
                f=copy.deepcopy(rando_Array)
                comps,assigns=quickSort(f,0,len(rando_Array)-1)
                results.append("run: "+str(i+1) +" had: "+str(comps)+" comparisons and "+str(assigns) +" variable asssignments after sorting all percent of the elements \n")
           
            i+=1  
       print(results)
    
    run_3()
    
    
    """
    This opens a new file and appends '-sorted' to the file's name per spec
    then writes the sorted array to a new file.
    """
    
    outputFile = open (fileName + "-sorted", 'w')
    for i in rando_Array :
        line = str(i) + "\n"
        outputFile.write(line)
    outputFile.close()
    
    # displays how many values were sorted to the user.
    print("I just sorted "+str(len(rando_Array))+" numbers for you.")
    

runMain()

    
