from dataclasses import dataclass
from vestis.enums.category import Category 
from typing import Optional

@dataclass
class Garment:
    name: str 
    category: Category
    colors: list[str] 
    brand: Optional[str] = None
    size: Optional[str] = None

    def __post_init__(self):
        errors: list[str] = []

        if len(self.name.strip()) == 0:
            errors.append("Una prenda debe tener un nombre")

        if len(self.colors) == 0:
            errors.append("Una prenda debe tener al menos un color.")

        if not isinstance(self.category, Category):
            errors.append("La categoria no es válida.")

        if errors:
            raise ValueError("\n".join(errors))





