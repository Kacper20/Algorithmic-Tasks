/*Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
 */

func firstMissingPositive(nums: [Int]) -> Int {
    func partitionNegative(inout tab: [Int]) -> Int {
        var j = 0
        for i in 0..<tab.count where tab[i] <= 0  {
            if i != j {
                swap(&tab[i], &tab[j])
            }
            j += 1
        }
        return j
    }

    var nums = nums
    let indexOfFirstPositive = partitionNegative(&nums)

    var slice = nums[indexOfFirstPositive..<nums.count]

    for elem in slice where elem <= slice.count{
        let indxToReverse = elem + indexOfFirstPositive - 1
        slice[indxToReverse] = -(abs(slice[indxToReverse]))
    }

    for i in slice.indices {
        if slice[i] > 0 {
            return i + 1 - indexOfFirstPositive
        }
    }

    return nums.count - indexOfFirstPositive + 1
}
