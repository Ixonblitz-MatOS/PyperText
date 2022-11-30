from htmlWidget import htmlWidget
class Header(htmlWidget):
    '''
    HTML Header Class derived from htmlWidget
    '''
    code:str=""
    def __init__(self,size:int) -> None:
        '''
        size:int=0< && >7
        '''
        if size<0 or size>7:print("The size was incorrectly entered and will use 3 as the default")
        self.size=size
        self.header:str=f"<h{str(size)}>"
        self.text:str=""
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.CustomHeader:bool=False
        self.footer:str=f"</h{str(size)}>"
    def addCustomOption(self,option:str)->None:
        '''
        adds custom options that aren't implemented
        '''
        self.options.append(option)
        self.CustomHeader=True
    def setText(self,text:str)->None:
        '''
        Set the Text of the header
        '''
        self.text=text
    def changeHeaderSize(self,size:int):
        '''
        Changes the size of the header
        '''
        self.header.replace(str(self.size),str(size))
        self.footer.replace(str(self.size),str(size))
        self.size=size
        self.CustomHeader=True
    def changeTextColor(self,color:str)->None:
        '''
        Changes the color of the text on the header
        '''
        self.style.append(f"color:{color}")
        self.CustomHeader=True
    def changeBackgroundColor(self,color:str)->None:
        '''
        Changes the background color of the header
        '''
        self.style.append(f"background-color:{color}")
        self.CustomHeader=True
    def setID(self,ids:str)->None:
        '''
        Set the ID for the header
        '''
        self.options.append(f"id=\"{ids}\"")
        self.CustomHeader=True
    def _buildOptions(self)->str:
        final:str=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):self.style=i.split("style=")[1].split(";")[0]  # type: ignore
                else:continue
        for i in self.options:final+=i+" "
        return final
    def _buildStyle(self)->str:
        final:str=""
        for i in self.style:
            if i.endswith(";"):final+=i
            else:final+=i+";"
        return final
    def finalize(self)->None:
        if self.CustomHeader:
            print("Finalizing with Custom Header")
            self.code=self.header[-1]+f" style=\"{self._buildStyle()}\" {self._buildOptions()}>"+self.text+self.footer
        else:
            print("Finalizing with default header")
            self.code=self.header+self.text+self.footer