import json
import os
from typing import List


class CompilerConfig:

    def __init__(self, projectRoot: str):
        self.config = json.load(open(os.path.join(projectRoot, 'ptconfig.json')))
        pass

    def get_config(self) -> object:
        """
        Get compiler options
        :return: Returns compiler options as object
        """
        return self.config
        pass

    def get_compiler_target(self) -> str:
        """
        Get compiler target set in the ptconfig.json
        :return: Returns target setting as string e.g. Python 3 as 'python3', Python 2.7 as 'python27' or other Python versions
        """
        return str(self.config['target'])
        pass

    def get_remove_target(self) -> bool:
        """
        Get if compiler should remove comments
        :return: Returns removeComments setting as boolean
        """
        return bool(self.config['removeComments'])
        pass

    def get_allow_any(self) -> bool:
        """
        Get if compiler should allow any
        :return: Returns allowAny setting as boolean
        """
        return bool(self.config['allowAny'])
        pass

    def get_add_sourcemaps(self) -> bool:
        """
        Get if compiler should add source maps that point to the original PyTHONK source code
        :return: Returns sourceMaps setting as boolean
        """
        return bool(self.config['sourceMaps'])
        pass

    def get_compile_output_dir(self) -> str:
        """
        Get the directory the compiler should output the compiled files to
        :return: Returns outDir setting as string
        """
        return str(self.config['outDir'])
        pass

    def get_excluded_dir(self) -> List[str]:
        """
        Get directories that the compiler should ignore and exclude
        :return: Returns excluded setting as List[str]
        """
        return list(self.config['excluded'])
        pass

    pass
