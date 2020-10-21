'''
One strinf is stricly smaller than another when the frequency of occurrence of he smalles character
in the string is less than the frequency of occurrenve of the samllest character in the omparison string.

For example, string "abcd" is smaller that strinf "aaa", becasuse the samelest character(in lexicographical order) in "abcd" is 'a',
with a frequency of 1 and the smalest character in "aaa", is also 'a', but with a frequency of 3.

In another example , string "a" is smaller than string "bb", becasuse the smallest character in "a" is 'a' with frecuency of 1
and the smales in "bb" is 'b' with the frequency of 2

write a function that given a string A(which contains M strings delimited by ',') and string B, returns an array C of N integers

'''
def countChar(arrayDict):
    dict={}
    for ad in arrayDict:
        if ad in dict:
            dict[ad]+=1
        else:
            dict[ad]=1
    return dict


def compare(arr1,minarr2):

    dictMin=countChar(minarr2)
    arrayC=[]
    for array1 in arr1:
        dictArr=countChar(array1)
        minArr=min(dictArr.keys())
        # print(dictArr.keys())
        # print(min(dictArr.keys()))
        # print(dictMin.keys())
        # print("ccc")
        # print(dictMin.values())
        # print(dictArr[minArr])
        if minArr in dictMin.keys():
            print(dictArr[minArr])
            print(dictMin[minArr])
            if dictArr[minArr]<dictMin[minArr]:
                print("entro")
                arrayC.append(arr1.index(array1))
            elif dictArr[minArr]==dictMin[minArr]:
                array1.pop(array1.index(minArr))
    return arrayC




    # for ar in arr1:
    #     if ar in dictarr1:
    #         dictarr1[ar]+=1
    #     else:
    #         dictarr1[ar]=1



if __name__ == '__main__':

    array1='abcd,aabc,bd'
    array2='aaa,aa'
    arr1=array1.split(',')
    arr2=array2.split(',')

    # print(arr1)
    # print(arr2)
    # print(min(arr2))
    compare(arr1,min(arr2))
