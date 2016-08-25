/*
5.1 
How would you go about computing parity of very large number of 64-bit non-negative integers

 */

//First, we need to create some structure, because our solution will involve some kind of memoization
struct ParityChecker {
    /*
     Basic idea goes as follows:
     Divide this 64-bit number into 4 parts. We will hold memorized solutions for 16-bit parts of bits. Solution i will provide is not optimized in terms of memory, but in terms of speed.
     We could have bit checking arrays(UInt8 is too big to hold 2 bits of data). But this would involve lots of dividing, which is quite expensive so we'll stick with current solution
     */
    private var parityCheckingArray = Array<UInt8>(repeating: 2, count: 65536)
    //It's parity function that checks
    private mutating func internalCheckParity(num: UInt16) -> UInt8 {
        let precheckNumber = parityCheckingArray[Int(num)]
        guard precheckNumber == 2 else { return precheckNumber }
        var result: UInt8 = 0
        var number = num
        while number > 0 {
            result ^= 1
            number &= (number - 1)
        }
        parityCheckingArray[Int(num)] = result
        return result
    }

    mutating func checkParity(num: UInt64) -> Bool {
        let helperMaxVal: UInt16 = 0xFFFF
        //Ugh, you Swift! :(
        let first = internalCheckParity(num: helperMaxVal & UInt16(num))
        let second = internalCheckParity(num: helperMaxVal & UInt16(num >> UInt64(16)))
        let third = internalCheckParity(num: helperMaxVal & UInt16(num >> UInt64(32)))
        let fourth = internalCheckParity(num: helperMaxVal & UInt16(num >> UInt64(48)))

        return (first ^ second ^ third ^ fourth) == 0
    }
}

var checker = ParityChecker()
let res = checker.checkParity(num: UInt64(3))
let res1 = checker.checkParity(num: UInt64(3))