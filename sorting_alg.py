import numpy
import math
from insertion import insertionSort
from bubble import bubbleSort

pi = math.pi

unsorted_arr = numpy.array([12, 11, 13, 5, 6, pi, 87, 74, 5.47, 46, 87, 41, 65, 5/7, 1,
44, 66, 88, 87, 95, 84, 62, 35, 14, 84, 5, 9, 7, 6, 3, 2, 4, 0, 8, 1, -1, -9,
-98, -6574, -64, 741, -541, 69, 74, 85, 96, 4, 41, 52, 63, 69, 58, 47])

#for i in range(len(unsorted_arr)):
#    print (unsorted_arr[i])

insertion_arr = unsorted_arr
bubble_arr = unsorted_arr
bubble_arr = numpy.insert(bubble_arr, len(bubble_arr), 69696969)

insertionSort(insertion_arr)
bubbleSort(bubble_arr)

print ("(InsertionSort) Sorted array is:")
for i in range(len(insertion_arr)):
    print (insertion_arr[i])



print ("(BubbleSort) Sorted array is:")
for i in range(len(bubble_arr)):
    print (bubble_arr[i])
