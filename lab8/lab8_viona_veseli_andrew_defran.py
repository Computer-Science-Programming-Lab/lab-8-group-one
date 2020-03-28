#Andrew DeFran and Viona Veseli
#3/7/2020
#lab8
#Itauma

#import statements
import math
import random
import timeit
from time import perf_counter

import sys
sys.setrecursionlimit(3000)
 
#global variables

#function prototypes and definitions
#welcome function
def welcome():
    print("\nHello and welcome to our lab app!\n")

#generate a list of psuedo-random numbers
def listGenerator(des_length):

    #1-10,100,1000,10000,100000. start with 1-10 and build in function to make
    #other sizes
    n = 10
    unsorted_list = []

    #loop through list and append a random in in the range.
    for i in range(1, des_length):
        unsorted_list.append(random.randint(1, n))

    return unsorted_list
    



#   Select an algorithm
#   Params: test list, length, number of repititions
def SelectAlgorithm():

    #   Prompt the user and execute sort on arg test_list
    #   Return time to complete

    algoOptions = '''
        The options are as follows: \n
        1: Selection Sort \n
        2: Quicksort \n
        3: Merge Sort \n\n
    '''


    #   Present and get option of algorithm from user
    print(algoOptions)
    selection = input('Please select an option:')    

    #   Get desired length of list
    L = int( input("What size (random) list would you like to test with?") )

    #   Generate the random list
    test_list = listGenerator(L)
    
    #   Get number of test runs
    N = int(input('How many times would you like to run test? '))

    #   Instantiate sorting class object
    sorting = Sort()

    #   Instantiate list of test results
    tests = list()



    #   Option one is selection sort
    if selection == '1':
        for i in range(1,N):

            t1 = perf_counter()
            sorting.selectionSort(test_list)
            t2 = perf_counter()

            #   Record result
            test = { 
            "algorithm": "Selection Sort",
            "test":i+1,
            "length":L,
            "elapsed":(t2-t1) 
            }

            #   Append result
            tests.append(test)

            #   Shuffle the list
            random.shuffle(test_list)

        return tests
    

    #   Option two is quicksort
    elif selection == '2':
        for i in range(0,N):

            t1 = perf_counter()
            sorting.quickSort(test_list)
            t2 = perf_counter()

            #   Record result
            test = { 
            "algorithm": "QuickSort",
            "test":i+1,
            "length":L,
            "elapsed":(t2-t1) 
            }

            #   Append result
            tests.append(test)

            #   Shuffle the list
            random.shuffle(test_list)

        return tests


    #   Option three is merge sort
    elif selection == '3':
        for i in range(1,N):
            print('final:')
            t1 = perf_counter()
            print(sorting.mergeSort(test_list))
            t2 = perf_counter()
            #   Record result
            test = { 
            "algorithm": "MergeSort",
            "test":i+1,
            "length":L,
            "elapsed":(t2-t1) 
            }

            #   Append result
            tests.append(test)
            
            #   Shuffle the list
            random.shuffle(test_list)

        return tests


    #   Catch Error
    else:
        print("Error: invalid selection. Try again.")
        SelectAlgorithm(test_list, description, L, N)









#Class definitions
class Sort:
    #no attributes?
    #we want each instance to have it's own list then we will call the
    #methods and compare them. class implements default constructor 
    #so no __init__ needed?
   
    #sorting methods go here...
    #selection sort method
    def selectionSort(self, input_list):

        #Selection sorting logic. two for loops to compare the values and swap
        for l in range(0, len(input_list) - 1):
            smallest = l
            for u in range(l + 1, len(input_list)):
                #check which is bigger and swap
                if input_list[u] < input_list[smallest]:
                    smallest = u
            input_list[l], input_list[smallest] = input_list[smallest], input_list[l]

        print("\nUsing selection sort is:\n " + str(input_list) )
        return 0
        
    #QuickSort ie divide and conquer
    def quickSort(self, input_list):
        #define the pivot and empty list variables
        pivot = len(input_list) // 2
        lesser = []
        equals = []
        greater = []

        #separate the values against the pivot into their buckets
        for i in range(len(input_list)):
            if input_list[i] < input_list[pivot]:
                lesser.append(input_list[i])
            elif input_list[i] > input_list[pivot]:
                greater.append(input_list[i])
            else:
                equals.append(input_list[i])

        #use recursion to sort the smaller lists
        if len(lesser) > 1:
            lesser = self.quickSort(lesser)
        if len(greater) > 1:
            greater = self.quickSort(greater)

        #concatenate the sorted lists and return result
        sortedlist = lesser + equals + greater

        return sortedlist




    #MergeSort
    def mergeSort(self, initial):

        
        def _merge(A, B):

            i_A = 0
            i_B = 0

            res = list()

            while( ( i_A < len(A) ) and ( i_B < len(B) ) ):
                #   Compare values, move indexes accordingly until one list is empty
                if (A[i_A] < B[i_B]): 
                    res.append( A[i_A] )
                    i_A += 1

                else: 
                    res.append( B[i_B] )
                    i_B += 1

            new_A = [ A[i] for i in range( i_A, len(A) )]
            new_B = [ B[i] for i in range( i_B, len(B) )]

            if len(new_A) != 0:
                res.extend(new_A)
            if len(new_B) != 0:
                res.extend(new_B)

            return res            


        #   Loop, comparing the numbers at respective indices
        if len(initial) == 1:
            return initial

        #   Continue to split and recurse
        else: 
            
            #   Middle value
            M = int( len(initial) / 2)
            
            A = initial[:M]

            B = initial[(len(initial) - M):]

            return _merge( self.mergeSort( A ), self.mergeSort( B ) )

        #   Loop, splitting until working with arrays of size 1





#main
def main():



    #welcome
    welcome()




    print(*SelectAlgorithm(), sep='\n')


main()
#end program
