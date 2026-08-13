# Vestis

> Vestis doesn't tell you what your wardrobe should be.  
> It helps you build the wardrobe you want.

Vestis es un gestor personal de ropa pensado para registrar, organizar y analizar un guardarropa.

El proyecto nace como una herramienta personal, pero está diseñado para poder crecer hacia un sistema más general de gestión de objetos.

## ¿Qué busca resolver?

Vestis busca permitir que una persona pueda:

- Registrar sus prendas y sus características.
- Organizar las prendas por categorías.
- Consultar y buscar prendas.
- Mantener un inventario actualizado.
- Identificar qué prendas tiene y cuáles podría necesitar.
- Registrar información relacionada con el uso de cada prenda.
- Generar estadísticas sobre el guardarropa.
- En el futuro, crear y organizar outfits.

## Estado actual

🚧 **En desarrollo**

Actualmente Vestis se encuentra en una etapa inicial de desarrollo.

Ya cuenta con:

- Estructura modular del proyecto.
- Modelo `Garment` para representar prendas.
- Categorías mediante `Enum`.
- Modelo `Wardrobe` para administrar un conjunto de prendas.
- Validación básica de los datos de una prenda.
- Registro y listado de prendas.
- Control de versiones mediante Git.

La interfaz de terminal y el almacenamiento persistente todavía están en desarrollo.

## Arquitectura

El proyecto utiliza una estructura basada en módulos:

```text
src/
└── vestis/
    ├── enums/
    │   └── category.py
    ├── models/
    │   ├── garment.py
    │   └── wardrobe.py
    ├── services/
    ├── storage/
    ├── utils/
    └── main.py
```

La intención es separar:

- **Modelos:** representan los objetos y conceptos de Vestis.
- **Enums:** contienen conjuntos de valores definidos por el sistema.
- **Services:** contienen lógica y operaciones sobre los modelos.
- **Storage:** se encargará de la persistencia de los datos.
- **Utils:** herramientas auxiliares.
- **Main:** punto de entrada de la aplicación.

## Tecnologías

Actualmente el proyecto utiliza:

- Python
- Git
- GitHub
- Linux
- Neovim

Se contempla utilizar posteriormente:

- JSON u otro sistema de almacenamiento.
- Inteligencia artificial ejecutada localmente.
- Herramientas adicionales para análisis y estadísticas.

## Roadmap

### Fase 1 · Fundamentos

- [x] Crear estructura inicial del proyecto.
- [x] Crear modelo `Category`.
- [x] Crear modelo `Garment`.
- [x] Crear modelo `Wardrobe`.
- [x] Agregar y listar prendas.
- [x] Implementar validaciones básicas.

### Fase 2 · Aplicación de terminal

- [ ] Crear menú principal.
- [ ] Permitir registrar prendas desde la terminal.
- [ ] Permitir listar prendas.
- [ ] Permitir buscar prendas.
- [ ] Permitir eliminar prendas.
- [ ] Permitir modificar prendas.

### Fase 3 · Datos

- [ ] Diseñar el sistema de almacenamiento.
- [ ] Guardar prendas de forma persistente.
- [ ] Cargar el guardarropa al iniciar Vestis.
- [ ] Crear categorías personalizadas.
- [ ] Diseñar un sistema de colores normalizado.

### Fase 4 · Gestión del guardarropa

- [ ] Filtrar prendas.
- [ ] Ordenar prendas.
- [ ] Registrar usos.
- [ ] Registrar lavados.
- [ ] Crear estadísticas.
- [ ] Crear sistema de prendas deseadas.

### Fase 5 · Funciones avanzadas

- [ ] Crear outfits.
- [ ] Analizar el guardarropa.
- [ ] Detectar posibles faltantes.
- [ ] Explorar integración con IA local.

## Filosofía del proyecto

Vestis no pretende decirle al usuario qué ropa debería tener.

Su objetivo es darle información sobre lo que ya tiene para que pueda tomar sus propias decisiones.

La aplicación debe ser:

- Flexible.
- Extensible.
- Transportable.
- Fácil de mantener.
- Independiente de servicios externos cuando sea posible.

## Proyecto de aprendizaje

Vestis también funciona como proyecto práctico para aprender:

- Python.
- Programación orientada a objetos.
- Estructuras de datos.
- Validación de información.
- Arquitectura de software.
- Git y GitHub.
- Linux.
- Neovim.
- Diseño de aplicaciones.

La idea es aprender construyendo una herramienta real, en lugar de estudiar cada concepto de forma aislada.

## Licencia

Este proyecto todavía no tiene una licencia definida.
