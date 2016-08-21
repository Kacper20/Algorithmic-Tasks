/*
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
*/

func search(nums: [Int], _ target: Int) -> Int {
    func helperSearch(inout nums: [Int], left: Int, right: Int) -> Int {
        if left > right { return -1 }
        let midIndex = (left + right) / 2
        if nums[midIndex] == target { return midIndex }

        if nums[left] <= nums[midIndex] {
            //Left part is sorted and target value lies there
            if target >= nums[left] && target <= nums[midIndex] { return helperSearch(&nums, left: left, right: midIndex - 1) }
            return helperSearch(&nums, left: midIndex + 1, right: right)
        }
        //Right part is sorted and target value lies there.
        if target >= nums[midIndex] && target <= nums[right] {
            return helperSearch(&nums, left: midIndex + 1, right: right)
        }
        return helperSearch(&nums, left: left, right: midIndex - 1 )
    }
    var nums = nums
    return helperSearch(&nums, left: 0, right: nums.count - 1)
}
