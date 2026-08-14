# Day 68: Decorators

## Concept
Decorators are used to modify the behavior of functions without changing their code.

They use the `@` syntax and are based on functions inside functions.

## What is a Decorator?
- A function that wraps another function
- Adds extra functionality
- Keeps original function clean

## Syntax
```python
@decorator_name  
def function_name():
    pass
```
## How It Works

1. Define a decorator function  
2. Inside it, define a wrapper function  
3. Call the original function inside wrapper  
4. Return wrapper  

## Example Use Cases
- Logging
- Authentication
- Timing functions
- Access control

## Logging Decorator

### Concept
Print message before and after function execution.

## Why Use Decorators?
- Clean and reusable code
- Avoid repetition
- Add features without modifying original function