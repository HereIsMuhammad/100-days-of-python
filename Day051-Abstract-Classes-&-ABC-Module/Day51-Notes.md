# Day 51: Abstract Classes & ABC Module

## Concept:
Abstract classes are classes that **cannot be instantiated** directly. They are used as a blueprint for other classes. Abstract classes often contain one or more **abstract methods**, which must be implemented by any subclass.

In Python, abstract classes are defined using the **`abc` module** and the decorator `@abstractmethod`.

## Why Use Abstract Classes?
- **Enforce a contract:** They ensure that all subclasses implement certain methods.
- **Prevent direct instantiation:** You don’t want a generic object of the base class.
- **Code consistency:** Makes your code structured and predictable when using inheritance.
- **Reusability:** Base functionality can be shared while forcing implementation of specific behavior in subclasses.

### Key Points:
- Abstract class **cannot be instantiated**.
- Abstract methods are **declared but not implemented** in the abstract class.
- Subclasses **must implement** all abstract methods.
- Useful for **enforcing a contract** for subclasses.

### Example Scenario:
We want a base `Shape` class but we don’t want someone to create a generic `Shape` object. Every shape must define its own `area` method.