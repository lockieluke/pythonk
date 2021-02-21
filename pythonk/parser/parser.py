import warnings

from rply.errors import ParserGeneratorWarning
from rply.parser import LRParser

from parser.global_parser import GlobalParser
from parser.internal.data_types import DataTypes
from parser.internal.err_handling import ErrorHandling
from parser.internal.log import Log
from parser.internal.math import Math


class PythonkParser():

    def __init__(self):
        GlobalParser.init_parser()
        pass

    def parse_all(self):

        Log()
        Math()
        DataTypes()
        ErrorHandling()
        
        pass

    def get_parser(self) -> LRParser:

        warnings.simplefilter("ignore")

        try:
            return GlobalParser.get_parser().build()
        except ParserGeneratorWarning:

            pass
        pass

    pass
