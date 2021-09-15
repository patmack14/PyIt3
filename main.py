from qs import quickSort
import sys
randoArray =[]
def runMain():
    print("Please enter the name of the file you would like to read in to be sorted: \n")
    fileName=input()

    with open(fileName,'r', encoding='utf-8')as theFile:
        #casting the read in string to an int
        randoArray=[int(i) for i in theFile]
       
       
    
    quickSort(randoArray, 0, len(randoArray)-1)
    print("Your sorted array: ",randoArray)
    
    
    """
    This opens a new file and appends '-sorted' to the file's name per spec
    then writes the sorted array to a new file.
    """
    outputFile = open (fileName + "-sorted", 'w')
    for i in randoArray :
        line = str(i) + "\n"
        outputFile.write(line)
    outputFile.close()
    print("I just sorted "+len(randoArray)+" numbers for you.")
runMain()

    