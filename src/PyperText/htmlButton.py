"""
Button Widget for PyperText
"""
# pylint: disable=locally-disabled, invalid-name, line-too-long, super-init-not-called, unspecified-encoding
from ultraimport.ultraimport import ultraimport
htmlWidget = ultraimport('__dir__/htmlWidget.py','htmlWidget')
SuspendedString = ultraimport('__dir__/tools.py','SuspendedString')
class Button(htmlWidget):
    '''
    HTML Button Class derived from htmlWidget
    '''
    code:str=""
    type="Button"
    def __init__(self) -> None:
        self.header:str="<button>"
        self.text:str=""
        self.footer:str="</button>"
        self.options:list[str]=list[str]()
        self.CustomHeader:bool=False
        self.requiredScripts: list[str]=list[str]()
        self.style: list[str]=list[str]()
    def setText(self,text:str|SuspendedString)->None:
        '''
        Set the Text of the Button
        '''
        if isinstance(text,str):
            self.text=text
        else:
            self.text=text.form() #type:ignore
    def setOnClick(self,functionname:str,function:str)->None:
        '''
        Set the click function of the Button
        '''
        self.options.append(f"onclick=\"{functionname}\"")
        self.requiredScripts.append(function)
        self.CustomHeader=True
    def setTextColor(self,color:str):
        '''
        Set the color of the text on the Button
        '''
        if color.endswith(";"):
            color=color.rstrip(color[-1])
        self.style.append(f"color:{color};")
        self.CustomHeader=True
    def setBackgroundColor(self,color:str)->None:
        '''
        Set the color of the background of the Button
        '''
        if color.endswith(";"):
            color=color.rstrip(color[-1])
        self.style.append(f"background-color:{color};")
        self.CustomHeader=True
    def setID(self,ids:str)->None:
        '''
        Set the ID of the Button
        '''
        self.options.append(f"id=\"{ids}\"")
        self.CustomHeader=True
    def _finalizeoptions(self)->str:
        final:str=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):
                    self.style=i.split("style=")[1].split(";")[0]  # type: ignore
                else:
                    continue
            del self.options[self.options.index("style")]
        for i in self.options:
            final+=i+" "
        s:str="style=\""
        for a in self.style:
            if not a.endswith(";"):
                a+=";"
            if "\"" in a:
                a.replace("\"","'")#prevent errors from occurring
            s+=a
        s+="\""
        if  s!="style=\"\"":
            final+=" "+s
        return final
    def finalize(self)->None:
        '''
        Update the Button Code Variable
        '''
        if self.CustomHeader:
            print("Button: Creating Button with Custom Header")
        else:
            print("Button: Creating Button with Default Header")
        self.code=self.header.rstrip(self.header[-1])+" "+self._finalizeoptions()+">"+self.text+self.footer


if __name__=="__main__":
    pass
