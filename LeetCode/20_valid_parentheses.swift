/*Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

 The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 */

func isValid(s: String) -> Bool {
    func isBeginning(char: Character) -> Bool {
        switch char {
            case "(", "[", "{": return true
            default: return false
        }
    }

    func arePair(lhs: Character, rhs: Character) -> Bool {
        switch (lhs, rhs) {
        case ("(", ")"), ("[", "]"), ("{", "}"): return true
        default: return false
        }
    }

    var stack = [Character]()
    for element in s.characters {
        if isBeginning(element) {
            stack.append(element)
        } else if let top = stack.last {
            if !arePair(top, rhs: element) { return false }
            stack.removeLast()
        } else { return false }
    }
    return stack.isEmpty
}