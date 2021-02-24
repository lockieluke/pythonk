import json
import os
from typing import List


class CompilerConfig:
    config: dict
    projectRoot: str

    @classmethod
    def init_config(cls, projectRoot: str):
        cls.projectRoot = os.path.abspath(projectRoot)
        cls.config = json.load(open(os.path.join(cls.projectRoot, 'pykconfig.json')))

    @classmethod
    def get_config(cls) -> object:
        """
        Get compiler options
        :return: Returns compiler options as object
        """
        return cls.config

    @classmethod
    def get_compiler_target(cls) -> str:
        """
        Get compiler target set in the pykconfig.json
        :return: Returns target setting as string e.g. Python 3 as 'python3', Python 2.7 as 'python27' or other Python versions
        """
        return str(cls.config['target'])

    @classmethod
    def get_remove_comments(cls) -> bool:
        """
        Get if compiler should remove comments
        :return: Returns removeComments setting as boolean
        """
        return bool(cls.config['removeComments'])

    @classmethod
    def get_allow_any(cls) -> bool:
        """
        Get if compiler should allow any
        :return: Returns allowAny setting as boolean
        """
        return bool(cls.config['allowAny'])

    @classmethod
    def get_add_sourcemaps(cls) -> bool:
        """
        Get if compiler should add source maps that point to the original PyTHONK source code
        :return: Returns sourceMaps setting as boolean
        """
        return bool(cls.config['sourceMaps'])

    @classmethod
    def get_compile_output_dir(cls) -> str:
        """
        Get the directory the compiler should output the compiled files to
        :return: Returns outDir setting as string
        """
        return str(os.path.join(cls.projectRoot, cls.config['outDir']))


    @classmethod
    def get_excluded_dir(cls) -> List[str]:
        """
        Get directories that the compiler should ignore and exclude
        :return: Returns excluded setting as List[str]
        """
        return list(os.path.join(cls.projectRoot, cls.config['excluded']))


pass
