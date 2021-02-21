import json
import os
from typing import List


class CompilerConfig:
    config: dict
    projectRoot: str

    def __init__(self, projectRoot: str):
        self.projectRoot = os.path.abspath(projectRoot)
        self.config = json.load(open(os.path.join(self.projectRoot, 'pykconfig.json')))

    def get_config(self) -> object:
        """
        Get compiler options
        :return: Returns compiler options as object
        """
        return self.config

    def get_compiler_target(self) -> str:
        """
        Get compiler target set in the ptconfig.json
        :return: Returns target setting as string e.g. Python 3 as 'python3', Python 2.7 as 'python27' or other Python versions
        """
        return self.config['target']

    def get_remove_target(self) -> bool:
        """
        Get if compiler should remove comments
        :return: Returns removeComments setting as boolean
        """
        return self.config['removeComments']

    def get_allow_any(self) -> bool:
        """
        Get if compiler should allow any
        :return: Returns allowAny setting as boolean
        """
        return self.config['allowAny']

    def get_add_sourcemaps(self) -> bool:
        """
        Get if compiler should add source maps that point to the original PyTHONK source code
        :return: Returns sourceMaps setting as boolean
        """
        return self.config['sourceMaps']

    def get_compile_output_dir(self) -> str:
        """
        Get the directory the compiler should output the compiled files to
        :return: Returns outDir setting as string
        """
        return os.path.join(self.projectRoot, self.config['outDir'])

    def get_excluded_dir(self) -> List[str]:
        """
        Get directories that the compiler should ignore and exclude
        :return: Returns excluded setting as List[str]
        """
        return os.path.join(self.projectRoot, self.config['excluded'])
