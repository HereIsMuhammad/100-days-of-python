# Day 74: Logging Module

## Concept
The `logging` module in Python allows you to record messages instead of using `print()`.  
It provides **different levels of messages** and is useful for debugging and monitoring applications.

## Why Logging?
- Better than `print()` for large projects  
- Can record different levels: info, warning, error, debug, critical  
- Can write logs to files for later analysis  
- Helps in debugging production code  

## Logging Levels

| Level     | Description                     |
|----------|---------------------------------|
| DEBUG    | Detailed information            |
| INFO     | General information             |
| WARNING | Something unexpected occurred   |
| ERROR    | Serious problem                 |
| CRITICAL | Very serious error              |

## Basic Setup

```python
import logging

# Basic configuration
logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Program started")
logging.warning("This is a warning")
logging.error("An error occurred")
logging.critical("Critical error!")`