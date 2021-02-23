from typing import List

stream: List[str] = []


class CompileStream:

    @staticmethod
    def add_stream(code_stream: str):
        global stream
        if not code_stream.isspace() and not code_stream == '':
            stream.append(code_stream)
            pass
        pass

    @staticmethod
    def output_stream() -> str:
        global stream
        stream_output: str = ""
        for stream_line in stream:
            stream_output += f"{stream_line}\n"
            pass
        return stream_output
        pass

    pass
