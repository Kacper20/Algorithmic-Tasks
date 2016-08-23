/*
 
 You are given an n x n 2D matrix representing an image.

 Rotate the image by 90 degrees (clockwise).

 Follow up:
 Could you do this in-place?
 */


func rotate(inout matrix: [[Int]]) {
    let size = matrix.count
    for i in 0..<size / 2 {
        for j in i..<size - i - 1 {
            let temp = matrix[i][j]
            matrix[i][j] = matrix[size - j - 1][i]
            matrix[size - j - 1][i] = matrix[size - i - 1][size - j - 1]
            matrix[size - i - 1][size - j - 1] = matrix[j][size - i - 1]
            matrix[j][size - i - 1] = temp
        }
    }
}