'''
Given a hotel which has 10 floors [0-9] and each floor has 26 rooms [A-Z]. You are given a sequence of rooms, where + suggests room is booked, - room is freed. You have to find which room is booked maximum number of times.

You may assume that the list describe a correct sequence of bookings in chronological order; that is, only free rooms can be booked and only booked rooms can be freeed. All rooms are initially free. Note that this does not mean that all rooms have to be free at the end. In case, 2 rooms have been booked the same number of times, return the lexographically smaller room.

You may assume:
N (length of input) is an integer within the range [1, 600]
each element of array A is a string consisting of three characters: "+" or "-"; a digit "0"-"9"; and uppercase English letter "A" - "Z"
the sequence is correct. That is every booked room was previously free and every freed room was previously booked.
Example:

Input: ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
Output: "1A"
Explanation: 1A as it has been booked 2 times.

https://leetcode.com/discuss/interview-question/421787/
'''

def hoteRoom(arr):
	dictRooms={}
	for a in arr:
		if a[0]=='+':
			if a in dictRooms:
				dictRooms[a]+=1
			else:
				dictRooms[a]=1

	maxBook=max(dictRooms.values())
	roomList=[]
	for k in dictRooms:
		if dictRooms[k]==maxBook:
			roomList.append(k)
	if len(roomList)==1:
		print(roomList[0])
	else:
		print(min(roomList))

if __name__ == "__main__":
    books0 = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]
    books1 = ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "+1A", "-1A", "+1A"]
    books2 = ["+1E", "-1E", "+1E", "-1E", "+1E", "-1E", "+1E", "-1E","+2A", "-2A", "+2A", "-2A", "+2A", "-2A", "+2A","-2A","+2B", "-2B", "+2B", "-2B", "+2B", "-2B", "+2B", "-2B"]
    hoteRoom(books0)
    hoteRoom(books1)
    hoteRoom(books2)
