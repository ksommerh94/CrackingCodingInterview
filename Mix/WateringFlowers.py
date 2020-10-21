'''
Given an array of plants of N integers(for the amount of water needed by each plant),
and variables capacity1 and capacity2( for the capacity od your watering can and your friend's)
Return the number of times you and yuor firend will have to reeflikk your cans to water all plants.

For example:
Plants=[2,4,5,1,2]
Capcity1=5
Capcity2=7

the funcion should return 2
'''

def watering(can1,can2,flowers):
    refill=2
    fillCan1=can1
    fillCan2=can2

    for i in range(len(flowers)):
        print(i)

        if (len(flowers)-1-i)==i:
            if fillCan1+fillCan2>=flowers[i]:
                break
            else:
                print("reffillll")
                refill+=1
                break
        else:
        #left-right
            if fillCan1<flowers[i]:
                print("reff")
                refill+=1
                fillCan1=can1
                fillCan1-=flowers[i]
            elif fillCan1>=flowers[i]:
                fillCan1-=flowers[i]
        #right-left
            if fillCan2<flowers[len(flowers)-1-i]:
                print("reffiii")
                refill+=1
                fillCan1=can1
                fillCan2-=flowers[len(flowers)-1-i]
            elif fillCan2>=flowers[len(flowers)-1-i]:
                fillCan2-=flowers[len(flowers)-1-i]

    return refill




if __name__ == '__main__':
    flowers=[5,5,5,5,5]
    can1=5
    can2=7

    print(watering(can1,can2,flowers))
