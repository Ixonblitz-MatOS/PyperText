from PyperText.htmlWidget import htmlWidget
class Entry(htmlWidget):
    '''
    HTML Input Textbox Class derived from htmlWidget
    '''
    def __init__(self)->None:
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.text:str=""
        self.CustomHeader:bool=False
        self.header:str="<input>"
        self.footer:str="</input>"
    def setSize(self,width:str|int)->None:
        '''
        Set Size of Entry
        '''
        self.options.append(f"size=\"{str(width)}\"")
        self.CustomHeader=True
    def setName(self,name:str)->None:
        '''
        Set name of Entry
        '''
        self.options.append(f"name=\"{name}\"")
        self.CustomHeader=True
    def setWidth(self,width:str|int)->None:
        '''
        Set width of Entry
        '''
        self.options.append(f"width=\"{width}\"")
        self.CustomHeader=True
    def setMaxLength(self,length:str|int)->None:
        '''
        Set max length of characters allowed
        '''
        self.options.append(f"maxlength=\"{length}\"")
        self.CustomHeader=True
    def setID(self,ids:str)->None:
        '''
        Set the ID of the Entry
        '''
        self.options.append(f"id=\"{ids}\"")
        self.CustomHeader=True
    def setValue(self,val:str)->None:
        '''
        Set the value of the entry
        '''
        self.options.append(f"value=\"{val}\"")
        self.CustomHeader=True
    def setHeight(self,height:str|int)->None:
        '''
        Set the height of the entry
        '''
        self.options.append(f"height=\"{height}\"")
        self.CustomHeader=True
    def setMinLength(self,length:str|int)->None:
        '''
        Set minimum length of characters
        '''
        self.options.append(f"minlength=\"{length}\"")
        self.CustomHeader=True
    def _buildOptions(self)->str:
        final=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):self.style=i.split("style=")[1].split(";")  # type: ignore
                else:continue
        del self.options[self.options.index("style")]
        for i in self.options:final+=i+" "
        return final    
    def _buildStyle(self)->str:
        final=""
        for i in final:final+=i
        return final
    def setType(self,types:str)->None:
        '''
        Set type of the entry
        	button
            checkbox
            color
            date
            datetime-local
            email
            file
            hidden
            image
            month
            number
            password
            radio
            range
            reset
            search
            submit
            tel
            text
            time
            url
            week
        '''
        self.options.append(f"type=\"{types}\"")
    def finalize(self)->None:
        '''
        Finalize the code to self.code
        '''
        if self.CustomHeader:
            print("Finalizing with Custom Header")
            self.code=self.header[-1]+" "+self._buildOptions()+f" style=\"{self._buildStyle()}\">"+self.text+self.footer
        else:
            print("Finalizing with Default Header")
            self.code=self.header+self.text+self.footer
class NumberEntry(htmlWidget):
    '''
    HTML Number Input Textbox Class derived from htmlWidget
    '''
    def __init__(self)->None:
        self.options:list[str]=list[str]()
        self.style:list[str]=list[str]()
        self.text:str=""
        self.CustomHeader:bool=False
        self.header:str="<input>"
        self.footer:str="</input>"
        self.options.append("type=\"number\"")
    def setSize(self,width:str|int)->None:
        '''
        Set Size of Entry
        '''
        self.options.append(f"size=\"{str(width)}\"")
        self.CustomHeader=True
    def setName(self,name:str)->None:
        '''
        Set name of Entry
        '''
        self.options.append(f"name=\"{name}\"")
        self.CustomHeader=True
    def setWidth(self,width:str|int)->None:
        '''
        Set width of Entry
        '''
        self.options.append(f"width=\"{width}\"")
        self.CustomHeader=True
    def setMaxLength(self,length:str|int)->None:
        '''
        Set max length of characters allowed
        '''
        self.options.append(f"maxlength=\"{length}\"")
        self.CustomHeader=True
    def setID(self,ids:str)->None:
        '''
        Set the ID of the Entry
        '''
        self.options.append(f"id=\"{ids}\"")
        self.CustomHeader=True
    def setValue(self,val:str|int)->None:
        '''
        Set the value of the entry
        '''
        try:
            if str(val).isnumeric():self.options.append(f"value=\"{str(val)}\"")
            else:print("Invalid number for the value, no action taken")
        except (Exception):pass
        self.CustomHeader=True
    def setHeight(self,height:str|int)->None:
        '''
        Set the height of the entry
        '''
        self.options.append(f"height=\"{height}\"")
        self.CustomHeader=True
    def setMinLength(self,length:str|int)->None:
        '''
        Set minimum length of characters
        '''
        self.options.append(f"minlength=\"{length}\"")
        self.CustomHeader=True
    def _buildOptions(self)->str:
        final=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):self.style=i.split("style=")[1].split(";")[0]  # type: ignore
                else:continue
        del self.options[self.options.index("style")]
        for i in self.options:final+=i+" "
        return final    
    def _buildStyle(self)->str:
        final=""
        for i in final:final+=i
        return final
    def finalize(self)->None:
        '''
        Finalize the code to self.code
        '''
        if self.CustomHeader:
            print("Finalizing with Custom Header")
            self.code=self.header[-1]+" "+self._buildOptions()+f" style=\"{self._buildStyle()}\">"+self.text+self.footer
        else:
            print("Finalizing with Default Header")
            self.code=self.header+self.text+self.footer