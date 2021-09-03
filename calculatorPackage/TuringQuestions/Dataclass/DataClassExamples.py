class Book:
    
    def __init__(self, name, author, num_pages):
    
        self.__name = name
        self.__author = author
        self.__num_pages = num_pages
        
    @property
    def name(self):
        return self.__name
    
    @property
    def author(self):
        return self.__author
    
    @property
    def num_pages(self):
        return self.__num_pages
    
    
    
    def __repr__(self):
        return f"Book({self.name}, {self.author}, {self.num_pages})"
    
    def __hash__(self):
        return hash((self.__class__, self.name, self.author, self.num_pages))
    
    
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.name == other.name and self.author == other.author and \
                   self.num_pages == other.num_pages
            
        else:
            return NotImplemented
        