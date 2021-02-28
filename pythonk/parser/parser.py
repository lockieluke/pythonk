import warnings

from rply.errors import ParserGeneratorWarning
from rply.parser import LRParser

from pythonk.parser.global_parser import GlobalParser
from pythonk.parser.internal.basic import Basic
from pythonk.parser.internal.data_types import DataTypes
from pythonk.parser.internal.err_handling import ErrorHandling
from pythonk.parser.internal.log import Log
from pythonk.parser.internal.math import Math
from pythonk.parser.internal.py import Py
from pythonk.parser.internal.variable import Variable


class PythonkParser():

    def __init__(self):
        GlobalParser.init_parser()
        self.parse_all()
        pass

    def parse_all(self):

        Basic()
        Log()
        Math()
        DataTypes()
        ErrorHandling()
        Py()
        Variable()
        
        pass

    def get_parser(self) -> LRParser:

        warnings.simplefilter("ignore")

        try:
            return GlobalParser.get_parser().build()
        except ParserGeneratorWarning:

            pass
        pass

    pass
