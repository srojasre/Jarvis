
class Functions:
    def __init__(self) -> None:
        pass
    
    def apiConnect(self):
        pass
    
    def functionCreate(self):
        try:
            pass
        
        except FunctionError:
            print(f'Class not created{'undefine'}')
        pass
    
    
    
    
    
    
class FunctionError(Exception):
    """
    Raised if class Functions is not create in proper way

    Args:
        Exception (class): type Exception
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
