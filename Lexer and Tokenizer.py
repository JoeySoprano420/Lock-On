module Lexer {
    func tokenize(code: String) -> List<Token> {
        let tokens = []
        let index = 0
        while (index < length(code)) {
            let char = code[index]
            if (char == ' ' or char == '\n') {
                continue
            } elif (isDigit(char)) {
                let number = ""
                while (isDigit(code[index])) {
                    number += code[index]
                    index += 1
                }
                tokens.append(Token("NUMBER", number))
            } elif (char == '+') {
                tokens.append(Token("PLUS", "+"))
                index += 1
            }
            # Handle other cases like variables, operators, keywords
        }
        return tokens
    }
}
