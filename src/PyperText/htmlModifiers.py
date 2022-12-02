from .tools import SuspendedString
def italics(text:str)->SuspendedString:
    '''
    Italicize Given Text
    '''
    return SuspendedString("<i>",text,"</i>")
def bold(text:str)->SuspendedString:
    '''
    Bold Given Text
    '''
    return SuspendedString("<b>",text,"</b>")
def underline(text:str)->SuspendedString:
    '''
    Underline Given Text
    '''
    return SuspendedString("<u>",text,"</u>")
def abbreviate(full:str,abbrev:str)->SuspendedString:
    '''
    Abbreviate Text
    '''
    return SuspendedString(f"<abbrev title=\"{full}\">",abbrev,"</abbrev>")
def newline()->str:return "<br>"
def code(code:str)->str:return f"<code>{code}</code>"
if __name__=="__main__":pass