from htmlWidget import htmlWidget
class Button(htmlWidget):
    '''
    HTML Button Class derived from htmlWidget
    '''
    code:str=""
    def __init__(self) -> None:
        self.header:str="<button>"
        self.text:str=""
        self.footer:str="</button>"
        self.options:list[str]=list[str]()
        self.CustomHeader:bool=False
        self.requiredScripts: list[str]=list[str]()
        self.style: list[str]=list[str]()
    def setText(self,text:str)->None:
        '''
        Set the Text of the Button
        '''
        self.text=text
    def setOnClick(self,functionname:str,function:str)->None:
        '''
        Set the click function of the Button
        '''
        self.options.append(f"onclick='{functionname}'")
        self.requiredScripts.append(function)
    def setTextColor(self,color:str):
        '''
        Set the color of the text on the Button
        '''
        if color.endswith(";"):color=color[-1]
        self.style.append(f"color:{color};")
    def setBackgroundColor(self,color:str)->None:
        '''
        Set the color of the background of the Button
        '''
        if color.endswith(";"):color=color[-1]
        self.style.append(f"background-color:{color};")
    def setID(self,ids:str)->None:
        '''
        Set the ID of the Button
        '''
        self.options.append(f"id={ids}")
    def _finalizeoptions(self)->str:
        final:str=""
        if "style" in self.options:
            for i in self.options:
                if i.__includes__("style"):self.style=i.split("style=")[1].split(";")  # type: ignore
                else:continue
        del self.options[self.options.index("style")]
        for i in self.options:final+=i+" "
        s:str="style=\""
        for a in self.style:
            if not a.endswith(";"):a+=";"
            if a.__contains__("\""):a.replace("\"","'")#prevent errors from occurring 
            s+=a
        s+="\""
        final+=" "+s
        return final
    def finalize(self)->None:
        '''
        Update the Button Code Variable
        '''
        if self.CustomHeader:print("Creating Button with Custom Header")
        else:print("Creating Button with Default Header")
        self.code=self.header[-1]+" "+self._finalizeoptions()+">"+self.text+self.footer