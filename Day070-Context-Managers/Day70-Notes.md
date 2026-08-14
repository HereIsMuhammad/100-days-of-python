# Day 70: Context Managers

## Concept
Context Managers automatically handle setup and cleanup actions using the `with` statement.

- Commonly used for file operations, locks, and resources  
- Implemented via `__enter__()` and `__exit__()` methods  

## What is a Context Manager?
- Ensures proper resource management  
- Automatically calls cleanup code even if an exception occurs  

## Syntax
```python
with context_manager as variable:
    # code block
```
* `__enter__()` → executes at the start of with block

* `__exit__()` → executes at the end of with block

### Use Cases
* File operations (open/close automatically)
* Database connections
* Thread locks or resource management

### Advantages
* Avoids forgetting cleanup (like closing files)
* Handles exceptions safely
* Cleaner, more readable code
