import os
import sys

from rply.lexer import Lexer
from rply.parser import LRParser

from pythonk.compiler.compile_stream import CompileStream
from pythonk.compiler.config import CompilerConfig
from pythonk.lexer.lexer import PythonkLexer
from pythonk.parser.parser import PythonkParser


class CompilerCLI:
    filename: str
    basename: str
    output_filename: str
    project_root: str

    @classmethod
    def __init__(cls):
        cls.setup_vars()
        CompilerConfig.init_config(cls.project_root)

        for line in CompilerToolchain.read_file(cls.filename).split('\n'):
            if CompileConditions.normal(line):
                CompilerToolchain.compile_line(line)
            elif CompileConditions.comment(line):
                CompileStream.add_stream(f"# {line.replace('// ', '', 1)}")
            pass

        cls.output_compile()

        pass

    @classmethod
    def setup_vars(cls):
        cls.filename = sys.argv[1]
        cls.basename = os.path.basename(cls.filename)
        cls.output_filename: str = f"{cls.basename.split('.')[0]}.py"
        cls.project_root: str = os.path.dirname(cls.filename)
        pass

    @classmethod
    def output_compile(cls):
        CompilerToolchain.create_compile_output_folder()
        CompilerToolchain.safe_write_file(CompileStream.output_stream(),
                                          os.path.join(CompilerConfig.get_compile_output_dir(), cls.output_filename))
        pass

    pass


class CompileConditions:

    @staticmethod
    def normal(stream: str):
        return not stream.isspace() and not len(stream) == 0 and not stream.startswith('// ')

    @staticmethod
    def comment(stream: str):
        return stream.startswith('// ') and not CompilerConfig.get_remove_comments()

    pass


class CompilerToolchain:
    lexer: Lexer = PythonkLexer().get_lexer()
    parser: PythonkParser = PythonkParser()

    class ScriptExtensionNotMatch(Exception):
        pass

    @staticmethod
    def read_file(filename: str) -> str:
        data: str
        with open(filename, 'r') as file:
            data = file.read()
            pass
        return data

    @staticmethod
    def safe_write_file(data: str, filename: str):
        if filename.endswith('.py'):
            with open(filename, 'a') as file:
                file.truncate(0)
                file.write(data)
                pass
        else:
            raise CompilerToolchain.ScriptExtensionNotMatch()
        pass

    @staticmethod
    def create_compile_output_folder():
        output_dir: str = os.path.join(CompilerConfig.projectRoot, CompilerConfig.get_compile_output_dir())
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        pass

    @classmethod
    def compile_line(cls, code_line_stream: str):
        tokens = cls.lexer.lex(code_line_stream)
        parser: LRParser = cls.parser.get_parser()
        parser.parse(tokens).eval()
        pass

    pass
