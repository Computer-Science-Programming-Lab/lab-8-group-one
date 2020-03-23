#Andrew DeFran and Viona Veseli
#3/7/2020
#lab8
#Itauma

#import statements
import math
import random
 
#global variables

#function prototypes and definitions
#welcome function
def welcome():
    print("\nHello and welcome to our lab app!\n")

#generate a list of psuedo-random numbers
def listGenerator():

    #1-10,100,1000,10000,100000
    a = random.randint(1, 10)
    b = random.randint(1, 100)
    c = random.randint(1, 1000)
    d = random.randint(1, 10000)
    e = random.randint(1, 100000)

    #i'm confused about how we contain these, is it supposed to be a list?


#Class definitions
class Sort:
    #no attributes
    #we want each instance to have it's own list then we will call the
    #methods and compare them. class implements default constructor 
    #so no __init__ needed?
   
    #sorting methods go here...
    #selection sort method
    def selectionSort(self):
        return 0

    #QuickSort
    def selectionSort(self):
        return 0

    #MergeSort
    def selectionSort(self):
        return 0

    pass


#main
def main():
    #welcome
    welcome()

    #instantiate class object
    #sorter1 = Sort()

    #test case Sort.selectionSort([random vector of numbers])

main()
#end program
