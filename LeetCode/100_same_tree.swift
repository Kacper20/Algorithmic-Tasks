/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func isSameTree(_ p: TreeNode?, _ q: TreeNode?) -> Bool {
        guard let first = p, let second = q else {
            return p == nil && q == nil
        }
        //Recursive: Check left, right and itself
        return isSameTree(first.left, second.left) && isSameTree(first.right, second.right) && first.val == second.val
    }
}