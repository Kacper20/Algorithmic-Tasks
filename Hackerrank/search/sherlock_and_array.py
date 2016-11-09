#find if there exists an element in the array, such that, the sum of 
#elments on its left is equal to the sum of elements on its right.

for _ in range (input()):
    
    flag = False
    length = input()
    numbers = map(int, raw_input().split())
    sum_left = 0
    sum_right = 0
    if len(numbers) == 1:
        print 'YES'
        continue
    for i in range(1, len(numbers)):
        sum_right += numbers[i]
    for i in range (1, (len(numbers)-1)):
        sum_left+= numbers[i-1]
        sum_right -= numbers[i]
        if sum_left == sum_right:
            print 'YES'
            flag = True
    if flag == False:
        print 'NO'
        


