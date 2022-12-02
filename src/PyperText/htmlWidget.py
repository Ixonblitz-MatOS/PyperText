from typing import Any
class htmlWidget(object):
    '''
        Base HTML Widget class to derive from
    '''
    code:str=""
    type:str=""
    def __repr__(self) -> str:return "<Class 'htmlWidget' at" + str(id(self))+">"
    def __str__(self):return self.__repr__()
class htmlParent(object):
    '''
        HTML PARENT CLASS
    '''
    inf:list[Any]=list[Any]()
    def _save(self,value:Any)->None:
        '''
        Save a value from child to parent class
        '''
        self.inf.append(value)
class htmlObject(object):
    '''
    HTML Object Class (For suspended strings)
    '''
    type:str=""