module AOTCompiler {
    func compile(ast: AST) -> MachineCode {
        let code = ""
        for node in ast.nodes:
            if (node is NumberNode):
                code += "LOAD " + node.value + "\n"
            elif (node is OperatorNode and node.operator == "+"):
                code += "ADD \n"
        # Output machine code
        return code
    }
}
