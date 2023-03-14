"""
List objects
"""
# pylint: disable=locally-disabled, line-too-long, invalid-name, super-init-not-called, broad-except, unspecified-encoding,attribute-defined-outside-init
from typing import Any,Type
from ultraimport.ultraimport import ultraimport
Class=Any|Type[type]
stripLast=ultraimport('__dir__/tools.py','stripLast')
htmlWidget,htmlObject=ultraimport('__dir__/htmlWidget.py',{"htmlWidget":Class,"htmlObject":Class})
#if[if]==if[if[if][if]]-=[if.iff[iff[if]]]

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
        self.header=f"<!--COMM--><{self._ret('ol') if self.ordered else self._ret('ul')}>"
        self.footer=f"</{self._ret('ol') if self.ordered else self._ret('ul')}>"
        self.style:list[str]=list[str]()
        self.CustomHeader=False
    def addMember(self,member:str)->None:
        '''
        Adds an element to the list
        '''
        self.elements.append(self._lst(member))
    def addStyle(self,style:str)->None:
        """
        Add styling to ul
        """
        self.style.append(style)
        self.CustomHeader=True
    def setComment(self,comment:str)->None:
        """
        Set the optional comment
        """
        self.header.replace("<!--COMM-->",f"<!--{comment}-->")
    def _buildElements(self)->str:
        final=""
        for i in self.elements:final+=i+"\n"
        return final
    def _buildStyle(self)->str:
        """
        return members by value
        """
        final=""
        for i in self.style:final+=i+";"
        return final
    def getMember(self,value:str)->str:
        """
        return members by value
        """
        for i in self.elements:
            if i.replace("<li>","").replace("</li>","")==value:return i
    def finalize(self)->None:
        """
        Finalize the list for script
        """
        if self.header.__contains__("<!--COMM-->"):self.header.replace("<!--COMM-->","")
        if self.CustomHeader:self.code=f"{stripLast(self.header)} {self._buildStyle()}>{self._buildElements()}{self.footer}"
        self.code=f"{self.header}{self._buildElements()}{self.footer}"
class DescriptionList(htmlWidget):
    '''
    HTML Description List Class derived from htmlWidget
    '''
    code=""
    type="DescriptionList"
    def __init__(self)->None:
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.header="<!--COMM--><dl >"
        self.footer="</dl>"
        self.CustomHeader=False
    def setComment(self,comment:str)->None:
        """
        Set the optional comment
        """
        self.header.replace("<!--COMM-->",f"<!--{comment}-->")
    