# Dataclass
from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
   # id:Optional[int] = None# beim Speichern vonn Books -> keine Id sondern Null
    id:int | None = None # ab Python 3.10 
    title:str=""
    author:str=""
    genre:str=""
    published_year:int=0


@dataclass
class EBook(Book):
    file_format: str = "PDF"
    file_size_mb: float = 0.0


# ebook = EBook(title="Kochbuch",author="Max",genre="Küche",published_year=2000,file_format="EPUB",file_size_mb=1.5)
# print(ebook)