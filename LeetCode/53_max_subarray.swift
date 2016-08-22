/*Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
 */

func maxSubArray(nums: [Int]) -> Int {
    guard let first = nums.first else { return 0 }
    var maxResult = first
    var tempMax = first

    for elem in nums.dropFirst() {
        tempMax = max(tempMax + elem, elem)
        maxResult = max(tempMax, maxResult)
    }

    return maxResult
}

