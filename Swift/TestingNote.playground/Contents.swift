import UIKit

let arr1 = [[1,2],[3,4]]
let arr2 = [[5,6],[7,8]]

func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    return zip(arr1, arr2).map{zip($0,$1).map{$0+$1}}
}

solution(arr1, arr2)
print(zip(arr1, arr2))
print(zip(arr1, arr2).map {
    zip($0, $1).map {
        $0 + $1
    }
})

var arr = Array(repeating: Array(repeating: 0, count: 2), count: 2)

var i = 0, j = 0
arr1.map { (nums) -> [Int] in
    defer {
        print("here nums ", nums)
        i += 1
        j = 0
    print(i, j)
    }
    return nums.map { num -> Int in
        defer {
            print("here num", num)
            j += 1
        print(i, j)
        }
        return num + arr2[i][j]
    }
}

//func deferfunc() -> Int {
//    defer {
//        print("here1")
//    }
//}
