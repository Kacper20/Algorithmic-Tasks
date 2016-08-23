/*
 Given an array of strings, group anagrams together.

 For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
 Return:

 /*
 Given an array of strings, group anagrams together.
 [
 ["ate", "eat","tea"],
 ["nat","tan"],
 ["bat"]
 ]
 Note: All inputs will be in lower-case.
 */

func groupAnagrams(strs: [String]) -> [[String]] {
    //We could create some kind of hash table(or maybe dict in swift and use hashing)
    //But let's use ordinary sorting to achieve it.

    var indexesAndStrings = Array(strs.enumerate()).map { ($0, String($1.characters.sort())) }
    indexesAndStrings.sortInPlace { $0.1 < $1.1 }

    var groupedAnagrams = [[String]]()
    groupedAnagrams.append([])

    var lastString: String?
    for i in 0..<indexesAndStrings.count {
        let currentElem = indexesAndStrings[i].1
        let currentIndex = indexesAndStrings[i].0
        if let last = lastString where last != currentElem {
            groupedAnagrams.append([strs[currentIndex]])
        } else {
            groupedAnagrams[groupedAnagrams.count - 1].append(strs[currentIndex])
        }
        lastString = currentElem
    }
    return groupedAnagrams
}

let arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
let result = groupAnagrams(arr)
print(result)