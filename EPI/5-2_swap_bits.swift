/*
    Implement code that takes integer and swaps bits at indices i and j
*/
extension Int {
    mutating func swapBits(i: Int, j: Int) {
        if ((self >> i) & 1) != ((self >> j) & 1) {
            self ^= Int((1 << i) | (1 << j))
        }
    }
}
