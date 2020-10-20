'''
There are some processes that need to be executed.
Amount of a load that process causes on a server that runs it, is being represented by a single integer.
Total load caused on a server is the sum of the loads of all the processes that run on that server.
You have at your disposal two servers, on which mentioned processes can be run.
Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads.

Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.

https://leetcode.com/discuss/interview-question/356433/
'''
def checksum(arr,vn1):
    print(vn1)



def MinAbsDifferenceServerLoads (arr):
    #Greedy solution Dynamic programming
    #Bottom-up
    server1=[]
    server2=[]

    validNumber1=sum(arr)//2
    validNumber2=sum(arr)-validNumber1

    checksum(arr,validNumber1)


if __name__ == '__main__':

    arr=[1, 2, 3, 4, 5]
    MinAbsDifferenceServerLoads(arr)
