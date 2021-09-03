from dataclasses import dataclass

@dataclass(frozen= True)

class Book:
    name:str
    author: str
    condition:str = field(default= 'new')
    reader:field(default_factory= list, compare= False, hash = False, repr= False)
    num_pages: str
    