import Foundation

func readInput() -> (Array<Int>, Int)? {
    guard let firstLine = readLine(), let secondLine = readLine() else { return nil }
    let splittedValues = firstLine.componentsSeparatedByString(" ")
    guard splittedValues.count == 2 else { return nil }
    guard let numbersOfRotations = Int(splittedValues[1]) else { return nil }
    let array = secondLine.componentsSeparatedByString(" ").flatMap { Int($0) }
    return (array, numbersOfRotations)
}

extension Array {
    func rotated(times: Int) -> Array<Element> {
        let newRightArray = self[0..<times]
        let newLeftArray = self[times..<count]
        return Array(newLeftArray) + Array(newRightArray)
    }

    var desc: String {
        return self.reduce("") { (result, current) -> String in
            return result + "\(current) "
        }
    }
}

func compute() {
    guard let (array, rotationTimes) = readInput() else { return }
    print(array.rotated(rotationTimes).desc)
}

compute()

