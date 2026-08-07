from dataclasses import dataclass
from vestis.enums.category import Category 
from typing import Optional

@dataclass
class Garment:
    name: str 
    category: Category
    brand: Optional[str] = None 



