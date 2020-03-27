#Andrew DeFran and Viona Veseli
#3/7/2020
#lab8
#Itauma

#import statements
import math
import random
import timeit
 
#global variables

#function prototypes and definitions
#welcome function
def welcome():
    print("\nHello and welcome to our lab app!\n")

#generate a list of psuedo-random numbers
def listGenerator():

    #1-10,100,1000,10000,100000. start with 1-10 and build in function to make
    #other sizes
    n = 10
    unsorted_list = []

    #loop through list and append a random in in the range.
    for i in range(1, 11):
        unsorted_list.append(random.randint(1, n))

    return unsorted_list
    

def selectionSort():

        #list variables
        input_list = [5, 1, 11, 4, 3, 10, 8, 4, 11, 9]
        

        #test print
        print("The list " + str(input_list))

        #sorting logic
        for u in range(0, len(input_list) - 1):
            smallest = u
            for j in range(u + 1, len(input_list)):
                if input_list[j] < input_list[smallest]:
                    smallest = j
            input_list[u], input_list[smallest] = input_list[smallest], input_list[u]

        print("using selection sort is:\n " + str(input_list) )

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
    def mergeSort(self, input_list):

        print("\nUsing Merge sort is:\n " + str(input_list) )

    pass

#main
def main():
    #welcome
    welcome()

    #instantiate class object
    sorter1 = Sort()
    test_list = listGenerator()

    #test case using list generator function
    #print
    print("The list " + str(test_list))

    #selection sort with time
    start = timeit.default_timer()
    sorter1.selectionSort(test_list)
    stop = timeit.default_timer()
    print('Time: ', stop - start) 

    #quick sort with timer
    print("\nUsing Quick sort is: " )
    start = timeit.default_timer()
    print(sorter1.quickSort(test_list))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    #sorter1.MergeSort(test_list)

main()
#end program
