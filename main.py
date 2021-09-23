from qs import quickSort
import sys
randoArray =[]
def runMain():
    print("Please enter the name of the file you would like to read in to be sorted: \n")
    
    """takes input from the command line """
    fileName=input()

    """Reads the user defined text file and adds each line into the randoArray list"""
    with open(fileName,'r', encoding='utf-8')as theFile:
        #casting the read in string to an int
        randoArray=[int(i) for i in theFile]
       
       
    
    num_comps,num_assign = quickSort(randoArray, 0, len(randoArray)-1)
    print("The Number of Assignments that occured in quicksort was: "+str(num_assign)+", The number of comparisons that occured in Quicksort was:  "+str(num_comps))
    
    
    """
    This opens a new file and appends '-sorted' to the file's name per spec
    then writes the sorted array to a new file.
    """
    
    outputFile = open (fileName + "-sorted", 'w')
    for i in randoArray :
        line = str(i) + "\n"
        outputFile.write(line)
    outputFile.close()
    
    #displays how many values were sorted to the user.
    print("I just sorted "+str(len(randoArray))+" numbers for you.")

runMain()

    