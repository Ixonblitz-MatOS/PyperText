"""
List objects
"""
# pylint: disable=locally-disabled, line-too-long, invalid-name, super-init-not-called, broad-except, unspecified-encoding,attribute-defined-outside-init
from typing import Any,Type
from ultraimport.ultraimport import ultraimport
Class=Any|Type[type]
htmlWidget,htmlObject=ultraimport('__dir__/htmlWidget.py',{"htmlWidget":Class,"htmlObject":Class})
#if[if]==if[if[if][if]]-=[if.iff[iff[if]]]
class Member(htmlObject):
    '''
    HTML member class for lists derived from htmlObject
    '''
    code:str=""
    type="Member"
    def __init__(self,mem:str,opt:Any) -> None:
        self.header=mem.split(">")[0]+" >"
        self.footer=mem.split("<"[2])#<T>TT<T>->['','T>TT','T>']
        self.value=mem.split(">"[1].split("<")[0])
        self.style:list[str]=list[str]()
        self.options=opt
        if "style=" in self.header:
            self.style=self.header.split("style\"")[1].rstrip(self.header.split("style\"")[1][-1]).split(";")#<tag style="">
            self.header=self.header.split("style=")[0]+">"
            if self.header!=f"<{self.header.split('<')[1].split(' ')[0]} >":
                #there are options
                print("There are options in Header, overwriting the provided options from before.")
                self.options=self.header.split(">")[0].split("<")[1].split(" ")[2]
                #<T as="" aa="">->['<T as="" aa=""','']->['','T','as="" aa=""','']
            else:self.header=f"<{self.header.split('>')[0].split('<')[1].split(' ')[1]} >"#no options
        else:pass#FINISH

class List(htmlWidget):
    '''
    HTML List Class derived from htmlWidget
    '''
    code=""
    type="List"
    def _ret(self,val:Any|str)->Any:
        """
        return same val
        """
        return val
    def _lst(self,val:str)->str:
        """
        return list from string
        """
        return f"<li>{val}</li>"
    def __init__(self,ordered:bool=False)->None:
        self.options:list[str]=list[str]()
        self.ordered=ordered
        self.elements:list[str]=list[str]()
        self.header=f"<{self._ret('ol') if self.ordered else self._ret('ul')}>"
        self.footer=f"</{self._ret('ol') if self.ordered else self._ret('ul')}>"
        self.style:list[str]=list[str]()
    def addMember(self,member:str)->None:
        '''
        Adds an element to the list
        '''
    def _buildElements(self)->str:
        final=""
        for i in self.elements:
            final+=i+"\n"
        return final

    def getMember(self,value:str)->Member:
        """
        return members by value
        """
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
