from antlr4 import CommonTokenStream, InputStream

from src.ast_visitor import ASTVisitor
from gen.katoLexer import katoLexer
from gen.katoParser import katoParser

from src.exec_tree import exec_tree

file = "./input.txt"

def main():
    input_stream = InputStream(open(file).read())
    lexer = katoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = katoParser(stream)
 
    visitor = ASTVisitor()
    start = parser.program()
    tree = visitor.visit(start)
    print("tree:", tree)
    print("program value:", exec_tree(tree, stack=[]))
    

if __name__ == "__main__":
    main()
