def largestRange(array):
    # Write your code here.
    bestrange = []
    longestlength = 0
    nums = {} ##Hast table
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentlength = 1
        left = num -1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentlength += 1
            left -=1
        while right in nums:
            nums[right] = True
            currentlength +=1
            right +=1
        if currentlength > longestlength:
            longestlength = currentlength
            bestrange = [left+1,right-1]
        return bestrange
largestRange([8, 4, 2, 10, 3, 6, 7, 9, 1])
