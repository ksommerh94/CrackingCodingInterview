'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
'''
def getKey(val,dict):
    for key, value in dict.items():
        if val == value:
            return key

def maxNumbers(arr1,arr2):
    dictArr1={}
    dictArr2={}
    for i in range(len(arr1)):
        if arr1[i] in dictArr1:
            dictArr1[arr1[i]]+=1
        else:
            dictArr1[arr1[i]]=1
        if arr2[i] in dictArr2:
            dictArr2[arr2[i]]+=1
        else:
            dictArr2[arr2[i]]=1
    return dictArr1,dictArr2


def rotate(arr1,arr2):
    dictArr1,dictArr2=maxNumbers(arr1,arr2)
    keyArr1=getKey(max(dictArr1.values()),dictArr1)
    keyArr2=getKey(max(dictArr2.values()),dictArr2)
    countRotation=0
    if keyArr1>keyArr2:
        for i in range(len(arr1)):
            if arr1[i]!=keyArr1 and arr2[i]==keyArr1:
                countRotation+=1
                arr1[i],arr2[i]=arr2[i],arr1[i]
    else:
        for i in range(len(arr1)):
            if arr1[i]!=keyArr2 and arr2[i]==keyArr2:
                countRotation+=1
                arr1[i],arr2[i]=arr2[i],arr1[i]


    if sum(arr1)==(len(arr1)*arr1[1]):
        print(countRotation)
    else:
        print("-1")





if __name__ == '__main__':
    A = [3,2,8,8,8]
    B = [8,8,8,3,1]

    rotate(A,B)
