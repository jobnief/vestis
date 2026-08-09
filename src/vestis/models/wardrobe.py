from dataclasses import dataclass, field  
from vestis.models.garment import Garment 

@dataclass
class Wardrobe:
    garments: list [Garment] = field(default_factory=list)

    def add_garment(self, garment: Garment):
        self.garments.append(garment)
    def list_garments(self):
        for garment in self.garments:
            print(garment)




