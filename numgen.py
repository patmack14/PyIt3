# numgen.py
# Module to create arrays filled with random integers.
#
# Usage: python3 numgen.py filename quantity [rangesize]
#
# Created - 2021 January - Erik Steinmetz

import numpy
import sys
from qs import quickSort


def create_array( how_many, range_size) :
    """ Creates an int array with the given number of spots. The array
        is filled with int values within the range size, half negative.
    """
    halfsize = range_size // 2
    answer = numpy.random.randint( -halfsize, halfsize, how_many)
    return answer
    
def write_array( filename, data_array) :
    """ Writes the given data array out to a file with the given filename.
    """
    outfile = open( filename, 'w')
    for value in data_array :
        aline = str(value) + "\n"
        outfile.write(aline)
    outfile.close()
    



if __name__ == "__main__" :
    if len(sys.argv) < 3 :
        print( "Usage: python3 numgen.py, filename, quantity [rangesize]")
        exit()
    the_filename = sys.argv[1]
    the_quantity = int(sys.argv[2])
    the_rangesize = 200
    if len(sys.argv) >= 4 :
        the_rangesize = int(sys.argv[3])
    the_data = create_array( the_quantity, the_rangesize)
    write_array( the_filename, the_data)
    print( the_quantity, "values written to", the_filename)

randoArray = []

file=sys.argv[1]

with open(file,'r', encoding='utf-8')as theFile:
    randoArray=theFile.read().splitlines()
    theFile.close()




quickSort(randoArray, 0, len(randoArray))
print("array after the sort",randoArray)