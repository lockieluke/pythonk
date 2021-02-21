import os
import sys

sys.path.append(os.path.join(os.getcwd(), 'pythonk'))

from rply.lexer import Lexer
from rply.parser import LRParser

from lexer.lexer import PythonkLexer
from compiler.compile_stream import CompileStream
from compiler.config import CompilerConfig
from parser.parser import PythonkParser


def read_file(filename: str) -> str:
    data: str
    with open(filename, 'r') as file:
        data = file.read()
        pass
    return data
    pass


def write_file(data: str, filename: str):
    with open(filename, 'a') as file:
        file.truncate(0)
        file.write(data)
        pass
    pass


def compile_code(code: str):
    lexer: Lexer = PythonkLexer().get_lexer()
    tokens = lexer.lex(code)
    rawParser: PythonkParser = PythonkParser()
    rawParser.parse_all()
    parser: LRParser = rawParser.get_parser()
    parser.parse(tokens).eval()
    pass


if __name__ == '__main__':
    filename: str = sys.argv[1]
    basename: str = os.path.basename(filename)
    output_filename: str = f"{basename.split('.')[0]}.py"
    projectRoot: str = os.path.dirname(filename)
    code: str = read_file(filename)
    compileConfig: CompilerConfig = CompilerConfig(projectRoot)
    for line in code.split('\n'):
        compile_code(line)
        pass

    if not os.path.exists(compileConfig.get_compile_output_dir()):
        os.mkdir(compileConfig.get_compile_output_dir())
        pass
    write_file(CompileStream.output_stream(), os.path.join(compileConfig.get_compile_output_dir(), output_filename))

    pass
