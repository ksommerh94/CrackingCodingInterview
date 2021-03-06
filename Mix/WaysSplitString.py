'''
Given a string S, we can split S into 2 strings: S1 and S2.
Return the number of ways S can be split such that the number of unique characters between S1 and S2 are the same.

Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a

Q2: https://leetcode.com/discuss/interview-question/553399/

BIG-O
https://www.inoutcode.com/concepts/big-o/
'''
#O(2n)
def lettersIn(s1,s2):
    flagS1=1
    flagS2=1
    for ss1 in s1:
        if ss1 not in s2:
            flagS1=0
    for ss2 in s2:
        if ss2 not in s1:
            flagS2=0
    if flagS1==1 and flagS2==1:
        return True
    else:
        return False

#O(n)
def uniqueLetter(strings):
    finalstring=""
    for s in strings:
        if s not in finalstring:
            finalstring+=s

    return finalstring

def splitString(arr):
    countSplit=0 #O(1)
    for i in range (len(arr)): #O(n)
        if len(arr)==1: #O(1)
            countSplit=0 #O(1)
        if i==0 and len(arr)>1: #O(1)
            if lettersIn(uniqueLetter(arr[i+1:]),uniqueLetter(arr[0])):
                countSplit+=1#O(1)
        elif lettersIn(uniqueLetter(arr[i+1:]),uniqueLetter(arr[0:i+1])):
            if i+1!=len(arr):#O(1)
                countSplit+=1#O(1)

    print(countSplit)

'''
FINAL BIG O

#  O(1)+(O(n)*(O(1)+O(n)+O(2n)))
#  O(1)+( O(n) * (O(3n))
# O(3n^2)



'''

if __name__ == '__main__':

    fullString='ababa'

    splitString(fullString)
