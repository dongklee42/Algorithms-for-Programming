import UIKit

//let arr1 = [[1,2],[3,4]]
//let arr2 = [[5,6],[7,8]]
//
//func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
//    return zip(arr1, arr2).map{zip($0,$1).map{$0+$1}}
//}
//
//solution(arr1, arr2)
//print(zip(arr1, arr2))
//print(zip(arr1, arr2).map {
//    zip($0, $1).map {
//        $0 + $1
//    }
//})
//
//var arr = Array(repeating: Array(repeating: 0, count: 2), count: 2)
//
//var i = 0, j = 0
//arr1.map { (nums) -> [Int] in
//    defer {
//        print("here nums ", nums)
//        i += 1
//        j = 0
//    print(i, j)
//    }
//    return nums.map { num -> Int in
//        defer {
//            print("here num", num)
//            j += 1
//        print(i, j)
//        }
//        return num + arr2[i][j]
//    }
//}

//for i in 0 ..< 3 {
//    for j in 0 ..< 5 {
//        print("*", terminator: "")
//    }
//    print("")
//}
//
//print(String(repeating: String(repeating: "*", count: 5)+"\n", count: 3))
//
//let strlist = "1234567"
//
//for (i, c) in strlist.indices.enumerated() {
//    print(strlist[c], i)
//}
//
//var test = strlist.map { String($0) }
//test[0] = "8"
//type(of: test[2])
//test.joined(separator: "")
//test
//

//var num = 4231
//Int("4")
//
//let numList = String(num).map { String($0) }
//var listSum: (Array<String>) -> (Int) = { str in
//    var sum = 0
//    for c in str {
//        sum += Int(c)!
//    }
//    return sum
//}
//let sum = listSum(numList)
//
//var sum2 = 0
//let numsum = String(num).map { _ in
//    sum2 += Int(String(c))!
//}
//numsum

//let x = 4231
//var sum = String(x).map { Int(String($0))! }.reduce(0, +)
//sum
//
//let y = [4,1]
//var sum2 = y.reduce(0) { $0 + $1 }
//sum2
//
//let n: Character = "5"
//let n_ = n.wholeNumberValue!
//print(n_)
//
//
////swap
//
//var swap1 = 23
//var swap2 = 45
//(swap1, swap2) = (swap2, swap1)
//print(swap1, swap2)
//
//// euclidGCD
//var gcdA = 1254
//var gcdB = 582
//var res = 0
//var euclidlist = [gcdA, gcdB]
//while euclidlist[1] != 0 {
//    euclidlist[0] %= euclidlist[1]
//    euclidlist.swapAt(0, 1)
//}
//
//
//// 리스트로 풀때와 데이터 직접 스왑할때 다름
//print(euclidlist[0])
//
//Array(repeating: 0, count: 2)
//
//var arrlist = [4,3,2,1]
//
//arrlist.firstIndex(of: arrlist.max()!)
//
////arrlist.remove(at: <#T##Int#>)
//
//Int.max
//func ft_sqrt(_ n: Int64) -> Int64 {
//    var x: Int64 = 0
//    while ((x * x) < n) {
//        x += 1
//    }
//    if x * x == n {
//        return x
//    }
//    return -1
//}
//var n64 = Int64(121)
//
//print("=======================================")
//extension Int64 {
//    func bitCount() -> Int {
//        let hexString = String(self, radix: 2, uppercase: false)
//        print("here_1 ", hexString, hexString.count)
//        return hexString.count
//    }
//}
//func solution(_ n:Int64) -> Int64 {
//    let sqrtBitCount: Int = (n.bitCount() + 1) / 2
//    let min, max: Int64
//    min = 1 << Int(sqrtBitCount - 1)
//    max = 1 << sqrtBitCount
//    print("minmax ", sqrtBitCount, min, max)
//    for i in min..<max {
//        if i * i == n {
//            return (i + 1) * (i + 1)
//        } else if i * i > n {
//            break
//        }
//    }
//    return -1
//}
//
//solution(121)
//
////var lst = String(12345).map { $0.wholeNumberValue }.sorted
//
//var nrev = Int64(872311)
//
//var nrevList = String(nrev).map { $0.wholeNumberValue! }.sorted().reversed()
//var result = ""
//nrevList.forEach { result.append(String($0)) }
//result
//
//var nlen = String(nrev).count
//for i in (0..<nlen).reversed() {
//    print(nrev / Int64(pow(Double(10), Double(i))))
//}
//
//var test = "hello test".map { String($0) }.split(separator: " ")
//type(of: test[0][0].uppercased())
//
//func solutionS(_ s:String) -> String {
//    var result: String = ""
//    let sList = s.map { String($0) }.split(separator: " ").map { Array($0) }
//    print(sList)
//    for i in 0..<sList.count {
//        for j in 0..<sList[i].count {
//            if j % 2 == 0 {
//                result.append(sList[i][j].uppercased())
//            } else {
//                result.append(sList[i][j])
//            }
//        }
//        result.append(" ")
//        print(result)
//    }
//    return result
//}
//
//
//func solutionS2(_ s:String) -> String {
//    var result = ""
//    let str = s.components(separatedBy: " ")
//    print(str)
//
//    for i in 0 ..< str.count{
//        for j in 0 ..< str[i].count{
//            var index = str[i].index(str[i].startIndex, offsetBy: j)
//            if j % 2 == 0{
//                result.append(str[i][index].uppercased())
//            }else{
//                result.append(str[i][index].lowercased())
//            }
//
//        }
//        result.append(" ")
//    }
//    result.removeLast()
//    print(result)
//    return result
//}
//
//solutionS2("try hello world")
//
//var testS = "Ad"
//var testslist = ["A", "b"]
////testslist.joined()
////Character(testS).asciiValue
////String(Character(testS).asciiValue! + 1)
//
//
//
//"A" == testS[testS.startIndex]
//for (i, c) in testS.indices.enumerated() {
//    print(i, c)
//}
//
//(25 + 25) % 25
//func getOffset(_ c: Character, _ cased: String) -> Int {
//    var resultIndex: Int = 0
//    for i in cased.indices {
//        if cased[i] == c {
//            break
//        }
//        resultIndex += 1
//    }
//    return resultIndex
//}
//
//func alphaloop(_ s:String, _ n:Int) -> String {
//    let upper: String = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
//    let lower: String = "abcdefghijklmnopqrstuvwxyz"
//    var offset: Int = 0
//    var result: String = ""
//    for i in s.indices {
//        if "A" <= s[i] && s[i] <= "Z" {
//            offset = Int((getOffset(s[i], upper) + n) % 26)
//            result.append(upper[upper.index(upper.startIndex, offsetBy: offset)])
//        } else if "a" <= s[i] && s[i] <= "z" {
//            offset = Int((getOffset(s[i], lower) + n) % 26)
//            result.append(lower[lower.index(lower.startIndex, offsetBy: offset)])
//        } else {
//            result.append(String(s[i]))
//        }
//    }
//    return result
//}

Int("+1234")

// 배열 내에 같은 문자열가진 인덱스 조회
func solution(_ seoul:[String]) -> String {
    return "김서방은 \(seoul.firstIndex(of: "Kim")!)에 있다"
}

