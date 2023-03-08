'''
Python HTML writer for beginners
'''
# pylint: disable=locally-disabled, line-too-long,invalid-name, super-init-not-called, unspecified-encoding
#module imports
import platform #(.path.exists() to check if the path they want exists,)
import os as oss
import webbrowser
from io import TextIOWrapper
from ultraimport.ultraimport import ultraimport


baseWidget = ultraimport('__dir__/htmlWidget.py', 'baseWidget')
htmlParent = ultraimport('__dir__/htmlWidget.py','htmlParent')
htmlWidget = ultraimport('__dir__/htmlWidget/py','htmlWidget')
OS=platform.system()
if "Linux" in OS:
    OS="Linux"
elif"Darwin" in OS:
    OS="MacOS"
elif"Windows" in OS:
    OS="Windows"
else:
    print("Unknown/Unsupported OS")
    quit(1)
#classes


class Script(htmlWidget,htmlParent):
    '''
    This is the original init for the module
    '''
    code:str="Scripts Do Not hold Code for Widgets"
    def __init__(self,path:str) -> None:
        match OS:
            case "Linux":
                text=f"FILE={path}\nif test -f '$FILE'; then\n\techo 'True'\nfi"
                if(oss.popen(text).read().__contains__("True")) and oss.access(path,oss.W_OK) and oss.access(path,oss.R_OK):
                    self.file: str=path
                else:
                    print("Cannot read, write, or access file")
                    quit(1)
            case "Windows":
                text=f"IF EXIST {path} ECHO True"
                if(oss.popen(text).read().__contains__("True")) and oss.access(path,oss.W_OK) and oss.access(path,oss.R_OK):
                    self.file: str=path
                else:
                    print("Cannot read, write, or access file")
                    quit(1)
            case "MacOS":
                text=f"if [[ ! -f {path} ]]\nthen\n\techo 'True'\nfi"
                if(oss.popen(text).read().__contains__("True")) and oss.access(path,oss.W_OK) and oss.access(path,oss.R_OK):
                    self.file:str=path
                else:
                    print("Cannot read, write, or access file")
                    quit(1)
            case  _:
                print("Unknown/Unsupported OS")
                quit(1)
        self.fp: TextIOWrapper=open(self.file,'w+')
        self.text: str=""
        self.header:str="<!DOCTYPE html>\n<html>"
        self.footer:str="</html>"
        self.CustomHeader:bool=False
        self.scripts: list[str]=list[str]()
        self.final: str=str()
        self.stylesheet=None
    def addScript(self,script:str,force:bool=False)->None:
        '''
        Adds a Javascript script to the file
        '''
        if(oss.path.exists(script) and script.endswith(".js")):
            self.scripts.append(script)
        else:
            if force:
                self.scripts.append(script)
            else:
                print("Script: The file does not exist or does not end in .js, No action taken, to add the script anyway set force equal to True")
    def addCustomHeader(self,options:str)->None:
        '''
        Changes the default header
        '''
        self.header=f"<!DOCTYPE html>\n<html {options}>\n"
        self.CustomHeader=True
    def addWidget(self,wid:htmlWidget)->None:
        '''
        Adds widget to script
        '''
        print(f"Script: Adding Widget({wid.type})")
        self.text+=wid.code+"\n"
    def setStyleSheet(self,sheet:str)->None:
        '''
        Sets CSS sheet for the script
        '''
        if oss.path.exists(sheet):
            self.stylesheet=sheet
        else:print("Sheet does not exist. No Changes have been made.")
    def _buildScripts(self)->str:
        '''
        Converts scripts from list[str] to string by opening the script files and writing to a script tag. No support for script src
        '''
        final:str=""
        for i in self.scripts:
            final+=f"<script>{open(i,'r').read()}</script>\n"
        return final
    def createAndWrite(self,opens:bool=False)->None:
        '''
        Create and write the HTML for the script and write to the file.
        '''
        if self.CustomHeader:
            print("Creating With Custom Header...")
        else:
            print("Creating with Default Header")
        if self.stylesheet is None:
            self.final+=self.header+self.text+self._buildScripts()+self.footer
        else:
            self.final+=self.header+open(self.stylesheet,'r').read()+"\n"+self.text+self._buildScripts()+self.footer
        self.fp.write(self.final)
        self.fp.close()
        if opens:
            webbrowser.open_new_tab('file://'+oss.path.abspath(self.file))
if __name__=="__main__":
    pass
