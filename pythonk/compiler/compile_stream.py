from typing import List


class CompileStream:

    compiling_file: str = ""
    stream: List[str] = []

    @classmethod
    def set_filename(cls, filename):
        cls.compiling_file = filename

    @classmethod
    def get_compiling_file(cls) -> str:
        return cls.compiling_file

    @classmethod
    def add_stream(cls, code_stream: str):
        if not code_stream.isspace() and not code_stream == '':
            cls.stream.append(code_stream)
            pass
        pass

    @classmethod
    def output_stream(cls) -> str:
        stream_output: str = ""
        for stream_line in cls.stream:
            stream_output += f"{stream_line}\n"
            pass
        return stream_output
        pass

    pass
