from vestis.models.garment import Garment
from vestis.enums.category import Category

nombre = input("¿Cómo se llama tu prenda? ")
opcion = int(input("¿Tu prenda a que categoria pertenece? \n 1-Remera \n 2-Pantalón \n 3-Campera \n 4-Boxer \n 5-Medias\n"  ) )

if opcion == 1:
    categoria = Category.REMERA
elif opcion == 2:
    categoria = Category.PANTALON
elif opcion == 3:
    categoria = Category.CAMPERA
elif opcion == 4:
    categoria = Category.BOXER
elif opcion == 5:
    categoria = Category.MEDIAS
else:
    print("No es una opción es valida")

colores = input("Agrega de que color/es esta compuesta la prenda (separa cada color con una coma: ,) ")
colores=colores.split(",")

colores_limpios = []

for color in colores:
    colores_limpios.append(color.strip())


prenda = Garment(
    name=nombre,
    category=categoria,
    colors=colores_limpios
)
print(prenda)
