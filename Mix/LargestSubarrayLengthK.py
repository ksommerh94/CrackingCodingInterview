'''
Array X is grater than array Y if the first non-matching element in both arrays has a greater value in x than in Y.
For example, for arrays X and Y such that x=[1,2,4,3,5] Y=[1,2,3,4,5]
X is grather than Y becasue the first element that does not mach is larger in X X[2]>Y[2]

A contiguous subarray is defined by an interval of the indices. In other words, a contiguous subarray is a subarray which has consecutive indexes.

Write a function that, given a zero-indexed array a consisting of N integers ans an integer K, return the largest contiguous subarrays of length K

For exaple given array A and K=4 duch that:
A=[1,4,3,2,5]
The funcion should return [4,3,2,5] because there are 2 subarrays of size 4 --> [1,4,3,2] abs [4,3,2,5] and the largest subarray is [4,3,2,5]

https://leetcode.com/discuss/interview-question/352459/

'''
def largestSubarrayLenghtK (arr,k):
    listArr=[]
    for i in range (len(arr)):
        if i+k-1< len(arr):
            listArr.append(arr[i:i+k])
    maxValue=0
    maxArr=[]
    for la in listArr:
        if sum(la)> maxValue:
            maxValue=sum(la)
            maxArr=la
    print(maxArr)





if __name__ == '__main__':
    arr=[5,77,2,76,71,70,75,79,7,0,1]
    k=4
    largestSubarrayLenghtK(arr,k)
