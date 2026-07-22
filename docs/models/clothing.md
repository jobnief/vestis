# Clothing Model

## Overview

A Clothing object represents one physical garment.

Each garment exists only once inside the inventory.

Every garment has its own identity and attributes.

---

## Required Attributes

- ID
- Name
- Category
- Colors

---

## Optional Attributes

- Brand
- Model
- Size
- Purchase Date
- Purchase Price
- Store
- Notes
- Photos

---

## Multi-value Attributes

- Colors
- Styles
- Seasons
- Uses
- Materials
- Tags

---

## Single-value Attributes

- Name
- Category
- Subcategory
- Cut
- Size
- Condition

---

## Design Philosophy

A Clothing object should only describe itself.

It should not know how to:

- save files
- calculate statistics
- search
- generate outfits

Those responsibilities belong to other modules.
