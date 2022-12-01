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


if __name__=="__main__":pass