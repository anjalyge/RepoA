from module_b import methodB, methodA


class C:
    def __init__(self, msg):
        self.msg = msg
        
    
    def methodC(self):
        print(f"Message from C")
        print(methodA())
        
        
        
c = C("custom message")
c.methodC()