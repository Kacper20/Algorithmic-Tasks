/* Function which takes string of '(' and ')' characters and returns length of the longest valid parentheses substring */
func longestValidParentheses(s: String) -> Int {
    var result = 0
    //On the top of stack we always have starting index of valid sequence.
    var stackOfIndexes = [-1]
    for (i, char) in s.characters.enumerate() {
        if char == "(" {
            stackOfIndexes.append(i)
        }
        if char == ")" {
            stackOfIndexes.removeLast()

            if let top = stackOfIndexes.last {
                result = max(i - top, result)
            } else {
                stackOfIndexes.append(i)

            }
        }
    }
    return result
}


assert(longestValidParentheses("()") == 2)
assert(longestValidParentheses("(()") == 2)
assert(longestValidParentheses(")()())") == 4)
