/*Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 You may assume no duplicates in the array.

 Here are few examples.
 [1,3,5,6], 5 → 2
 [1,3,5,6], 2 → 1
 [1,3,5,6], 7 → 4
 [1,3,5,6], 0 → 0
 */
 func searchInsert(nums: [Int], _ target: Int) -> Int {

    func helperSearch(inout nums: [Int], left: Int, right: Int) -> Int? {
        if left > right { return nil }
        let midIndex = (left + right) / 2
        if nums[midIndex] == target { return midIndex }

        if target > nums[nums.count - 1] { return nums.count }
        if target < nums[0] { return 0 }

        if midIndex > 0 && nums[midIndex - 1]  < target && nums[midIndex] > target {
            return midIndex
        }

        if midIndex < nums.count - 1 && nums[midIndex + 1] > target && nums[midIndex] < target {
            return midIndex + 1
        }

        if nums[midIndex] > target {
            return helperSearch(&nums, left: 0, right: midIndex - 1)
        } else {
            return helperSearch(&nums, left: midIndex + 1, right: right)
        }
    }
    var nums = nums

    if let index = helperSearch(&nums, left: 0, right: nums.count - 1) {
        return index
    }
    return -1
}