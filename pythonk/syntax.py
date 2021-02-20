import asyncio
import aiofiles
import errors
IDK: int = -1
ALLOWED_VAR_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
ALLOWED_VAR_CHARS_NO_FIRST = "0123456789"


def throw(error):
    if isinstance(error, errors.pykCompileError):
        ln, cn = error.ln, error.cn
        print(f"[{ln},{cn}]{error.name}: {error.msg}")
    return error

class Context:
    skip: str = ""
    rst: bool
    def __init__(self, f, ln: int, cn: int):
        self.file = f
        self.ln = ln
        self.cn = cn
    def skip_until(self, reset=True):
        self.skip = "\n"
        self.rst = reset
    def skip_line(self, reset=True):
        self.skip="\n"
        self.rst = reset

class Syntax:
    def __init__(self, coro, matches: list, priority: int):
        self.matches = matches
        self.check = coro
        self.priority = priority


def syntax(priority, *matches):
    """
    Returns a Syntax object. If no matches supplied, kw_<name> will be used.
    The higher the priority, the earlier it will get interpreted.
    """
    def decorate(coro):
        if matches is None and coro.__name__.startswith("kw_"):
            matches = [coro.__name__[3:]]
        if matches is None:
            raise errors.pykInternalCompilerError(f"@syntax() for coro {coro.__name__} without matches.")
        syn = Syntax(coro, matches, priority)
        return syn

    return decorate

class Keywords:
    @syntax(5)
    async def kw_pass(self, ctx):
        pass
    @syntax(8)
    async def kw_def(self, ctx):
        pass
    @syntax(8)
    async def kw_class(self, ctx):
        pass
    @syntax(8)
    async def kw_import(self, ctx):
        pass

class Punctuations:
    @syntax(IDK, ";")
    async def semicolon(self, ctx):
        pass
    @syntax(IDK, ":")
    async def colon(self, ctx):
        pass
    @syntax(IDK, ".")
    async def full_stop(self, ctx):
        pass
    @syntax(IDK, "=")
    async def equal(self, ctx):
        #todo process the value and skip until semicolon
        pass
    @syntax(IDK, " ")
    async def space(self, ctx):
        pass
    @syntax(21, "\n")
    async def new_line(self, ctx: Context):
        ctx.rst = True
    @syntax(20, "#")
    async def hashtag(self, ctx):
        ctx.skip_line()


def sync_get_sorted_syn():
    # get attributes from each cls, loop thru the attribs, filter the ones that are of cls Syntax
    attribs = keywords = [getattr(Punctuations, name) for name in dir(Keywords) if isinstance(getattr(Punctuations, name), Syntax)]
    punctuations = [getattr(Keywords, name) for name in dir(Keywords) if isinstance(getattr(Keywords, name), Syntax)]
    attribs.extend(punctuations)
    # sort the syntaxes by their priority
    attribs.sort(key=lambda syn: syn.priority)
    punctuations.sort(key=lambda syn: syn.priority) 
    keywords.sort(key=lambda syn: syn.priority)
    return attribs, punctuations, keywords


def hasMatches(o: str, d: dict):
    for match in d:
        if match.startswith(o):
            return True
    return False

async def analyse(f, futureSyntaxes: asyncio.Future):
    dsSyntaxes: dict
    dsPuncs: dict
    dsKws: dict
    errs: list
    variables: list     # list of known names/words
    sCurVar: str        # on-going variable name construction
    isCurPunc: bool     # is sCurVar currently an on-going punctuation construction?
    ctx: Context        # Context to be passed onto
    ln: int = 1         # line number
    cn: int = 1         # char number
    async for line in f:  # async iterator, enum() doesn't work
        rline = line + "\n"
        for cn, char in enumerate(rline):  # $char_loop
            # pre hooks
            if ctx.skip:  # need to skip code alright
                if ctx.skip == "\n":
                    ctx.skip = ""
                    break  # $char_loop
                if char == ctx.skip:
                    ctx.skip = ""
                continue  # onto the next char
            if isCurPunc:  # $punc_check
                if char in ALLOWED_VAR_CHARS or char in ALLOWED_VAR_CHARS_NO_FIRST or char in '\n':  # a new word
                    ctx = Context(f, ln, cn-1)  # process the cur punc
                    await dsPuncs[sCurVar].check(ctx)
                    isCurPunc = False  # then leave $punc_check for the word proc
                else:  # is also a symbol, continue building it
                    sCurVar += char
                    if not hasMatches(sCurVar, dsPuncs):  # no more new matches, new symbol?
                        ctx = Context(f, ln, cn-1)  # ctx the old one
                        await dsPuncs[sCurVar[:-1]].check(ctx)
                        # and yep, new symbol
                        sCurVar = char
                        if not hasMatches(char, dsPuncs):  # syntax error: inv symbol
                            errs.append(throw(errors.pykSyntaxError(f"Invalid symbol {char}", ln, cn)))
                            isCurPunc = False
                            sCurVar = ""
                    continue
            if char in ALLOWED_VAR_CHARS or (sCurVar and char in ALLOWED_VAR_CHARS_NO_FIRST):
                sCurVar += char
                continue
            # sCurVar is a full word / val

            # onetime - init syntaxes from future
            if not dsSyntaxes:
                syntaxes, puncs, kws = futureSyntaxes.result()  # yes this is how you get results from Future
                dsSyntaxes = dsPuncs = dsKws = {}
                def assign(d,k,v): d[k] = v  # for use in the list comp and no we don't need an executor idiot
                # std::vector<Tuple<dict, list>> todo
                todo: list = [(dsSyntaxes, syntaxes), (dsPuncs, puncs), (dsKws, kws)]
                # assign the matches as keys to the corr. dict like a badass :die:
                [assign(d, match, syn) for match in syn.matches for syn in l for d, l in todo]

            # check if it is keyword
            if sCurVar in dsKws:
                ctx = Context(f, ln, cn)  # generate ctx
                await dsKws[sCurVar].check(ctx)  # call syntax.check
            else:  # not a keyword, probably a variable
                variables.append(sCurVar)
            sCurVar = None

            #* check for a new symbol/punctuation
            for match in dsPuncs:
                if match.startswith(char):
                    sCurVar = char
                    isCurPunc = True
        #? might want to clean up symbols and words
        sCurVar = ""
        isCurPunc = False
        ln += 1

async def parse(filename):
    loop = asyncio.get_event_loop()
    futureSyntaxes = loop.run_in_executor(None, sync_get_sorted_syn)
    async with aiofiles.open(filename, mode='r') as f:
        await analyse(f, futureSyntaxes)
    
