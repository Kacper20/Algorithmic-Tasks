class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
        let numsCopy = Array(nums1[0..<m])
        nums1 = numsCopy + nums2
        var tempNumsCopyIndex = 0
        var tempNums2Index = 0
        
        var tempMergedIndex = 0
        while tempNumsCopyIndex != numsCopy.count && tempNums2Index != nums2.count {
            if numsCopy[tempNumsCopyIndex] < nums2[tempNums2Index] {
                nums1[tempMergedIndex] = numsCopy[tempNumsCopyIndex]
                tempNumsCopyIndex += 1
            } else {
                nums1[tempMergedIndex] = nums2[tempNums2Index]
                tempNums2Index += 1
            }  
            tempMergedIndex += 1
        }
                    //If there are any left from the nums 2 array - write them
        for i in tempNumsCopyIndex..<numsCopy.count {
            nums1[tempMergedIndex] = numsCopy[i]
            tempMergedIndex += 1
        }
    }
}