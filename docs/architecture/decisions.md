# Architectural Decisions

## ADR-001

The application stores one object per physical garment.

Reason:

Two visually identical garments are still different physical objects.

---

## ADR-002

Documentation is written before implementation.

Reason:

The project follows a documentation-first approach.

---

## ADR-003

A Clothing object only contains data.

Business logic belongs to services.

---

## ADR-004

Categories and attributes are independent.

Example:

Category:
Jeans

Cut:
Baggy

Style:
Streetwear

The same cut or style may exist across multiple categories.

---

## ADR-005

Multiple values are allowed only when they represent reality.

Examples:

Multiple colors

Multiple materials

Multiple styles

Multiple seasons

## ADR-006

Wardrobe plans are completely customizable.

Reason:

There is no universally correct wardrobe.

Every user has different needs,
styles,
budgets,
climates
and professions.

The application provides example plans,
but users remain in full control.
