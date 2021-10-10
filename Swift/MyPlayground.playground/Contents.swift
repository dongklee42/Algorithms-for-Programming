import UIKit


let str = "hello world!"
str.startIndex

var idx = str.index(str.startIndex, offsetBy: 6)
str[idx]
str[str.startIndex]
//str[str.endIndex] // 문자열 범위 Character밖의 인덱스 또는 문자열 범위 밖의 인덱스에 액세스하려고 하면 런타임 오류가 발생합니다.

let t1 = "\u{D55C}"
let t2 = "\u{1112}\u{1161}\u{11AB}"
let t3 = "한"
t1.utf8.count
t2.utf8.count
t3.utf8.count
t1.utf16.count
t2.utf16.count
t3.utf16.count
//"\u{D55C}"                  // 한
var ko_str = "\u{1112}\u{1161}\u{11AB}글짱짱맨".precomposedStringWithCanonicalMapping

for u in t2.utf8.indices {
    print(t2[u])
}


//t2[t2.utf16.startIndex]

for k in ko_str.indices {
    print(ko_str[k], k)
}

ko_str[ko_str.index]

print(str.startIndex, str.endIndex)

struct Foo {
  let x: Int
  let y: Bool
}

MemoryLayout<Int>.size      // returns 8-byte on 64-bit
MemoryLayout<Bool>.size     // returns 1
MemoryLayout<Foo>.size      // returns 9
MemoryLayout<Foo>.stride    // returns 16 because of alignment requirements
MemoryLayout<Foo>.alignment // returns 8, addresses must be multiples of 8

let s = "hello"
MemoryLayout<String>.size(ofValue: s)
let size = s.utf16.count
