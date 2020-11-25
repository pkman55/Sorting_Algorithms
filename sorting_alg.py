import numpy
import math
from datetime import datetime

start = datetime.now()

pi = math.pi

arr = numpy.array([12, 11, 13, 5, 6, pi, 87, 74, 5.47, 46, 87, 41, 65, 5/7, 1,
44, 66, 88, 87, 95, 84, 62, 35, 14, 84, 5, 9, 7, 6, 3, 2, 4, 0, 8, 1, -1, -9,
-98, -6574, -64, 741, -541, 69, 74, 85, 96, 4, 41, 52, 63, 69, 58, 47])
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])
done = datetime.now()
print("It took {} seconds".format(done-start))
