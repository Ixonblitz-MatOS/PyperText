'''
Table widget for pypertext
'''
from ultraimport.ultraimport import ultraimport
htmlWidget=ultraimport('__dir__/htmlWidget.py','htmlWidget')
stripLast=ultraimport('__dir__/tools.py','stripLast')
class TableHeader(htmlWidget):
    """
    Header object for pypertext table
    """
    code=None
    type="TableHeader"
    def __init__(self) -> None:
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.header="<tr>"
        self.elements=[]
        self.CustomHeader=False
        self.footer="</tr>"
    def addStyle(self,style:str)->None:
        """
        Add style to the TR tag
        """
        if style.__contains__("style=") and style.endswith("\""):style=stripLast(style.replace("style=",""))
        self.style.append(style)
        self.CustomHeader=True
    def addOptions(self,options:str)->None:
        """
        Add options to the TR tag
        """
        self.options.append(options)
        self.CustomHeader=True
    def addText(self,value:str,style:str=None,options:str=None)->None:
        if style is None:style=""
        if options is None:options=""
        self.elements.append(f"<th {style} {options}>{value}</th>")
    def _buildOptions(self)->str:
        """
        Build options for final code
        """
        final=""
        for i in self.options:final+=f"{i} "
        return final
    def _buildStyle(self)->str:
        """
        Build Style for final code
        """
        final="style=\""
        for i in self.style:final+=f"{i} "
        return final+"\""
    def _buildElements(self)->str:
        """
        build all elements for the code finalization
        """
        final=""
        for i in self.elements:
            final+=i+"\n"
        return final
    def finalize(self)->None:
        """
        Finalize the code for the Table Header to be passed to the table
        """
        if self.CustomHeader:
            print("Table Header: Creating TableHeader with Custom Header")
            self.code=f"{stripLast(self.header)} {self._buildStyle()} {self.options}>{self._buildElements()}{self.footer}"
        print("Table Header: Creating TableHeader with Default Header")
        self.code=f"{self.header}{self._buildElements()}{self.footer}"
class TableData(htmlWidget):
    """
    Data object for pypertext table
    """
    code=None
    type="TableData"
    def __init__(self) -> None:
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.header="<tr>"
        self.elements=[]
        self.CustomHeader=False
        self.footer="</tr>"
    def addStyle(self,style:str)->None:
        """
        Add style to the TR tag
        """
        if style.__contains__("style=") and style.endswith("\""):style=stripLast(style.replace("style=",""))
        self.style.append(style)
        self.CustomHeader=True
    def addOptions(self,options:str)->None:
        """
        Add options to the TR tag
        """
        self.options.append(options)
        self.CustomHeader=True
    def addText(self,value:str,style:str=None,options:str=None)->None:
        if style is None:style=""
        if options is None:options=""
        self.elements.append(f"<td {style} {options}>{value}</td>")
    def _buildOptions(self)->str:
        """
        Build options for final code
        """
        final=""
        for i in self.options:final+=f"{i} "
        return final
    def _buildStyle(self)->str:
        """
        Build Style for final code
        """
        final="style=\""
        for i in self.style:final+=f"{i} "
        return final+"\""
    def _buildElements(self)->str:
        """
        build all elements for the code finalization
        """
        final=""
        for i in self.elements:
            final+=i+"\n"
        return final
    def finalize(self)->None:
        """
        Finalize the code for the Table Header to be passed to the table
        """
        if self.CustomHeader:
            print("Table Data: Creating TableData with Custom Header")
            self.code=f"{stripLast(self.header)} {self._buildStyle()} {self.options}>{self._buildElements()}{self.footer}"
        print("Table Data: Creating TableData with Default Header")
        self.code=f"{self.header}{self._buildElements()}{self.footer}"
class Table(htmlWidget):
    '''
    table widget for pypertext
    '''
    code=None
    type="Table"
    def __init__(self) -> None:
        self.header="<table>"
        self.elements=[]
        self.footer="</table>"
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.CustomHeader=False
    def addOptions(self,options:str)->None:
        """
        Add options to table tag
        """
        self.options.append(options)
        self.CustomHeader=True
    def addStyle(self,style:str)->None:
        """
        Add styling to the table tag
        """
        if style.__contains__("style=") and style.endswith("\""):style=stripLast(style.replace("style=",""))
        self.style.append(style)
        self.CustomHeader=True
    def addHeader(self,header:TableHeader)->None:
        """
        Adding the Table Header code to the Table
        """
        self.elements.append(header.code)
    def addData(self,data:TableData)->None:
        """
        Adding the Table Data code to the Table
        """
        self.elements.append(data.code)
    def _buildElement(self)->str:
        """
        Building the elements for finalization
        """
        final=""
        for i in self.elements:
            final+=i+"\n"
        return final
    def _buildStyle(self)->str:
        """
        Build the styling for finalization
        """
        final="style=\""
        for i in self.style:final+=f"{i} "
        return final+"\""
    def _buildOptions(self)->str:
        """
        Build the options for finalization
        """
        final=""
        for i in self.options:final+=f"{i} "
        return final
    def finalize(self)->None:
        """
        Finalize the table code
        """
        if self.CustomHeader:
            print("Table: Creating Table with Custom Header")
            self.code=f"{stripLast(self.header)} {self._buildStyle()} {self._buildOptions()}>{self._buildElement()}{self.footer}"
        print("Table: Creating Table with Default Header")
        self.code=f"{self.header}{self._buildElement()}{self.footer}"