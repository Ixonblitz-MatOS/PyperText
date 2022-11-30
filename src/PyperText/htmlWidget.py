class htmlWidget(object):
    '''
        Base HTML Widget class to derive from
    '''
    code:str=""
    def __repr__(self) -> str:return "<Class 'htmlWidget' at" + str(id(self))+">"
    def __str__(self):return self.__repr__()