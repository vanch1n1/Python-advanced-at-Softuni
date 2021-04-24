class Pizza:
    def __init__(self, name, dough, toppoing_capacity):
        self.__name = name
        self.__dough = dough
        
        
    @@property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @@property
    def dough(self):
        return 
    
    @dough.setter
    def dough(self, value):
        pass

    def example(self):
        self.name   # you can access it without double thunder