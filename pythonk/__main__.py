import os
import sys
import re

from rply.lexer import Lexer
from rply.parser import LRParser

from pythonk.lexer.lexer import PythonkLexer
from pythonk.compiler.compile_stream import CompileStream
from pythonk.compiler.config import CompilerConfig
from pythonk.parser.parser import PythonkParser


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
    CompilerConfig.init_config(projectRoot)
    for line in code.split('\n'):

        if not line.isspace() and not len(line) == 0 and not line.startswith('// '):
            compile_code(line)
        elif line.startswith('// ') and not CompilerConfig.get_remove_comments():
            CompileStream.add_stream(f"# {line.replace('// ', '', 1)}")

        pass

    write_file(CompileStream.output_stream(), os.path.join(CompilerConfig.get_compile_output_dir(), output_filename))

    pass
