func solution(_ new_id:String) -> String {
    var converted = new_id
        .map { c -> String in
            if c.isUppercase { return c.lowercased() }
            return String(c)
        }.filter { s in
            let regex = try! NSRegularExpression(pattern: "[a-zA-Z0-9_.-]")
            if let _ = regex.firstMatch(in: s, options: [], range: NSRange(location: 0, length: s.count)) {
                return true
            }
            return false
        }.joined()
        .components(separatedBy: ".")
        .map { s -> String in
            if s.count >= 1  {
                return "." + s
            }
            return ""
        }.joined()
        .trimmingCharacters(in: ["."])
    if converted.count >= 16 {
        converted = String(converted[converted.startIndex..<converted.index(converted.startIndex, offsetBy: 15)]).trimmingCharacters(in: ["."])
        print(converted, converted.count)
    } else if converted.count < 1 {
        converted = String("a")
    }
    if converted.count < 3 {
        let buffer: String = String(converted[converted.index(converted.endIndex, offsetBy: -1)])
        while converted.count < 3 {
            converted = converted + buffer
        }
    }
    return converted
}
