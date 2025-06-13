# Counts up from 1
import re

class Utils:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def countUp(num):
        num = num + 1
        return num
    
    @staticmethod
    def replace_illegal_chars_regex(s: str, pattern: str, replacement: str) -> str:
        return re.sub(pattern, replacement, s)
        #%&$+<>!`|'"={}/*:/\@