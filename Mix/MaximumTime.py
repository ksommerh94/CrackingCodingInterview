'''
You are given a string that represents time in the format hh:mm.
Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible.
Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.

https://leetcode.com/discuss/interview-question/396769/
'''
def maximumTime (list):
    s=[]
    for l in list:
        s.append(l)
    maxMin2='9'
    maxMin1='5'
    if s[4]=='?':
        s[4]=maxMin2
    if s[3]=='?':
        s[3]=maxMin1
    if s[1]=='?':
        if s[0]=='1' or  s[0]=='0' :
            s[1]=maxMin2
        else:
            s[1]='3'
    if s[0]=='?':
        if s[1]<='3':
            s[0]='2'
        else:
            s[0]='1'
    print(s)


if __name__ == '__main__':
    a="?4:5?"
    b="23:5?"
    c="2?:22"
    d="0?:??"
    f="??:??"

    maximumTime(a)
    maximumTime(b)
    maximumTime(c)
    maximumTime(d)
    maximumTime(f)
