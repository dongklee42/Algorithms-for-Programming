import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let person1 = [1,2,3,4,5]
    let person2 = [2,1,2,3,2,4,2,5]
    let person3 = [3,3,1,1,2,2,4,4,5,5]
    var result = Array(repeating: 0, count: 3)
    var answer = [Int]()
    for (i, person) in [person1,person2,person3].enumerated() {
        for j in 0..<answers.count {
            if answers[j] == person[j % person.count] {
                result[i] += 1
            }
        }
    }
    for i in 0..<result.count {
        if result[i] == result.max() {
            answer.append(i + 1)
        }
    }
    return answer
}

print(solution([1,3,2,4,2]))
