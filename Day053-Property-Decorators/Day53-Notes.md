# Day 53: Property Decorators (@property)

## Concept
In Python, `@property` is used to control access to class attributes in a clean and Pythonic way.

Normally, class attributes can be accessed and changed directly. But sometimes we want to:
- protect data
- validate values before updating them
- keep internal data safe

This is where **encapsulation** comes in.

Encapsulation means hiding internal data and controlling how it is accessed or modified.

With `@property`, we can create:
- a **getter** to read a value
- a **setter** to update a value with validation

## Why Use `@property`?
`@property` is used when we want to add control over an attribute without changing how it is used.

It is useful because:
- it helps protect important data
- it allows validation before assigning values
- it improves encapsulation
- it makes code cleaner than using traditional getter and setter methods

Without `@property`, users of the class may set invalid values directly.

For example, in a bank account, balance should never be negative.  
So we use a property setter to check the value before updating it.

## Getter and Setter
A **getter** is used to return the value of an attribute.
A **setter** is used to update the value of an attribute with some rules.

In Python:
- `@property` creates the getter
- `@attribute_name.setter` creates the setter

## Balance Validation Example
In a `BankAccount` class:
- the account balance is stored in a protected way
- the getter returns the balance
- the setter checks that the balance is not negative

This keeps the data safe and valid.

## Key Points
- `@property` allows a method to be accessed like an attribute.
- It is used for encapsulation.
- A setter can validate data before updating it.
- It helps protect class data from invalid values.
- It makes code more readable and professional.

## Example Scenario
We have a `BankAccount` class with a `balance`.

We want:
- to view the balance safely
- to update the balance only if the value is valid
- to prevent negative balance assignment

Using `@property` and a setter helps us do this.

## Conclusion
`@property` is a very useful feature in Python. It allows us to control attributes more safely and cleanly. It is commonly used in real-world programs where data validation and encapsulation are important.