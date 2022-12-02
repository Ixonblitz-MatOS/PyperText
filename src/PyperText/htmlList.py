from .htmlWidget import htmlWidget,htmlObject
from typing import Any,Literal,overload
#if[if]==if[if[if][if]]-=[if.iff[iff[if]]]
class Member(htmlObject):
    '''
    HTML member class for lists derived from htmlObject
    '''
    code:str=""
    type="Member"
    @overload
    def __init__(self,mem:str) -> None:
        self.header=mem.split(">")[0]+" >"
        self.footer=mem.split("<"[2])#<T>TT<T>->['','T>TT','T>']
        self.value=mem.split(">"[1].split("<")[0])
        self.style:list[str]=list[str]()
        self.options:list[str]=list[str]()
        if "style=" in self.header:self.options=self.header.split("style\"")[1].rstrip(self.header.split("style\"")[1][-1]).split(";")#<tag style="">

    @overload
    def __init__(self)->None:
        pass
class List(htmlWidget):
    '''
    HTML List Class derived from htmlWidget
    '''
    code=""
    type="List"
    def _ret(val:Any)->Any:return val
    def _lst(val:str)->str:return f"<li>{val}</li>"
    def __init__(self,ordered:bool=False)->None:
        self.options:list[str]=list[str]()
        self.elements:list[str]=list[str]()
        self.header=f"<{self._ret('ol') if self.ordered else self._ret('ul')}>"
        self.footer=f"</{self._ret('ol') if self.ordered else self._ret('ul')}>"
        self.ordered=ordered
        self.style:list[str]=list[str]()
    def addMember(self,member:str)->None:
        '''
        Adds an element to the list
        '''
    def _buildElements(self)->str:
        final=""
        for i in self.elements:final+=i+"\n"
        return final
    @overload
    def getMember(self,value:str)->Member:
        for i in self.elements:
            if i.replace("<li>","").replace("</li>","")==value:
                return Member(self._ret('ol') if self.ordered else self._ret('ul'),self._buildElements())
class DescriptionList(htmlWidget):
    '''
    HTML Description List Class derived from htmlWidget
    '''
    code=""
    type="DescriptionList"
    def __init__(self)->None:
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.header="<dl >"
        self.footer="</dl>"

