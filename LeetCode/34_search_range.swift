/***LEETCODE #34***/
/*
 Given a sorted array of integers, find the starting and ending position of a given target value.

 Your algorithm's runtime complexity must be in the order of O(log n).

 If the target is not found in the array, return [-1, -1].

 For example,
 Given [5, 7, 7, 8, 8, 10] and target value 8,
 return [3, 4].
*/


func searchRange(nums: [Int], _ target: Int) -> [Int] {
    func rangeForSameValues(inout nums: [Int], index: Int) -> [Int] {
        var starting = index
        print(index)
        for i in (0..<starting).reverse() {
            if nums[starting] == nums[i] {
                starting -= 1
            } else { break }

        }
        var ending = index
        for i in (ending + 1..<nums.count) {
            if nums[starting] == nums[i] {
                ending += 1
            } else { break }
        }
        return [starting, ending]
    }

    func helperSearch(inout nums: [Int], left: Int, right: Int) -> Int? {
        if left > right { return nil }
        let midIndex = (left + right) / 2
        if nums[midIndex] == target { return midIndex }

        if nums[midIndex] > target {
            return helperSearch(&nums, left: 0, right: midIndex - 1)
        } else {
            return helperSearch(&nums, left: midIndex + 1, right: right)
        }
    }
    var nums = nums

    if let index = helperSearch(&nums, left: 0, right: nums.count - 1) {
        return rangeForSameValues(&nums, index: index)
    }
    return [-1, -1]
}